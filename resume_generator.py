from config import MODEL_NAME
import google.generativeai as genai

def generate_resume(name, contact, education, experience, skills):
    prompt = f"""
    Create a professional, complete, ready-to-use resume in Markdown format for:
    Name: {name}
    Contact: {contact}
    Education: {education}
    Experience: {experience} years
    Skills: {skills}

    Make sure the resume is fully filled with realistic job titles, companies, and bullet points.
    """
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(prompt)
    return response.text
