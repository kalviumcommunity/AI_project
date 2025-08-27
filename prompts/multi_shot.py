import google.generativeai as genai
import json
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def clean_json_response(text: str) -> str:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        parts = cleaned.split("```")
        if len(parts) >= 2:
            cleaned = parts[1].strip()
    if cleaned.lower().startswith("json"):
        cleaned = cleaned[4:].strip()
    return cleaned

def generate_multi_shot_questions(role, experience, location):
    examples = [
        {
            "role": "backend developer",
            "experience": 3,
            "location": "chennai",
            "questions": [
                "Explain how you have used Node.js with Express to build scalable APIs in your projects.",
                "Describe a database optimization challenge you faced while working with MongoDB or SQL.",
                "How do you ensure security (like authentication/authorization) in backend systems?"
            ]
        },
        {
            "role": "frontend developer",
            "experience": 2,
            "location": "bangalore",
            "questions": [
                "Explain how you used React hooks in building dynamic UIs.",
                "What strategies do you follow for optimizing page load performance?",
                "Describe a time you integrated REST APIs into your frontend project."
            ]
        }
    ]

    prompt = f"""
You are an AI Interview Question Generator.
Here are multiple examples:

{chr(10).join(
    [f"Example {i+1}:\nRole: {ex['role']}\nExperience: {ex['experience']} years\nLocation: {ex['location']}\nQuestions:\n" +
     "\n".join(["- " + q for q in ex['questions']]) for i, ex in enumerate(examples)]
)}

Now, based on these examples, generate **5 interview questions** for:
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

if __name__ == "__main__":
    name = input("Full Name: ").strip()
    role = input("Enter role: ").strip()
    experience = int(input("Enter years of experience: ").strip())
    location = input("Enter location: ").strip()

    print(f"\nHi {name}, here are your interview questions:\n")
    questions = generate_multi_shot_questions(role, experience, location)
    for i, q in enumerate(questions, 1):
        print(f"{i}. {q}")
