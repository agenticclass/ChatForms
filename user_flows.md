# ChatForm User Flows

## Landing Page Flow

### Pages:
1. **Landing Page**
   - Navigation with Google OAuth
   - Hero section with CTAs
   - Features section
   - Comparison section (vs Google Forms)
   - Testimonials section
   - Footer
   - Navigation to:
     - Dashboard (after authentication)
     - Features/Comparison/Testimonials sections

### Navigation Flow:
1. Landing Page → Dashboard (after authentication)

## Preparer (Form Creator) Flow

### Pages:
1. **Dashboard**
   - List of existing campaigns
   - Create New Campaign button
   - Campaign statistics overview
   - Navigation to:
     - Campaign Details
     - Form Creation
     - Analytics

2. **Campaign Creation Page**
   - Campaign naming and description
   - Objective selection
   - Target audience definition
   - Advanced settings configuration
   - Navigation to:
     - Form Configuration
     - Preview

3. **Form Configuration Page**
   - Objective-driven question generation
   - Manual question addition/editing
   - Question type selection
   - Response validation rules
   - Conditional logic setup
   - Navigation to:
     - Preview
     - Save/Exit

4. **Preview Page**
   - Form simulation
   - Test functionality
   - Navigation to:
     - Edit Form
     - Publish

5. **Analytics Dashboard**
   - Real-time response tracking
   - Response rate monitoring
   - Export options
   - Navigation to:
     - Individual Response Details
     - Campaign Settings

6. **Response Details Page**
   - Individual response analysis
   - Conversation history
   - Navigation back to Analytics Dashboard

### Navigation Flow:
1. Landing Page → Dashboard (after authentication)
2. Dashboard → Campaign Creation
3. Campaign Creation → Form Configuration
4. Form Configuration ↔ Preview
5. Preview → Publish → Dashboard
6. Dashboard → Analytics
7. Analytics ↔ Response Details

## Responder (Form Respondent) Flow

### Pages:
1. **Form Landing Page**
   - Campaign information
   - Start button
   - Optional authentication
   - Navigation to:
     - Conversation Interface

2. **Conversation Interface**
   - Chat-style question flow
   - Input validation
   - Progress indicator
   - Navigation to:
     - Completion Page

3. **Completion Page**
   - Summary of responses
   - Thank you message
   - Feedback collection
   - Optional redirection

### Navigation Flow:
1. Form Landing Page → Conversation Interface
2. Conversation Interface → Completion Page
3. Completion Page → (Optional) External Redirect

## Common Navigation Elements
- Header with logo and navigation menu
- Footer with legal information
- Help/Support access from all pages
- Account settings access (for authenticated users)
