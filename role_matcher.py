# role_matcher.py

def calculate_role_fit(skills):
    # Define expected skills for each role
    role_requirements = {
    "AI Engineer": {
        "AI/ML & Data Analytics": ["python", "pandas", "numpy", "matplotlib", "scikit-learn", "tensorflow", "pytorch", "machine learning", "deep learning", "nlp"]
    },
    "Analytics Engineer": {
        "AI/ML & Data Analytics": ["sql", "python", "power bi", "excel", "data visualization"],
        "Backend & Databases": ["mysql", "postgresql"]
    },
    "Software Engineer": {
        "Programming Languages": ["c++", "java", "python"],
        "Tools & Platforms": ["git"],
        "CS Fundamentals": ["object-oriented programming", "data structures", "algorithms", "system design"]
    },
    "Full Stack Developer": {
        "Web Development": ["html", "css", "javascript", "react", "node.js"],
        "Backend & Databases": ["mongodb", "express.js"],
        "Tools & Platforms": ["git"]
    }
}

    role_scores = {}

    for role, requirements in role_requirements.items():
        matched = []
        total = 0

        for category, required_skills in requirements.items():
            if category in skills:
                total += len(required_skills)
                for skill in required_skills:
                    if skill.lower() in [s.lower() for s in skills[category]]:
                        matched.append(skill)

        score = int((len(matched) / total) * 100) if total > 0 else 0

        role_scores[role] = {
            "score": score,
            "matched_skills": matched
        }

    return role_scores
