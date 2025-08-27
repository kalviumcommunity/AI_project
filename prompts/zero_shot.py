import google.generativeai as genai
import json
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def clean_json_response(text: str) -> str:
    """
    Remove markdown fences like ```json ... ```
    """
    cleaned = text.strip()
    if cleaned.startswith("```"):
        parts = cleaned.split("```")
        if len(parts) >= 2:
            cleaned = parts[1].strip()
    if cleaned.lower().startswith("json"):
        cleaned = cleaned[4:].strip()
    return cleaned

def generate_zero_shot_questions(role, years, location):
    prompt = f"""
    You are an AI interview assistant.
    Generate 5 technical interview questions for a {role} with {years} years of experience in {location}.
    Return the response strictly in JSON format as:
    {{
      "questions": [
        "question 1",
        "question 2",
        "question 3",
        "question 4",
        "question 5"
      ]
    }}
    """
    response = model.generate_content(prompt)

    text_response = response.text

    try:
        cleaned = clean_json_response(text_response)
        data = json.loads(cleaned)
        return data.get("questions", [])
    except Exception as e:
        return [f"Parsing error: {e}. Raw response: {text_response}"]
