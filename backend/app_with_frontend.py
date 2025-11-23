"""
Flask Backend with Frontend Serving for Single-Deployment
Use this for Replit, Railway, Render, etc.
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from dotenv import load_dotenv
from orchestrate_client import OrchestrateClient
from sample_data import generate_sample_employee_data
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='../frontend/build', static_url_path='')
CORS(app)  # Enable CORS for frontend

# Initialize Orchestrate client
orchestrate_client = OrchestrateClient(
    api_key=os.getenv('ORCHESTRATE_API_KEY'),
    api_url=os.getenv('ORCHESTRATE_API_URL', 'https://api.watsonx.orchestrate.ibm.com')
)


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'HR Onboarding Assistant API'
    }), 200


@app.route('/api/onboard', methods=['POST'])
def start_onboarding():
    """
    Start onboarding workflow for a new employee
    
    Expected payload:
    {
        "employee_name": "John Doe",
        "email": "john.doe@company.com",
        "department": "Engineering",
        "start_date": "2024-02-15",
        "manager": "Jane Smith",
        "position": "Software Engineer"
    }
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['employee_name', 'email', 'department', 'start_date']
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            return jsonify({
                'status': 'error',
                'message': f'Missing required fields: {", ".join(missing_fields)}'
            }), 400
        
        logger.info(f"Starting onboarding workflow for {data['employee_name']}")
        
        # Trigger Orchestrate workflow
        workflow_result = orchestrate_client.execute_workflow(
            workflow_id='onboarding_workflow',
            input_data=data
        )
        
        if workflow_result.get('status') == 'success':
            return jsonify({
                'status': 'success',
                'workflow_id': workflow_result.get('workflow_id'),
                'actions_completed': workflow_result.get('actions_completed', []),
                'summary': f"Onboarding workflow completed successfully for {data['employee_name']}"
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'message': workflow_result.get('error', 'Workflow execution failed')
            }), 500
            
    except Exception as e:
        logger.error(f"Error in onboarding workflow: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/workflow/status/<workflow_id>', methods=['GET'])
def get_workflow_status(workflow_id):
    """Get status of a running workflow"""
    try:
        status = orchestrate_client.get_workflow_status(workflow_id)
        return jsonify(status), 200
    except Exception as e:
        logger.error(f"Error getting workflow status: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/sample-data', methods=['GET'])
def get_sample_data():
    """Generate sample employee data for testing"""
    try:
        sample_data = generate_sample_employee_data()
        return jsonify(sample_data), 200
    except Exception as e:
        logger.error(f"Error generating sample data: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/skills', methods=['GET'])
def list_skills():
    """List available digital skills"""
    try:
        skills = orchestrate_client.list_skills()
        return jsonify({
            'status': 'success',
            'skills': skills
        }), 200
    except Exception as e:
        logger.error(f"Error listing skills: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)

