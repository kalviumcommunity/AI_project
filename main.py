from job_application import generate_job_application
from resume_generator import generate_resume
from job_search import search_jobs

while True:
    print("\n=== AI Job Assistant ===")
    print("1. Generate Job Application")
    print("2. Create Resume")
    print("3. Search for Jobs")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        role = input("Enter job role: ")
        exp = input("Enter years of experience: ")
        loc = input("Enter your location (state): ")
        skills = input("Enter your main skill/feature: ")
        cname, ccity, letter = generate_job_application(role, exp, loc, skills)
        print(f"\nCompany: {cname} ({ccity})\n")
        print(letter)

    elif choice == "2":
        name = input("Full Name: ")
        contact = input("Contact Info (phone/email): ")
        edu = input("Education: ")
        exp = input("Experience: ")
        skills = input("Skills (comma separated): ")
        resume = generate_resume(name, contact, edu, exp, skills)
        print("\n=== Generated Resume ===\n")
        print(resume)

    elif choice == "3":
        role = input("Enter job role: ")
        loc = input("Enter location: ")
        jobs = search_jobs(role, loc)
        print("\n=== Job Listings ===")
        for job in jobs:
            print(f"- {job['title']} at {job['company']} ({job['location']})")

    elif choice == "4":
        break
    else:
        print("Invalid choice, try again.")
