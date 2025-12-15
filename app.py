from flask import Flask, render_template, request
import os

from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from job_roles import JOB_ROLES
from analyzer import analyze_skills
from roadmap_generator import generate_roadmap
from project_recommender import recommend_projects

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

# Ensure uploads folder exists
if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    selected_role = None

    if request.method == "POST":
        file = request.files.get("resume")
        role = request.form.get("role")
        selected_role = role

        if file and role:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)

            resume_text = extract_text_from_pdf(file_path)
            resume_skills = extract_skills(resume_text)

            role_skills = JOB_ROLES.get(role, [])
            analysis = analyze_skills(resume_skills, role_skills)

            # Learning roadmap
            roadmap = generate_roadmap(analysis["missing_skills"])
            analysis["roadmap"] = roadmap

            # Project recommendations (only if match < 50%)
            analysis["projects"] = recommend_projects(
                analysis["missing_skills"],
                analysis["match_percentage"],
                max_projects=3
            )

            analysis["role"] = role
            analysis["filename"] = file.filename

            result = analysis

    return render_template(
        "index.html",
        result=result,
        roles=JOB_ROLES.keys(),
        selected_role=selected_role
    )

if __name__ == "__main__":
    app.run(debug=True)
