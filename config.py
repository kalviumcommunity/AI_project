import os
import google.generativeai as genai
GEMINI_API_KEY = "AIzaSyCyAfOLNNJ--x1R8FvFQyUrqbsTE-aGLQY"

# Load API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Gemini API key not found. Set it as GEMINI_API_KEY environment variable.")

# Configure Gemini
genai.configure(api_key=api_key)

# Function to get Gemini model
def get_model():
    return genai.GenerativeModel("gemini-1.5-flash")
