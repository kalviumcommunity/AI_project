# AI_project

# AI Job Application Assistant

## 📌 Overview
An AI-powered assistant that helps users find jobs, create and optimize resumes, and prepare for interviews.  
It uses **Basic Prompting**, **Function Calling**, **Structured Output**, and **RAG** to make career growth smarter and faster.

---

## 📌 How the Four Criteria Are Used

**Basic Prompting:**  
Understands user queries in plain language.  
Example: *"Find me a frontend developer job in Bangalore"*.

**Function Calling:**  
Automatically triggers APIs for job listings, or resume analysis.

**Retrieval-Augmented Generation (RAG):**  
Fetches verified interview tips, resume improvement suggestions, and industry insights from a stored knowledge base, then merges them with the AI's response.

---

## 🚀 Features

- **AI Job Application Assistant** – Guides you on company name, role details, must-know requirements, and location info.
- **AI Resume Generator** – Creates a professional, ATS-friendly resume tailored to your skills and experience.
- **AI Job Search** – Finds relevant job openings using APIs, with filters for location, role, and salary range.
- **Personalized Job Recommendations** – Matches jobs to user skills and preferences.
- **Resume Optimization** – Suggests improvements for better ATS compatibility.
- **Real-Time Job Fetching** – Integrates with job listing APIs.
- **Structured Job Listings** – Outputs clean JSON data for easy integration into websites or apps.
- **Interview Guidance** – Offers tailored tips using a curated knowledge base.

---

## 🛠 How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/AI_project.git
   cd AI_project
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment variables**  
   - Create a `.env` file in the project root.  
   - Add your API key:  
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

4. **Run the application**  
   ```bash
   python main.py
   ```

---
