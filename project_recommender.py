PROJECT_BASED_LEARNING = {

    # ---------------- Programming ----------------
    "python": {
        "project": "Student Management System using Python",
        "reference": "Practice Python basics, file handling, OOP, and modules"
    },

    "java": {
        "project": "Library Management System using Java",
        "reference": "Learn OOP, collections, exception handling, and JDBC"
    },

    "c++": {
        "project": "Banking System using C++",
        "reference": "Practice STL, pointers, OOP, and memory management"
    },

    "data structures": {
        "project": "Implementation of Data Structures in C++/Java",
        "reference": "Implement arrays, stacks, queues, trees, and graphs"
    },

    "algorithms": {
        "project": "Algorithm Visualizer Application",
        "reference": "Practice sorting, searching, recursion, and DP"
    },

    # ---------------- Data & Analytics ----------------
    "sql": {
        "project": "Employee Database Management System using SQL",
        "reference": "Practice joins, subqueries, indexing, and aggregations"
    },

    "excel": {
        "project": "Sales Performance Dashboard using Excel",
        "reference": "Learn pivot tables, formulas, charts, and dashboards"
    },

    "power bi": {
        "project": "Interactive Business Intelligence Dashboard",
        "reference": "Learn DAX, reports, and data modeling"
    },

    "tableau": {
        "project": "Customer Insights Dashboard using Tableau",
        "reference": "Apply visualization best practices and storytelling"
    },

    "data analysis": {
        "project": "Exploratory Data Analysis on Real-World Dataset",
        "reference": "Practice data cleaning, EDA, and visualization"
    },

    "statistics": {
        "project": "Statistical Analysis of Business Data",
        "reference": "Apply probability, hypothesis testing, and distributions"
    },

    # ---------------- Web Development ----------------
    "html": {
        "project": "Personal Portfolio Website",
        "reference": "Learn semantic HTML and accessibility"
    },

    "css": {
        "project": "Responsive Website Design",
        "reference": "Practice Flexbox, Grid, and responsive layouts"
    },

    "javascript": {
        "project": "Interactive Form Validation System",
        "reference": "Practice DOM manipulation and events"
    },

    "react": {
        "project": "Task Management Web Application",
        "reference": "Learn components, state, props, and hooks"
    },

    "node": {
        "project": "REST API for User Management",
        "reference": "Learn Express, middleware, and routing"
    },

    "mongodb": {
        "project": "CRUD Application using MongoDB",
        "reference": "Practice schema design and database operations"
    },

    "api": {
        "project": "API Integration Project",
        "reference": "Consume and integrate REST APIs"
    },

    # ---------------- Machine Learning & AI ----------------
    "machine learning": {
        "project": "House Price Prediction System",
        "reference": "Learn regression, feature engineering, and evaluation"
    },

    "deep learning": {
        "project": "Image Classification using CNN",
        "reference": "Learn neural networks, CNNs, and backpropagation"
    },

    "tensorflow": {
        "project": "Deep Learning Model using TensorFlow",
        "reference": "Build and train neural networks using TensorFlow"
    },

    "pytorch": {
        "project": "Neural Network Implementation using PyTorch",
        "reference": "Learn tensors, autograd, and training loops"
    },

    # ---------------- DevOps & Cloud ----------------
    "linux": {
        "project": "Linux System Monitoring Tool",
        "reference": "Practice Linux commands, scripting, and processes"
    },

    "docker": {
        "project": "Dockerized Web Application",
        "reference": "Learn Dockerfiles, images, and containers"
    },

    "aws": {
        "project": "Deploy Web Application on AWS",
        "reference": "Learn EC2, S3, IAM, and deployment basics"
    },

    "cloud computing": {
        "project": "Cloud-Based File Storage System",
        "reference": "Understand cloud architecture and scalability"
    },

    # ---------------- Security & Testing ----------------
    "network security": {
        "project": "Network Vulnerability Analysis Tool",
        "reference": "Learn basic network security and threat analysis"
    },

    "ethical hacking": {
        "project": "Web Application Security Assessment",
        "reference": "Practice penetration testing fundamentals"
    },

    "manual testing": {
        "project": "Test Case Management System",
        "reference": "Learn SDLC, STLC, and test case design"
    },

    "automation testing": {
        "project": "Automated Web Testing using Selenium",
        "reference": "Practice automation frameworks and scripts"
    },

    # ---------------- Mobile ----------------
    "android": {
        "project": "Android Notes Application",
        "reference": "Learn activities, intents, and UI components"
    },

    "flutter": {
        "project": "Cross-Platform Mobile App using Flutter",
        "reference": "Practice widgets, layouts, and navigation"
    },

    # ---------------- UI / UX ----------------
    "ui/ux": {
        "project": "Mobile App UI Redesign Case Study",
        "reference": "Learn wireframing, prototyping, and usability testing"
    }
}


def recommend_projects(missing_skills, match_percentage, max_projects=3):
    """
    Recommend one project per missing skill (up to max_projects)
    Only if match percentage is below 50
    """
    if match_percentage >= 50:
        return []

    recommendations = []

    for skill in missing_skills:
        if skill in PROJECT_BASED_LEARNING:
            recommendations.append({
                "skill": skill,
                "project": PROJECT_BASED_LEARNING[skill]["project"],
                "reference": PROJECT_BASED_LEARNING[skill]["reference"]
            })

        if len(recommendations) >= max_projects:
            break

    return recommendations
