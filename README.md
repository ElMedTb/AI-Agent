# HR Onboarding Assistant - IBM watsonx Orchestrate AI Agent

## 🎯 Use Case

The **HR Onboarding Assistant** automates the repetitive tasks involved in onboarding new employees. When a new hire is added, the agent orchestrates workflows across multiple tools to:

- Send welcome emails
- Create calendar events for orientation sessions
- Generate onboarding documents
- Post announcements in Slack
- Create tasks in project management tools
- Schedule follow-up reminders

This frees HR teams to focus on high-value interactions with new employees rather than manual administrative work.

## 🏗️ System Architecture

```
┌─────────────────┐
│   React UI      │  User triggers onboarding request
│   (Frontend)    │
└────────┬────────┘
         │ HTTP/REST
         ▼
┌─────────────────┐
│  Python Backend │  Processes request, manages state
│  (Flask API)    │
└────────┬────────┘
         │ REST API
         ▼
┌─────────────────┐
│ IBM watsonx     │  Orchestrates workflow across tools
│ Orchestrate     │
└────────┬────────┘
         │
         ├──► Gmail API (Send emails)
         ├──► Google Calendar API (Schedule events)
         ├──► Slack API (Post messages)
         ├──► Google Docs API (Create documents)
         └──► Jira API (Create tasks)
```

### Components

1. **Frontend (React)**: Simple UI to trigger onboarding workflows
2. **Backend (Python Flask)**: REST API that communicates with Orchestrate
3. **IBM watsonx Orchestrate**: Workflow orchestration engine
4. **Digital Skills**: Pre-built integrations for external tools
5. **External APIs**: Gmail, Google Calendar, Slack, Google Docs, Jira

## 📁 Project Structure

```
.
├── backend/
│   ├── app.py                 # Flask application
│   ├── orchestrate_client.py  # Orchestrate API client
│   ├── config.py              # Configuration
│   ├── requirements.txt       # Python dependencies
│   └── sample_data.py         # Sample data generator
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js             # Main React component
│   │   ├── index.js           # React entry point
│   │   └── styles.css         # Styling
│   ├── package.json           # Node dependencies
│   └── README.md              # Frontend setup
├── orchestrate/
│   ├── workflows/
│   │   └── onboarding_workflow.json  # Workflow definition
│   ├── skills/
│   │   ├── email_skill.json          # Email skill
│   │   ├── calendar_skill.json        # Calendar skill
│   │   ├── slack_skill.json           # Slack skill
│   │   ├── docs_skill.json            # Docs skill
│   │   └── jira_skill.json            # Jira skill
│   └── README.md                      # Orchestrate setup
└── README.md                   # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 14+
- IBM watsonx Orchestrate account and API credentials
- API keys for external services (Gmail, Slack, Google Calendar, etc.)

### Step 1: Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file in the `backend/` directory:

```env
ORCHESTRATE_API_KEY=your_orchestrate_api_key
ORCHESTRATE_API_URL=https://api.watsonx.orchestrate.ibm.com
GMAIL_CLIENT_ID=your_gmail_client_id
GMAIL_CLIENT_SECRET=your_gmail_client_secret
SLACK_BOT_TOKEN=xoxb-your-slack-token
GOOGLE_CALENDAR_CREDENTIALS=path/to/credentials.json
JIRA_API_TOKEN=your_jira_token
JIRA_BASE_URL=https://your-domain.atlassian.net
```

Run the backend:

```bash
python app.py
```

The backend will start on `http://localhost:5000`

### Step 2: Frontend Setup

```bash
cd frontend
npm install
npm start
```

The frontend will start on `http://localhost:3000`

### Step 3: Orchestrate Setup

1. Log into IBM watsonx Orchestrate
2. Import the skills from `orchestrate/skills/`
3. Import the workflow from `orchestrate/workflows/onboarding_workflow.json`
4. Configure API credentials for each skill
5. Test the workflow

### Step 4: Test the Agent

1. Open `http://localhost:3000`
2. Fill in the new employee details
3. Click "Start Onboarding"
4. Watch the orchestration happen!

## 🔄 Workflow Steps

The onboarding workflow consists of these steps:

1. **Validate Input**: Check that all required fields are provided
2. **Send Welcome Email**: Compose and send personalized welcome email
3. **Create Calendar Events**: Schedule orientation and check-in meetings
4. **Generate Onboarding Doc**: Create a personalized onboarding document
5. **Post Slack Announcement**: Announce new hire in relevant channels
6. **Create Jira Tasks**: Set up onboarding tasks for the team
7. **Send Confirmation**: Notify HR that onboarding is complete

## 🔌 API Integrations

### Gmail API
- **Purpose**: Send welcome emails
- **Endpoint**: `POST /gmail/v1/users/me/messages/send`
- **Authentication**: OAuth 2.0

### Google Calendar API
- **Purpose**: Schedule orientation sessions
- **Endpoint**: `POST /calendar/v3/calendars/primary/events`
- **Authentication**: OAuth 2.0

### Slack API
- **Purpose**: Post announcements
- **Endpoint**: `POST /api/chat.postMessage`
- **Authentication**: Bot Token

### Google Docs API
- **Purpose**: Create onboarding documents
- **Endpoint**: `POST /docs/v1/documents`
- **Authentication**: OAuth 2.0

### Jira API
- **Purpose**: Create onboarding tasks
- **Endpoint**: `POST /rest/api/3/issue`
- **Authentication**: API Token

## 📝 Example Request

```json
{
  "employee_name": "John Doe",
  "email": "john.doe@company.com",
  "department": "Engineering",
  "start_date": "2024-02-15",
  "manager": "Jane Smith",
  "position": "Software Engineer"
}
```

## 📝 Example Response

```json
{
  "status": "success",
  "workflow_id": "wf_123456",
  "actions_completed": [
    "Welcome email sent to john.doe@company.com",
    "Calendar events created for orientation",
    "Onboarding document created: Onboarding_John_Doe",
    "Slack announcement posted in #general",
    "Jira tasks created: ONB-123, ONB-124"
  ],
  "summary": "Onboarding workflow completed successfully for John Doe"
}
```

## 🛠️ Development

### Running in Development Mode

Backend:
```bash
cd backend
export FLASK_ENV=development
python app.py
```

Frontend:
```bash
cd frontend
npm start
```

### Testing

Backend tests:
```bash
cd backend
pytest tests/
```

## 📚 Additional Resources

- [IBM watsonx Orchestrate Documentation](https://www.ibm.com/docs/en/watsonx-orchestrate)
- [Digital Skills Catalog](https://www.ibm.com/docs/en/watsonx-orchestrate/skills)
- [API Reference](https://www.ibm.com/docs/en/watsonx-orchestrate/api)

## 🤝 Contributing

This is a hackathon project. Feel free to extend it with:
- More integrations (Notion, Asana, etc.)
- AI-powered personalization
- Analytics dashboard
- Multi-language support

## 📄 License

MIT License - Feel free to use this for your hackathon!


