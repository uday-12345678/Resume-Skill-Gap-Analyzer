from learning_roadmap import LEARNING_RESOURCES

def generate_roadmap(missing_skills):
    roadmap = []
    week = 1

    for skill in missing_skills:
        description = LEARNING_RESOURCES.get(
            skill, 
            "Learn fundamentals and practice projects related to this skill"
        )
        roadmap.append({
            "week": f"Week {week}",
            "skill": skill,
            "description": description
        })
        week += 1

    return roadmap
