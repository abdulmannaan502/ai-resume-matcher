import re

def load_skills():
    return [
        # TECH
        "python", "java", "c", "c++", "c#", "javascript", "typescript", "sql", "nosql", "html", "css", "react", "angular",
        "vue", "node.js", "django", "flask", "spring", "express", "fastapi", "next.js", "php", "ruby", "rails", "go", "kotlin", "swift",
        # DATA / AI
        "machine learning", "deep learning", "artificial intelligence", "data science", "data analysis", "data mining",
        "data visualization", "pandas", "numpy", "matplotlib", "seaborn", "scikit-learn", "tensorflow", "keras", "pytorch",
        "hadoop", "spark", "hive", "bigquery", "airflow", "power bi", "tableau", "excel", "statistics",
        # CLOUD / DEVOPS
        "aws", "azure", "gcp", "docker", "kubernetes", "jenkins", "terraform", "ansible", "ci/cd", "linux", "bash", "cloudformation",
        # SECURITY
        "cybersecurity", "penetration testing", "network security", "ethical hacking", "siem", "owasp", "kali linux",
        # MOBILE DEV
        "android", "ios", "flutter", "react native", "xamarin",
        # DATABASES
        "mysql", "postgresql", "mongodb", "redis", "cassandra", "oracle", "sqlite",
        # PRODUCT / BIZ
        "product management", "business analysis", "requirements gathering", "stakeholder management",
        "market research", "project management", "agile methodology", "scrum", "kanban",
        # MARKETING
        "seo", "sem", "google analytics", "facebook ads", "email marketing", "copywriting", "branding",
        # DESIGN
        "figma", "adobe xd", "illustrator", "photoshop", "ui design", "ux design", "user research", "wireframing",
        # FINANCE
        "financial modeling", "budgeting", "forecasting", "quickbooks", "xero", "sap", "oracle erp",
        # HEALTHCARE
        "nursing", "emr", "clinical research", "pharmaceuticals",
        # EDUCATION
        "lesson planning", "e-learning", "curriculum design",
        # SOFT SKILLS
        "communication", "leadership", "teamwork", "problem solving", "critical thinking", "adaptability", "time management",
        "decision making", "creativity", "empathy", "collaboration", "negotiation",
        # TOOLS
        "jira", "confluence", "notion", "microsoft office", "word", "powerpoint", "slack", "asana", "monday.com", "salesforce"
    ]

def extract_keywords_from_jd(jd_text, all_skills):
    jd = jd_text.lower()
    return [skill for skill in all_skills if re.search(rf'\b{re.escape(skill)}\b', jd)]

def extract_skills(resume_text, skill_keywords):
    res = resume_text.lower()
    return [skill for skill in skill_keywords if re.search(rf'\b{re.escape(skill)}\b', res)]
