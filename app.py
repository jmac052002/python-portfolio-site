from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "name": "Serverless TODO API",
        "desc": "AWS SAM, Lambda, API Gateway, DynamoDB, S3 static hosting.",
        "link": "https://github.com/jmac052002/sam-tiny-api"
    },
    {
        "name": "Terraform 3-Tier App",
        "desc": "VPC, ALB, ASG, RDS — infra-as-code to show SA/DevOps skills.",
        "link": "https://github.com/jmac052002"
    },
    {
        "name": "Automation Scripts (Python)",
        "desc": "Small CLI tools to organize files and demo Python fundamentals.",
        "link": "https://github.com/jmac052002"
    },
]

SKILLS = [
    "AWS (Lambda, API Gateway, DynamoDB, S3, CloudFront)",
    "Terraform / IaC",
    "Docker / k3d / Kubernetes basics",
    "Python (automation, FastAPI/Flask)",
    "GitHub Actions / CI/CD",
]

@app.route("/")
def home():
    return render_template("index.html", projects=PROJECTS, skills=SKILLS)

@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    # in WSL this is fine
    app.run(debug=True)
