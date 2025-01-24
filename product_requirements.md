# ChatForm Product Requirements Document

## 1. Introduction
### 1.1 Product Overview
ChatForm is an AI-powered conversational form platform that revolutionizes data collection by replacing static forms with intelligent, adaptive conversations. It enables businesses to collect better insights with less effort through dynamic, context-aware conversations that adapt to each responder's unique situation while maintaining the preparer's data collection objectives.

### 1.2 Objectives
- Transform traditional form creation into an objective-driven process
- Provide an engaging, conversational interface for responders
- Deliver real-time analytics and insights for preparers
- Ensure enterprise-grade security and scalability
- Reduce form creation time by 50% while increasing response rates by 40%

### 1.3 Key Features
#### For Preparers:
- Objective-Driven Forms
- Smart Question Generation
- Optional Fixed Questions
- Response Limit Control
- Multi-Channel Distribution
- Authentication Options
- Campaign Management
- Advanced Analytics
- Report Generation

#### For Responders:
- Conversational Interface
- Context-Aware Responses
- Optional Authentication
- Guided Experience
- Efficient Completion

## 2. User Flows
### 2.1 Preparer Flow
#### 2.1.1 Account Creation & Authentication
- New user sign-up with Google OAuth

#### 2.1.2 Campaign Creation
- Campaign naming and description
- Objective selection from predefined templates
- Target audience definition
- Advanced settings (e.g., response limits, branching logic)
- Preview and test functionality

#### 2.1.3 Form Configuration
- Objective-driven question generation
- Manual question addition and editing
- Question type selection (multiple choice, open-ended, rating, etc.)
- Response validation rules
- Preparer clicks on New Survey/Poll and uses Chat interface for prepare for the survey. 
- Conditional logic configuration
- AI-powered question suggestions
- Real-time conversation flow visualization
- Preparer can load the Survey and chat for insights or summary based on the responses received so far.

#### 2.1.4 Distribution & Monitoring
- Link generation with tracking parameters
- Email invitation system with templates
- Social media sharing options
- Real-time response tracking dashboard
- Response rate monitoring
- Automated reminders for incomplete responses
- Export options for response data
- Campaign performance analytics

### 2.2 Responder Flow
#### 2.2.1 Form Access
- Landing page with campaign information as provided by the preparer to be presented to responder.
- Authentication (if preparer needs the responder to authenticate using Google OAuth)
- Privacy policy and terms of service
- Mobile-responsive interface
- Progress indicator
- Chat interface for response collection
- Accessibility features (screen reader support, high contrast mode)

#### 2.2.2 Conversation Flow
- Chat-style interface with typing indicators
- Context-aware question sequencing
- Input validation and error handling
- Option to skip or go back to previous questions
- Real-time feedback on responses
- AI-powered clarification requests
- Time estimation for completion
- Save and resume functionality

#### 2.2.3 Completion & Feedback
- Summary of responses
- Option to edit answers before submission
- Thank you message with next steps
- Feedback collection about the form experience
- Redirection to preparer's website (if configured)
- Email confirmation of submission

## 3. Backend Requirements
### 3.1 Core Services
#### Authentication Service
- Python-based authentication middleware
- Supabase Auth integration with Google OAuth
- JWT token generation and validation
- Session management with refresh tokens
- Rate limiting for authentication endpoints
- Audit logging for security events

#### Form Management Service
- RESTful API endpoints for form CRUD operations
- Jinja2 templates for form rendering
- Version control for form configurations
- Collaboration features with real-time updates
- Form validation and sanitization
- Export/import functionality for forms

#### Conversation Engine
- OpenAI API integration with GPT-4
- Context management for ongoing conversations
- Dynamic question generation based on responses
- Conversation state persistence
- Rate limiting and error handling
- Conversation analytics tracking

#### Analytics Service
- Real-time data processing pipeline
- Supabase database integration
- Data aggregation and transformation
- Report generation with Jinja2 templates
- API endpoints for data visualization
- Data export functionality (CSV, JSON)

#### Notification Service
- Email notification system with templates
- Real-time web notifications
- Notification preferences management
- Delivery status tracking
- Rate limiting and retry mechanism
- Supabase storage for notification templates

### 3.2 API Specifications
#### OpenAI API Integration
- Endpoint: /api/v1/chat
- Input: User context, conversation history
- Output: Next question or response
- Rate limiting: 100 requests/minute
- Error handling: Retry mechanism with exponential backoff
- Context window management
- Prompt engineering for optimal responses

#### Supabase Integration
- Authentication: /api/v1/auth
- Database: /api/v1/data
- Storage: /api/v1/storage
- Real-time: /api/v1/realtime
- Rate limiting per endpoint
- Error handling and retry logic
- Connection pooling and optimization

### 3.3 Database Schema
#### Users Table
- id (UUID)
- email (string)
- created_at (timestamp)
- last_login (timestamp)
- role (enum: admin, manager, user)
- preferences (jsonb)
- metadata (jsonb)

#### Forms Table
- id (UUID)
- owner_id (UUID)
- title (string)
- config (jsonb)
- created_at (timestamp)
- updated_at (timestamp)
- version (integer)
- collaborators (UUID[])
- status (enum: draft, active, archived)

#### Responses Table
- id (UUID)
- form_id (UUID)
- user_id (UUID)
- answers (jsonb)
- completed_at (timestamp)
- session_data (jsonb)
- metadata (jsonb)

### 3.4 AI Integration
- OpenAI GPT-4 for conversational question generation
- Context-aware response processing
- Dynamic question branching based on responses
- Sentiment analysis for response quality
- Natural language understanding for open-ended responses
- Conversation summarization
- Response clustering and pattern detection
- Real-time feedback analysis

## 4. UI/UX Guidelines
### 4.1 Design Principles
- Chat-first interface for all interactions
- Consistent chat experience across roles
- Mobile-friendly responsive design
- Clear visual feedback for actions

### 4.2 Preparer Interface (MVP)
#### Dashboard
- Simple list of campaigns
- Chat button to create new form
- Basic response count display

#### Form Creation Chat
- Chat interface for defining form objectives
- AI-assisted question generation
- Preview of generated form
- Save and publish functionality

#### Form Analysis Chat
- Chat interface to analyze responses
- Basic statistics and insights
- Export responses as CSV

### 4.3 Responder Interface (MVP)
#### Form Access
- Clean landing page with form title
- Start chat upon landing or opening the link and optional authentication as per preparer
- The bot starts the conversation welcoming the responder and communicates the objective of the survey.
- Progress indicator

#### Conversation Flow
- Simple chat interface
- AI-driven question flow
- Basic input validation
- Submit button at end

## 5. Security Requirements
### 5.1 Authentication
- Implement OAuth 2.0 with Supabase Auth and use Google OAuth
- Support for Google authentication


## 6. Success Metrics
### 6.1 Key Performance Indicators
- **Form Creation Time**: Average time to create a new form (target: <5 minutes)
- **Response Rate**: Percentage of invited users who complete forms (target: >60%)
- **Completion Rate**: Percentage of started forms that are completed (target: >85%)
- **User Satisfaction**: Net Promoter Score (target: >70)
- **System Uptime**: Percentage of time system is operational (target: 99.9%)
- **Response Time**: Average API response time (target: <500ms)
- **Error Rate**: Percentage of failed requests (target: <0.1%)

### 6.2 Monitoring & Reporting
- Real-time dashboard for system health metrics
- Daily/weekly/monthly performance reports
- Automated alerts for critical metrics
- User feedback collection and analysis
- A/B testing framework for new features
- Regular review of key metrics with stakeholders
- Integration with business intelligence tools
