import google.generativeai as genai
import json
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def clean_json_response(text: str) -> str:
    """
    Clean Gemini's response by removing ```json ... ``` wrappers.
    """
    cleaned = text.strip()
    if cleaned.startswith("```"):
        parts = cleaned.split("```")
        if len(parts) >= 2:
            cleaned = parts[1].strip()
    if cleaned.lower().startswith("json"):
        cleaned = cleaned[4:].strip()
    return cleaned

def generate_one_shot_questions(role, experience, location):
    example = {
        "role": "backend developer",
        "experience": 3,
        "location": "chennai",
        "questions": [
            "Explain how you have used Node.js with Express to build scalable APIs in your projects.",
            "Describe a database optimization challenge you faced while working with MongoDB or SQL.",
            "How do you ensure security (like authentication/authorization) in backend systems?"
        ]
    }

    prompt = f"""
You are an AI Interview Question Generator.
Below is one example of how interview questions are structured for a role.

Example:
Role: {example['role']}
Experience: {example['experience']} years
Location: {example['location']}
Questions:
{chr(10).join(['- ' + q for q in example['questions']])}

Now, based on this example, generate **5 interview questions** for:
Role: {role}
Experience: {experience} years
Location: {location}

Return output strictly in JSON format:
{{
  "questions": ["question1", "question2", "question3", "question4", "question5"]
}}
"""

    response = model.generate_content(prompt)
    text_response = response.text

    try:
        cleaned = clean_json_response(text_response)
        data = json.loads(cleaned)
        return data.get("questions", [])
    except Exception as e:
        return [f"Parsing error: {e}", f"Raw response: {text_response}"]
