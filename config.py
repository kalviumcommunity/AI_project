import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

if not GEMINI_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing in .env")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
