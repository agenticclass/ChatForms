# System Architecture

## Overview
The application will be built using Python with Jinja templating for server-side rendering. Supabase will serve as the backend-as-a-service, handling authentication, database, and storage needs.

## Tech Stack
- **Frontend**: Jinja templates with HTML/CSS/JavaScript
- **Backend**: Python (Flask/FastAPI)
- **Database**: Supabase PostgreSQL
- **Authentication**: Supabase Auth with Google OAuth
- **Storage**: Supabase Storage
- **Hosting**: Supabase Edge Functions

## Application Structure
```
project/
├── app/
│   ├── templates/          # Jinja templates
│   ├── static/             # Static assets
│   ├── routes/             # Application routes
│   ├── models/             # Database models
│   └── services/           # Business logic
├── config.py               # Configuration
├── requirements.txt        # Python dependencies
└── main.py                 # Application entry point
```

## Authentication Flow
1. User clicks "Login with Google"
2. Application redirects to Supabase Auth
3. Supabase handles OAuth with Google
4. Supabase returns JWT token
5. Application stores token securely
6. Subsequent requests include token for authorization

## Database Design
- Users table (managed by Supabase Auth)
- Custom tables for application data
- Row-level security enabled
- PostgreSQL functions for complex queries

## Storage Architecture
- Supabase Storage for user uploads
- Buckets organized by content type
- Signed URLs for secure access
- Automatic image optimization

## Deployment Strategy
1. Build Python application
2. Package with required dependencies
3. Deploy to Supabase Edge Functions
4. Configure custom domain
5. Set up CI/CD pipeline

## Key Integration Points
1. Supabase Auth for authentication
2. Supabase PostgreSQL for database
3. Supabase Storage for file uploads
4. Supabase Edge Functions for hosting
5. Google OAuth for social login

## Security Considerations
- Row-level security in database
- JWT token validation
- HTTPS enforced
- Rate limiting
- Input validation
- Secure storage of credentials
