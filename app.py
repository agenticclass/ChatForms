from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, AsyncClient
import os
import httpx
from dotenv import load_dotenv
from typing import Optional
from src.routes import landing

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase: AsyncClient = create_client(
    supabase_url=os.getenv("SUPABASE_URL"),
    supabase_key=os.getenv("SUPABASE_KEY")
)

# Configure API settings
API_BASE_URL = os.getenv("BaseUrl")
API_MODEL = os.getenv("modelId")
API_KEY = os.getenv("APIKey")

app = FastAPI()

# Include landing routes
app.include_router(landing.router)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize API client
class APIClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.model = API_MODEL
        self.api_key = API_KEY
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    async def chat(self, messages):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/v1/chat/completions",
                headers=self.headers,
                json={
                    "model": self.model,
                    "messages": messages,
                    "temperature": 0.7
                }
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]

api_client = APIClient()

# Mount static files
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Configure templates
templates = Jinja2Templates(directory="src/templates")

# OAuth2 scheme
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    tokenUrl=f"{os.getenv('SUPABASE_URL')}/auth/v1/token",
    authorizationUrl=f"{os.getenv('SUPABASE_URL')}/auth/v1/authorize"
)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        user = await supabase.auth.get_user(token)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        return user
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

@app.get("/login")
async def login():
    # Redirect to Supabase Google OAuth
    return {
        "redirect_url": f"{os.getenv('SUPABASE_URL')}/auth/v1/authorize?provider=google"
    }

@app.get("/auth/callback")
async def auth_callback(code: str):
    try:
        # Exchange code for token
        session = await supabase.auth.sign_in_with_oauth({
            "provider": "google",
            "options": {
                "redirect_to": f"{os.getenv('SUPABASE_URL')}/auth/callback"
            }
        })
        return {"access_token": session.access_token, "refresh_token": session.refresh_token}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/chat")
async def chat(request: Request, user: dict = Depends(get_current_user)):
    data = await request.json()
    try:
        response = await api_client.chat(data["messages"])
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
