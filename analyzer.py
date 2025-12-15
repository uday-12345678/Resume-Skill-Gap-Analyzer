def analyze_skills(resume_skills, role_skills):
    matched = set(resume_skills).intersection(set(role_skills))
    missing = set(role_skills) - matched

    match_percentage = (len(matched) / len(role_skills)) * 100

    return {
        "matched_skills": list(matched),
        "missing_skills": list(missing),
        "match_percentage": round(match_percentage, 2)
    }
