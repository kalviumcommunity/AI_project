import json
from config import MODEL_NAME
import google.generativeai as genai

def generate_interview_questions(role: str, years: str, location: str):
    prompt = f"""
You are an interview coach.

Task: Generate exactly 5 concise, role-specific interview questions for a {role}
with {years} years of experience in {location}.

Return ONLY a JSON array of strings. No markdown, no keys, no commentary.
Example of the shape only (do not include this example in the output):
[
  "Question 1?",
  "Question 2?",
  "Question 3?",
  "Question 4?",
  "Question 5?"
]
"""
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(
        prompt,
        generation_config={"response_mime_type": "application/json"}  
    )

    try:
        items = json.loads(response.text)
        if not isinstance(items, list):
            raise ValueError("Output not a list")
       
        return [str(q).strip() for q in items][:5]
    except Exception:
        return ["Failed to parse model output. Please try again."]
