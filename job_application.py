from config import MODEL_NAME
import google.generativeai as genai

def generate_job_application(role, years, location, features):
    prompt = f"""
    Generate a formal job application letter for the role of {role}
    with {years} years of experience, applying for jobs in {location}.
    Highlight the following skills/features: {features}.
    Also, automatically find and include a realistic company name and city in that location.
    """
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(prompt)
    return response.text
