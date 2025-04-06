import re

# Grouped Skill Categories
SKILL_CATEGORIES = {
    "Programming Languages": [
        "python", "c++", "c", "java", "javascript", "typescript", "sql"
    ],
    "Web Development": [
        "html", "css", "react", "angular", "vue", "node.js", "express.js", "bootstrap", "tailwind", "rest api"
    ],
    "Backend & Databases": [
        "mongodb", "mysql", "postgresql", "firebase", "redis", "express.js", "flask", "django"
    ],
    "Tools & Platforms": [
        "git", "github", "docker", "aws", "azure", "gcp", "netlify", "vercel", "heroku", "linux"
    ],
    "AI/ML & Data Analytics": [
        "machine learning", "deep learning", "nlp", "pandas", "numpy", "matplotlib",
        "tensorflow", "keras", "pytorch", "scikit-learn", "data visualization", "power bi", "excel", "streamlit"
    ],
    "CS Fundamentals": [
        "data structures", "algorithms", "object-oriented programming", "operating systems", "computer networks", "dbms", "system design"
    ],
    "Soft Skills": [
        "communication", "teamwork", "problem solving", "leadership", "critical thinking", "adaptability"
    ]
}

# Extract skills
def extract_skills(resume_text):
    resume_text = resume_text.lower()
    found_skills = {}

    for category, skills in SKILL_CATEGORIES.items():
        matched = []
        for skill in skills:
            if re.search(rf"\b{re.escape(skill)}\b", resume_text):
                matched.append(skill)
        if matched:
            found_skills[category] = matched

    return found_skills
