import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def generate_resume(full_name, contact, education, experience, skills):
    model = genai.GenerativeModel("gemini-1.5-pro")

    prompt = f"""
    Create a complete, professional resume in markdown format for the following details:

    Full Name: {full_name}
    Contact: {contact}
    Education: {education}
    Years of Experience: {experience}
    Skills: {skills}

    Include:
    - A short, impactful professional summary at the top
    - Detailed education section
    - Detailed experience section with company names, positions, and quantified achievements
    - Skills section (formatted cleanly)
    - Optional Projects section based on skills
    - Clean markdown formatting

    Do NOT include placeholders like [Company Name] or [University Name].
    """

    response = model.generate_content(prompt)
    return response.text
