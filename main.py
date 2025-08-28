import os
from dotenv import load_dotenv
from job_application import generate_job_application
from resume_generator import generate_resume
from job_search import search_jobs
from prompts.zero_shot import generate_zero_shot_questions  
from prompts.one_shot import generate_one_shot_questions
from prompts.multi_shot import generate_multi_shot_questions
from prompts.chain_of_thought import generate_chain_of_thought_answer

load_dotenv()

def main():
    while True:
        print("\n=== AI Job Assistant ===")
        print("1. Search for jobs")
        print("2. Generate Job Application")
        print("3. Generate Resume")
        print("4. Generate Interview Questions (Zero-Shot)") 
        print("5. Generate Interview Questions (One-Shot)")
        print("6. Generate Interview Questions (Multi-Shot)") 
        print("7. Solve Reasoning Question (Chain-of-Thought)")
        print("8. Exit")


        choice = input("Choose an option: ").strip()

        if choice == "1":
            role = input("Enter desired role: ").strip()
            years = input("Years of experience: ").strip()
            state = input("Preferred state: ").strip()
            print("\n=== Job Search Results ===")
            jobs = search_jobs(role, years, state)
            if jobs:
                for job in jobs:
                    print(f"- {job.get('title', 'N/A')} at {job.get('company', 'N/A')} ({job.get('location', 'N/A')})")
            else:
                print("⚠️ No jobs found.")

        elif choice == "2":
            role = input("Enter job role: ").strip()
            years = input("Years of experience: ").strip()
            location = input("Preferred job location: ").strip()
            features = input("Special features or skills: ").strip()
            print("\n=== Generated Job Application ===")
            print(generate_job_application(role, years, location, features))

        elif choice == "3":
            name = input("Full Name: ").strip()
            contact = input("Contact Info (phone/email): ").strip()
            education = input("Education: ").strip()
            experience = input("Experience: ").strip()
            skills = input("Skills (comma separated): ").strip()
            print("\n=== Generated Resume ===\n")
            print(generate_resume(name, contact, education, experience, skills))

        elif choice == "4":
            role = input("Role for interview prep: ").strip()
            years = input("Years of experience: ").strip()
            location = input("Location: ").strip()
            print("\n=== Zero-Shot Interview Questions ===")
            qs = generate_zero_shot_questions(role, years, location) 
            if qs and isinstance(qs, list):
                for i, q in enumerate(qs, 1):
                    print(f"{i}. {q}")
            else:
                print("⚠️ No questions generated. Check your `zero_shot.py` implementation.")

        elif choice == "5":
            role = input("Role for interview prep: ").strip()
            experience = input("Years of experience: ").strip()
            location = input("Location: ").strip()
            qs = generate_one_shot_questions(role, experience, location)
            print("\n=== One-Shot Interview Questions ===")
            if qs and isinstance(qs, list):
                for i, q in enumerate(qs, 1):
                    print(f"{i}. {q}")
            else:
                print("⚠️ No questions generated. Check your `one_shot.py` implementation.") 

        elif choice == "6":
            role = input("Role for interview prep: ").strip()
            experience = input("Years of experience: ").strip()
            location = input("Location: ").strip()
            qs = generate_multi_shot_questions(role, experience, location)  # ✅ call multi-shot
            print("\n=== Multi-Shot Interview Questions ===")
            if qs and isinstance(qs, list):
                for i, q in enumerate(qs, 1):
                    print(f"{i}. {q}")
            else:
                print("⚠️ No questions generated. Check your `multi_shot.py` implementation.")
        elif choice == "7":
            question = input("Enter your reasoning question: ").strip()
            temp = float(input("Enter temperature (0.0 - 1.0): ").strip()) 
            print("\n=== Chain-of-Thought Answer ===")
            answer = generate_chain_of_thought_answer(question, temp) 
            print(answer)


        elif choice == "8":
            print("✅ Thank you for using AI Job Assistant!")
            break

        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
