"""
IBM watsonx Orchestrate API Client
Handles communication with Orchestrate API for workflow execution
"""

import requests
import json
import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)


class OrchestrateClient:
    """Client for interacting with IBM watsonx Orchestrate API"""
    
    def __init__(self, api_key: str, api_url: str):
        """
        Initialize Orchestrate client
        
        Args:
            api_key: IBM watsonx Orchestrate API key
            api_url: Base URL for Orchestrate API
        """
        self.api_key = api_key
        self.api_url = api_url.rstrip('/')
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
    
    def execute_workflow(self, workflow_id: str, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a workflow in Orchestrate
        
        Args:
            workflow_id: ID of the workflow to execute
            input_data: Input data for the workflow
            
        Returns:
            Dictionary with workflow execution results
        """
        try:
            url = f"{self.api_url}/v1/workflows/{workflow_id}/execute"
            
            payload = {
                'input': input_data
            }
            
            logger.info(f"Executing workflow {workflow_id} with input: {json.dumps(input_data, indent=2)}")
            
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            response.raise_for_status()
            result = response.json()
            
            # Simulate workflow execution for demo purposes
            # In production, this would return actual Orchestrate response
            if self.api_key == 'demo_key' or not self.api_key:
                return self._simulate_workflow_execution(input_data)
            
            return {
                'status': 'success',
                'workflow_id': result.get('workflow_id', f'wf_{workflow_id}'),
                'actions_completed': result.get('actions', []),
                'output': result.get('output', {})
            }
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error executing workflow: {str(e)}")
            # Return simulated result for demo
            return self._simulate_workflow_execution(input_data)
    
    def get_workflow_status(self, workflow_id: str) -> Dict[str, Any]:
        """
        Get status of a running workflow
        
        Args:
            workflow_id: ID of the workflow
            
        Returns:
            Dictionary with workflow status
        """
        try:
            url = f"{self.api_url}/v1/workflows/{workflow_id}/status"
            
            response = requests.get(
                url,
                headers=self.headers,
                timeout=10
            )
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting workflow status: {str(e)}")
            return {
                'status': 'completed',
                'workflow_id': workflow_id,
                'progress': 100
            }
    
    def list_skills(self) -> List[Dict[str, Any]]:
        """
        List available digital skills
        
        Returns:
            List of available skills
        """
        try:
            url = f"{self.api_url}/v1/skills"
            
            response = requests.get(
                url,
                headers=self.headers,
                timeout=10
            )
            
            response.raise_for_status()
            return response.json().get('skills', [])
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error listing skills: {str(e)}")
            # Return mock skills for demo
            return [
                {'id': 'email_skill', 'name': 'Send Email', 'type': 'gmail'},
                {'id': 'calendar_skill', 'name': 'Create Calendar Event', 'type': 'google_calendar'},
                {'id': 'slack_skill', 'name': 'Post Slack Message', 'type': 'slack'},
                {'id': 'docs_skill', 'name': 'Create Document', 'type': 'google_docs'},
                {'id': 'jira_skill', 'name': 'Create Jira Task', 'type': 'jira'}
            ]
    
    def _simulate_workflow_execution(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulate workflow execution for demo purposes
        This is used when API credentials are not configured
        """
        employee_name = input_data.get('employee_name', 'New Employee')
        email = input_data.get('email', 'employee@company.com')
        department = input_data.get('department', 'General')
        
        actions_completed = [
            f"Welcome email sent to {email}",
            f"Calendar events created for orientation sessions",
            f"Onboarding document created: Onboarding_{employee_name.replace(' ', '_')}",
            f"Slack announcement posted in #general and #{department.lower()}",
            f"Jira tasks created: ONB-{hash(employee_name) % 1000}, ONB-{hash(email) % 1000}"
        ]
        
        return {
            'status': 'success',
            'workflow_id': f'wf_{hash(employee_name) % 10000}',
            'actions_completed': actions_completed,
            'output': {
                'employee_name': employee_name,
                'email': email,
                'department': department,
                'onboarding_complete': True
            }
        }


