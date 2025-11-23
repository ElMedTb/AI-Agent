# Quick Setup Guide

## Environment Variables

### Backend (.env file in backend/ directory)

Create a `.env` file in the `backend/` directory with:

```env
# IBM watsonx Orchestrate
ORCHESTRATE_API_KEY=your_orchestrate_api_key_here
ORCHESTRATE_API_URL=https://api.watsonx.orchestrate.ibm.com

# Gmail API (OAuth 2.0)
GMAIL_CLIENT_ID=your_gmail_client_id
GMAIL_CLIENT_SECRET=your_gmail_client_secret

# Slack API
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
SLACK_WORKSPACE=your-workspace-name

# Google Calendar API (OAuth 2.0)
GOOGLE_CALENDAR_CLIENT_ID=your_calendar_client_id
GOOGLE_CALENDAR_CLIENT_SECRET=your_calendar_client_secret
GOOGLE_CALENDAR_CREDENTIALS=path/to/credentials.json

# Google Docs API (OAuth 2.0)
GOOGLE_DOCS_CLIENT_ID=your_docs_client_id
GOOGLE_DOCS_CLIENT_SECRET=your_docs_client_secret

# Jira API
JIRA_API_TOKEN=your_jira_api_token
JIRA_BASE_URL=https://your-domain.atlassian.net
JIRA_EMAIL=your-email@company.com

# Flask Configuration
FLASK_ENV=development
PORT=5000
CORS_ORIGINS=http://localhost:3000
```

### Frontend (.env file in frontend/ directory)

Create a `.env` file in the `frontend/` directory with:

```env
REACT_APP_API_URL=http://localhost:5000
```

## Quick Start Commands

### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend
```bash
cd frontend
npm install
npm start
```

## Demo Mode

If you don't have API credentials yet, the backend will run in demo mode and simulate workflow execution. This allows you to test the UI and see how the system works.


