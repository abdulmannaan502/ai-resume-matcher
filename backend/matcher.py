from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    return model.encode(text)

def get_similarity_scores(jd_text, resume_texts):
    jd_embedding = get_embedding(jd_text)
    resume_embeddings = [get_embedding(resume) for resume in resume_texts]
    scores = cosine_similarity([jd_embedding], resume_embeddings)[0]
    return scores
