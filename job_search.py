import json
from config import MODEL_NAME
import google.generativeai as genai

def search_jobs(role, years, state):
    prompt = f"""
    Generate exactly 5 job postings for a {role} with {years} years of experience in {state}.
    Respond ONLY with a JSON array in this format:
    [
      {{ "title": "Job Title", "company": "Company Name", "location": "City, State" }},
      ...
    ]
    No extra text, no markdown, no code block.
    """

    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(
        prompt,
        generation_config={"response_mime_type": "application/json"}  # Forces JSON
    )

    try:
        jobs = json.loads(response.text)
    except json.JSONDecodeError:
        jobs = [{"title": "Error parsing jobs", "company": "", "location": ""}]

    return jobs
