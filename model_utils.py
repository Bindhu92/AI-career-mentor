# model_utils.py
from sentence_transformers import SentenceTransformer
import json
import numpy as np

embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Dummy career DB (you can expand this or load from JSON)
career_db = [
    {
        "title": "Data Scientist",
        "summary": "Good fit for analytical and coding skills.",
        "roadmap": "1. Learn Python\n2. Study statistics\n3. Build ML projects\n4. Get internships",
        "salary": 120000
    },
    {
        "title": "UI/UX Designer",
        "summary": "Ideal for creative and design-focused interests.",
        "roadmap": "1. Learn design tools (Figma)\n2. Study UX principles\n3. Build a portfolio",
        "salary": 85000
    },
    {
        "title": "AI Researcher",
        "summary": "Great for theoretical interests and long-term innovation.",
        "roadmap": "1. Study ML theory\n2. Learn PyTorch\n3. Read papers\n4. Contribute to research",
        "salary": 140000
    }
]

def get_career_recommendations(interests, skills, goals):
    query = f"{interests} {skills} {goals}"
    query_vec = embedder.encode(query)

    similarities = []
    for career in career_db:
        desc = f"{career['title']} {career['summary']} {career['roadmap']}"
        career_vec = embedder.encode(desc)
        sim = np.dot(query_vec, career_vec)
        similarities.append((sim, career))

    similarities.sort(reverse=True)
    return [item[1] for item in similarities[:3]]
