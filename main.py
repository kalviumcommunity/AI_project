import os
from dotenv import load_dotenv
from job_application import generate_job_application
from resume_generator import generate_resume
from job_search import search_jobs

# Load environment variables
load_dotenv()

while True:
    print("\n=== AI Job Assistant ===")
    print("1. Search for jobs")
    print("2. Generate Job Application")
    print("3. Generate Resume")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        role = input("Enter desired role: ")
        years = input("Years of experience: ")
        state = input("Preferred state: ")
        print("\n=== Job Search Results ===")
        for job in search_jobs(role, years, state):
            print(f"- {job['title']} at {job['company']} ({job['location']})")


    elif choice == "2":
        role = input("Enter job role: ")
        years = input("Years of experience: ")
        location = input("Preferred job location: ")
        features = input("Special features or skills: ")
        print("\n=== Generated Job Application ===")
        print(generate_job_application(role, years, location, features))

    elif choice == "3":
        name = input("Full Name: ")
        contact = input("Contact Info (phone/email): ")
        education = input("Education: ")
        experience = input("Experience: ")
        skills = input("Skills (comma separated): ")
        print("\n=== Generated Resume ===\n")
        print(generate_resume(name, contact, education, experience, skills))

    elif choice == "4":
        print("Thank you")
        break

    else:
        print("Invalid choice, please try again.")
