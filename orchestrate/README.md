# IBM watsonx Orchestrate Configuration

This directory contains the workflow definitions and digital skills for the HR Onboarding Assistant.

## 📁 Directory Structure

```
orchestrate/
├── workflows/
│   └── onboarding_workflow.json    # Main onboarding workflow
└── skills/
    ├── email_skill.json             # Gmail integration
    ├── calendar_skill.json          # Google Calendar integration
    ├── slack_skill.json             # Slack integration
    ├── docs_skill.json              # Google Docs integration
    └── jira_skill.json              # Jira integration
```

## 🚀 Setup Instructions

### Step 1: Access IBM watsonx Orchestrate

1. Log into your IBM watsonx Orchestrate account
2. Navigate to the Skills section
3. Navigate to the Workflows section

### Step 2: Import Digital Skills

For each skill in the `skills/` directory:

1. Click "Create Skill" or "Import Skill"
2. Copy the JSON content from the skill file
3. Paste it into the skill editor
4. Configure the authentication credentials:
   - **Email Skill**: Gmail OAuth credentials
   - **Calendar Skill**: Google Calendar OAuth credentials
   - **Slack Skill**: Slack Bot Token
   - **Docs Skill**: Google Docs OAuth credentials
   - **Jira Skill**: Jira API token and email

### Step 3: Configure API Credentials

#### Gmail API Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable Gmail API
4. Create OAuth 2.0 credentials
5. Add credentials to skill configuration

#### Google Calendar API Setup
1. Enable Google Calendar API in Google Cloud Console
2. Create OAuth 2.0 credentials
3. Add credentials to skill configuration

#### Slack API Setup
1. Go to [api.slack.com](https://api.slack.com/apps)
2. Create a new app
3. Add `chat:write` scope
4. Install app to workspace
5. Copy Bot User OAuth Token
6. Add token to skill configuration

#### Google Docs API Setup
1. Enable Google Docs API in Google Cloud Console
2. Create OAuth 2.0 credentials
3. Add credentials to skill configuration

#### Jira API Setup
1. Go to [id.atlassian.com](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Create API token
3. Use your email and API token for basic auth
4. Add credentials to skill configuration

### Step 4: Import Workflow

1. Navigate to Workflows in Orchestrate
2. Click "Create Workflow" or "Import Workflow"
3. Copy the JSON content from `workflows/onboarding_workflow.json`
4. Paste it into the workflow editor
5. Map the skills to the imported skills
6. Test the workflow with sample data

### Step 5: Test the Workflow

Use this sample input to test:

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

## 📋 Workflow Steps

The onboarding workflow executes these steps in order:

1. **Validate Input** - Ensures all required fields are present
2. **Send Welcome Email** - Sends personalized welcome email
3. **Create Calendar Events** - Schedules orientation sessions
4. **Create Onboarding Doc** - Generates personalized onboarding document
5. **Post Slack Announcement** - Announces new hire in channels
6. **Create Jira Tasks** - Creates onboarding tasks for the team
7. **Send Confirmation** - Notifies HR of completion

## 🔧 Customization

### Adding New Steps

To add a new step to the workflow:

1. Create or use an existing skill
2. Add a new step object to the `steps` array in `onboarding_workflow.json`
3. Define dependencies using `depends_on`
4. Map input variables using `{{input.field_name}}` syntax

### Modifying Skills

Each skill can be customized by:
- Updating the `input_schema` to accept different parameters
- Modifying the `configuration` to use different endpoints
- Adding new output fields to `output_schema`

## 📚 Resources

- [IBM watsonx Orchestrate Documentation](https://www.ibm.com/docs/en/watsonx-orchestrate)
- [Digital Skills Guide](https://www.ibm.com/docs/en/watsonx-orchestrate/skills)
- [Workflow Builder Guide](https://www.ibm.com/docs/en/watsonx-orchestrate/workflows)

## 🔒 Security Notes

- Never commit API keys or tokens to version control
- Use environment variables for sensitive credentials
- Regularly rotate API tokens
- Use OAuth 2.0 where possible instead of API keys
- Review and limit API scopes to minimum required permissions


