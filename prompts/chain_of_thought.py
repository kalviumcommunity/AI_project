import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_chain_of_thought_answer(question: str, temperature: float = 0.7):
    prompt = f"""
You are an AI that solves reasoning problems step by step.
Show your reasoning process clearly and then give the final answer.

Question: {question}

Format:
Step 1: ...
Step 2: ...
Step 3: ...
Final Answer: ...
"""
    response = model.generate_content(
        prompt,
        generation_config={"temperature": temperature} 
    )
    return response.text

