import streamlit as st
from backend.parser import extract_text_from_pdf
from backend.utils import clean_text
from backend.scorer import load_skills, extract_keywords_from_jd, extract_skills
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

st.set_page_config(page_title="AI Resume Matcher", layout="wide")
st.title("📄 AI Resume Screening & Job Matcher")

# Inputs
uploaded_files = st.file_uploader("Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)
job_description = st.text_area("Paste Job Description")

if st.button("🔍 Match Candidates"):
    if not uploaded_files or not job_description:
        st.warning("Please upload at least one resume and enter a job description.")
    else:
        jd_clean = clean_text(job_description)
        all_skills = load_skills()
        skill_keywords = extract_keywords_from_jd(job_description, all_skills)
        st.markdown(f"✅ **Extracted Skills from JD ({len(skill_keywords)}):** `{', '.join(skill_keywords)}`")

        resume_texts = []
        candidate_names = []

        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            resume_texts.append(clean_text(text))
            candidate_names.append(file.name)

        model = SentenceTransformer('all-MiniLM-L6-v2')
        jd_embedding = model.encode(jd_clean)
        resume_embeddings = [model.encode(text) for text in resume_texts]
        scores = cosine_similarity([jd_embedding], resume_embeddings)[0]

        results = []
        for i, score in enumerate(scores):
            matched = extract_skills(resume_texts[i], skill_keywords)
            results.append({
                "Candidate": candidate_names[i],
                "Match Score": round(score, 2),
                "Skills Matched": ", ".join([f"🟢 **{s}**" for s in matched])
            })

        df = pd.DataFrame(sorted(results, key=lambda x: x["Match Score"], reverse=True))
        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download CSV Report", csv, file_name="resume_rankings.csv", mime="text/csv")
