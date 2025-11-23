"""
Streamlit UI for HR Onboarding Assistant
Alternative to React frontend - Python-only solution
"""

import streamlit as st
import requests
import json
from datetime import datetime, timedelta
import random

# Page config
st.set_page_config(
    page_title="HR Onboarding Assistant",
    page_icon="🤖",
    layout="wide"
)

# API URL
API_BASE_URL = st.secrets.get("API_URL", "http://localhost:5000")

# Sample data
SAMPLE_NAMES = [
    "John Doe", "Jane Smith", "Michael Johnson", "Emily Davis",
    "David Wilson", "Sarah Brown", "Robert Taylor", "Jessica Martinez"
]

DEPARTMENTS = [
    "Engineering", "Marketing", "Sales", "HR", "Finance",
    "Operations", "Product", "Design", "Customer Success"
]

def load_sample_data():
    """Generate sample employee data"""
    name = random.choice(SAMPLE_NAMES)
    department = random.choice(DEPARTMENTS)
    start_date = (datetime.now() + timedelta(days=random.randint(7, 30))).strftime("%Y-%m-%d")
    first_name, last_name = name.lower().split()
    email = f"{first_name}.{last_name}@company.com"
    
    return {
        "employee_name": name,
        "email": email,
        "department": department,
        "start_date": start_date,
        "manager": random.choice(["Alice Johnson", "Bob Williams", "Carol Davis"]),
        "position": f"{department} Team Member"
    }

def main():
    # Header
    st.title("🤖 HR Onboarding Assistant")
    st.markdown("**Powered by IBM watsonx Orchestrate**")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("📋 Quick Actions")
        if st.button("🔄 Load Sample Data"):
            sample = load_sample_data()
            for key, value in sample.items():
                st.session_state[key] = value
            st.success("Sample data loaded!")
        
        st.markdown("---")
        st.markdown("### ℹ️ About")
        st.markdown("""
        This assistant automates the complete onboarding process:
        - ✉️ Welcome emails
        - 📅 Calendar events
        - 📄 Onboarding documents
        - 💬 Slack announcements
        - ✅ Jira tasks
        """)
    
    # Main form
    st.header("Start New Employee Onboarding")
    
    with st.form("onboarding_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            employee_name = st.text_input(
                "Employee Name *",
                value=st.session_state.get("employee_name", ""),
                placeholder="John Doe"
            )
            email = st.text_input(
                "Email Address *",
                value=st.session_state.get("email", ""),
                placeholder="john.doe@company.com"
            )
            department = st.selectbox(
                "Department *",
                options=[""] + DEPARTMENTS,
                index=0 if not st.session_state.get("department") else DEPARTMENTS.index(st.session_state.get("department", "")) + 1
            )
        
        with col2:
            position = st.text_input(
                "Position",
                value=st.session_state.get("position", ""),
                placeholder="Software Engineer"
            )
            start_date = st.date_input(
                "Start Date *",
                value=datetime.strptime(st.session_state.get("start_date", datetime.now().strftime("%Y-%m-%d")), "%Y-%m-%d").date() if st.session_state.get("start_date") else datetime.now().date(),
                min_value=datetime.now().date()
            )
            manager = st.text_input(
                "Manager",
                value=st.session_state.get("manager", ""),
                placeholder="Jane Smith"
            )
        
        submitted = st.form_submit_button("🚀 Start Onboarding", use_container_width=True)
    
    # Handle form submission
    if submitted:
        # Validation
        if not all([employee_name, email, department, start_date]):
            st.error("❌ Please fill in all required fields (marked with *)")
        else:
            # Prepare data
            data = {
                "employee_name": employee_name,
                "email": email,
                "department": department,
                "start_date": start_date.strftime("%Y-%m-%d"),
                "manager": manager or "TBD",
                "position": position or "Team Member"
            }
            
            # Show progress
            with st.spinner("🔄 Starting onboarding workflow..."):
                try:
                    response = requests.post(
                        f"{API_BASE_URL}/api/onboard",
                        json=data,
                        timeout=30
                    )
                    
                    if response.status_code == 200:
                        result = response.json()
                        
                        if result.get("status") == "success":
                            st.success("✅ " + result.get("summary", "Onboarding workflow completed!"))
                            
                            # Show actions completed
                            if result.get("actions_completed"):
                                st.markdown("### 📋 Actions Completed:")
                                for action in result.get("actions_completed", []):
                                    st.markdown(f"✅ {action}")
                            
                            # Show workflow ID
                            if result.get("workflow_id"):
                                st.info(f"🆔 Workflow ID: `{result.get('workflow_id')}`")
                        else:
                            st.error("❌ " + result.get("message", "Workflow execution failed"))
                    else:
                        error_data = response.json() if response.content else {}
                        st.error("❌ " + error_data.get("message", f"Error: {response.status_code}"))
                        
                except requests.exceptions.RequestException as e:
                    st.error(f"❌ Connection error: {str(e)}")
                    st.info("💡 Make sure the backend is running on " + API_BASE_URL)
    
    # Info section
    st.markdown("---")
    st.markdown("### 📖 How It Works")
    st.markdown("""
    1. Fill in the new employee details above
    2. Click "Start Onboarding" to trigger the workflow
    3. IBM watsonx Orchestrate automatically:
       - Sends welcome emails via Gmail
       - Creates calendar events for orientation
       - Generates onboarding documents
       - Posts Slack announcements
       - Creates Jira tasks
    4. Get a summary of all completed actions
    """)
    
    # Footer
    st.markdown("---")
    st.markdown("**Built with ❤️ using IBM watsonx Orchestrate**")

if __name__ == "__main__":
    main()

