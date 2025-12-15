import re

# Canonical skill → possible variations
SKILL_ALIASES = {
    "java": ["java", "core java", "java se", "java ee", "jdk"],
    "python": ["python", "python3", "python programming"],
    "c++": ["c++", "cpp"],
    "data structures": ["data structures", "ds", "dsa"],
    "algorithms": ["algorithms", "algo"],
    "sql": ["sql", "mysql", "postgresql", "oracle sql"],
    "excel": ["excel", "ms excel", "microsoft excel"],
    "power bi": ["power bi", "powerbi"],
    "tableau": ["tableau"],
    "html": ["html", "html5"],
    "css": ["css", "css3"],
    "javascript": ["javascript", "js"],
    "react": ["react", "reactjs"],
    "node": ["node", "nodejs"],
    "mongodb": ["mongodb", "mongo db"],
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning", "dl"],
    "statistics": ["statistics", "statistical analysis"],
    "data analysis": ["data analysis", "data analytics"],
    "git": ["git", "git version control"]
}

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            # word boundary avoids partial matches
            if re.search(r"\b" + re.escape(alias) + r"\b", text):
                found_skills.append(skill)
                break

    return list(set(found_skills))
