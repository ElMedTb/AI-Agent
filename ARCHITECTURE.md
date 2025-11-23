# System Architecture

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         User Interface                           │
│                    (React Frontend - Port 3000)                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  • Employee Onboarding Form                              │   │
│  │  • Workflow Status Display                                │   │
│  │  • Results Summary                                        │   │
│  └──────────────────────────────────────────────────────────┘   │
└────────────────────────────┬────────────────────────────────────┘
                             │ HTTP/REST API
                             │ (JSON)
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Backend API Layer                          │
│                   (Flask - Port 5000)                           │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  • Request Validation                                     │   │
│  │  • Orchestrate Client                                     │   │
│  │  • Error Handling                                         │   │
│  │  • Response Formatting                                    │   │
│  └──────────────────────────────────────────────────────────┘   │
└────────────────────────────┬────────────────────────────────────┘
                             │ REST API
                             │ (IBM watsonx Orchestrate API)
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              IBM watsonx Orchestrate Platform                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              Workflow Orchestration Engine                │   │
│  │  ┌────────────────────────────────────────────────────┐  │   │
│  │  │  Step 1: Validate Input                            │  │   │
│  │  │  Step 2: Send Welcome Email                        │  │   │
│  │  │  Step 3: Create Calendar Events                    │  │   │
│  │  │  Step 4: Create Onboarding Document                │  │   │
│  │  │  Step 5: Post Slack Announcement                   │  │   │
│  │  │  Step 6: Create Jira Tasks                         │  │   │
│  │  │  Step 7: Send Confirmation                          │  │   │
│  │  └────────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────┘   │
└────────────────────────────┬────────────────────────────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  Gmail API   │    │ Google APIs  │    │  Slack API   │
│              │    │              │    │              │
│ • Send Email │    │ • Calendar   │    │ • Post Msg   │
│              │    │ • Docs       │    │              │
└──────────────┘    └──────────────┘    └──────────────┘
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                             ▼
                    ┌──────────────┐
                    │   Jira API   │
                    │              │
                    │ • Create Task│
                    └──────────────┘
```

## Component Details

### 1. Frontend (React)
- **Purpose**: User interface for triggering onboarding workflows
- **Technology**: React 18, Axios for API calls
- **Features**:
  - Form validation
  - Real-time status updates
  - Sample data generator
  - Responsive design

### 2. Backend (Flask)
- **Purpose**: API layer that communicates with Orchestrate
- **Technology**: Python Flask, Flask-CORS
- **Endpoints**:
  - `POST /api/onboard` - Start onboarding workflow
  - `GET /api/workflow/status/<id>` - Get workflow status
  - `GET /api/sample-data` - Generate sample data
  - `GET /api/skills` - List available skills
  - `GET /health` - Health check

### 3. IBM watsonx Orchestrate
- **Purpose**: Workflow orchestration engine
- **Features**:
  - Step-by-step workflow execution
  - Dependency management
  - Error handling and retries
  - Digital skills integration

### 4. Digital Skills
- **Email Skill**: Gmail API integration
- **Calendar Skill**: Google Calendar API integration
- **Slack Skill**: Slack Web API integration
- **Docs Skill**: Google Docs API integration
- **Jira Skill**: Jira REST API integration

## Data Flow

1. **User Input**: User fills form in React UI
2. **API Request**: Frontend sends POST to `/api/onboard`
3. **Validation**: Backend validates input data
4. **Orchestrate Call**: Backend calls Orchestrate API with workflow ID
5. **Workflow Execution**: Orchestrate executes steps sequentially
6. **Skill Execution**: Each step calls respective digital skill
7. **External API Calls**: Skills make API calls to external services
8. **Response**: Results flow back through Orchestrate → Backend → Frontend
9. **Display**: Frontend shows completion summary

## Error Handling

- **Frontend**: Catches API errors and displays user-friendly messages
- **Backend**: Validates input, handles Orchestrate API errors
- **Orchestrate**: Retries failed steps, handles skill errors
- **Skills**: Return error status for failed API calls

## Security

- **Authentication**: OAuth 2.0 for Google APIs, Bearer tokens for Slack/Jira
- **API Keys**: Stored in environment variables, never committed
- **CORS**: Configured for frontend origin only
- **Input Validation**: All inputs validated before processing

## Scalability

- **Stateless Backend**: Can scale horizontally
- **Orchestrate**: Handles concurrent workflows
- **Skills**: Can be rate-limited per API provider
- **Frontend**: Static build can be served from CDN


