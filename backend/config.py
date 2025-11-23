"""
Configuration settings for the HR Onboarding Assistant
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration"""
    
    # Orchestrate settings
    ORCHESTRATE_API_KEY = os.getenv('ORCHESTRATE_API_KEY', '')
    ORCHESTRATE_API_URL = os.getenv('ORCHESTRATE_API_URL', 'https://api.watsonx.orchestrate.ibm.com')
    
    # Gmail settings
    GMAIL_CLIENT_ID = os.getenv('GMAIL_CLIENT_ID', '')
    GMAIL_CLIENT_SECRET = os.getenv('GMAIL_CLIENT_SECRET', '')
    
    # Slack settings
    SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN', '')
    SLACK_WORKSPACE = os.getenv('SLACK_WORKSPACE', '')
    
    # Google Calendar settings
    GOOGLE_CALENDAR_CREDENTIALS = os.getenv('GOOGLE_CALENDAR_CREDENTIALS', '')
    
    # Jira settings
    JIRA_API_TOKEN = os.getenv('JIRA_API_TOKEN', '')
    JIRA_BASE_URL = os.getenv('JIRA_BASE_URL', '')
    JIRA_EMAIL = os.getenv('JIRA_EMAIL', '')
    
    # Flask settings
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    PORT = int(os.getenv('PORT', 5000))
    DEBUG = FLASK_ENV == 'development'
    
    # CORS settings
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:3000').split(',')


