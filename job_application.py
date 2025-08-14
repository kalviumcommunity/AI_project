import random
from config import get_model
from companies_data import COMPANIES_BY_STATE

def generate_job_application(role, experience, person_location, features):
    companies = COMPANIES_BY_STATE.get(person_location, [("Generic Tech Solutions", person_location)])
    company_name, company_city = random.choice(companies)

    prompt = f"""
    You are an expert career writer.
    Create a professional job application letter for:
    Role: {role}
    Experience: {experience} years
    Skills: {features}
    Company Name: {company_name}
    Company Location: {company_city}
    """
    model = get_model()
    response = model.generate_content(prompt)
    return company_name, company_city, response.text.strip()
