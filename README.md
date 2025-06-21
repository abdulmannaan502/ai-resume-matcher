# 🔍 AI Resume Screening & Job Matcher

AI-powered app to automate resume screening by matching resumes against job descriptions using semantic similarity with BERT.

## 🚀 Features
- Upload multiple resumes (PDF)
- Paste a job description
- Uses Sentence-BERT for semantic embeddings
- Cosine similarity ranking
- Highlights matched skills
- Downloadable report (CSV)

## 🧠 Tech Stack
- Python
- Streamlit
- SentenceTransformers (BERT)
- PyMuPDF
- Scikit-learn

## 📦 Setup

```bash
git clone https://github.com/abdulmannaan502/ai-resume-matcher
cd ai-resume-matcher
pip install -r requirements.txt
streamlit run app.py
