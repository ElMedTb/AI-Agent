"""
Sample data generator for testing the onboarding assistant
"""

import random
from datetime import datetime, timedelta
from typing import Dict, Any


# Sample data pools
EMPLOYEE_NAMES = [
    "John Doe", "Jane Smith", "Michael Johnson", "Emily Davis",
    "David Wilson", "Sarah Brown", "Robert Taylor", "Jessica Martinez",
    "William Anderson", "Amanda Thomas", "James Jackson", "Lisa White"
]

DEPARTMENTS = [
    "Engineering", "Marketing", "Sales", "HR", "Finance",
    "Operations", "Product", "Design", "Customer Success"
]

POSITIONS = {
    "Engineering": ["Software Engineer", "Senior Software Engineer", "DevOps Engineer", "QA Engineer"],
    "Marketing": ["Marketing Manager", "Content Specialist", "SEO Analyst", "Brand Manager"],
    "Sales": ["Sales Representative", "Account Executive", "Sales Manager", "Business Development"],
    "HR": ["HR Coordinator", "Talent Acquisition", "HR Business Partner", "People Operations"],
    "Finance": ["Financial Analyst", "Accountant", "Finance Manager", "Controller"],
    "Operations": ["Operations Manager", "Operations Analyst", "Process Manager", "Operations Coordinator"],
    "Product": ["Product Manager", "Product Owner", "Product Analyst", "Product Designer"],
    "Design": ["UX Designer", "UI Designer", "Graphic Designer", "Design Lead"],
    "Customer Success": ["Customer Success Manager", "Support Specialist", "Customer Success Lead"]
}

MANAGERS = [
    "Alice Johnson", "Bob Williams", "Carol Davis", "Daniel Miller",
    "Eva Garcia", "Frank Rodriguez", "Grace Lee", "Henry Martinez"
]


def generate_sample_employee_data() -> Dict[str, Any]:
    """
    Generate random sample employee data for testing
    
    Returns:
        Dictionary with employee onboarding data
    """
    name = random.choice(EMPLOYEE_NAMES)
    department = random.choice(DEPARTMENTS)
    position = random.choice(POSITIONS.get(department, ["Team Member"]))
    manager = random.choice(MANAGERS)
    
    # Generate start date (between 1 week and 1 month from now)
    start_date = (datetime.now() + timedelta(days=random.randint(7, 30))).strftime("%Y-%m-%d")
    
    # Generate email from name
    first_name, last_name = name.lower().split()
    email = f"{first_name}.{last_name}@company.com"
    
    return {
        "employee_name": name,
        "email": email,
        "department": department,
        "start_date": start_date,
        "manager": manager,
        "position": position
    }


def generate_multiple_samples(count: int = 5) -> list:
    """
    Generate multiple sample employee records
    
    Args:
        count: Number of samples to generate
        
    Returns:
        List of employee data dictionaries
    """
    return [generate_sample_employee_data() for _ in range(count)]


