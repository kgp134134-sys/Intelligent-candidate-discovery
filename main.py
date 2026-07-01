import json
import pandas as pd

print("=== Intelligent Candidate Discovery ===")

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

print(f"Total Sample Candidates: {len(candidates)}")

required_skills = [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "LLM",
    "Fine-tuning LLMs",
    "Embeddings",
    "Vector Databases",
    "Milvus",
    "Pinecone",
    "FAISS",
    "RAG",
    "Search",
    "Ranking",
    "Recommendation Systems",
    "Data Pipelines",
    "Spark",
    "Kafka",
    "MLOps",
    "AWS",
    "GCP",
]

rows = []

for candidate in candidates:
    profile = candidate.get("profile", {})
    signals = candidate.get("redrob_signals", {})

    skills = candidate.get("skills", [])
    skill_names = [skill.get("name", "") for skill in skills]
    skill_names_lower = [name.lower() for name in skill_names]

    matched_skills = []
    skill_score = 0

    for required_skill in required_skills:
        if required_skill.lower() in skill_names_lower:
            matched_skills.append(required_skill)
            skill_score += 5

    experience = profile.get("years_of_experience", 0)
    experience_score = min(experience * 3, 30)

    github_score = signals.get("github_activity_score", 0)
    if github_score == -1:
        github_score = 0
    github_score = min(github_score, 20)

    open_to_work_score = 10 if signals.get("open_to_work_flag", False) else 0

    final_score = skill_score + experience_score + github_score + open_to_work_score

    rows.append({
        "candidate_id": candidate.get("candidate_id", ""),
        "name": profile.get("anonymized_name", ""),
        "headline": profile.get("headline", ""),
        "location": profile.get("location", ""),
        "country": profile.get("country", ""),
        "years_of_experience": experience,
        "current_title": profile.get("current_title", ""),
        "current_company": profile.get("current_company", ""),
        "matched_skills": ", ".join(matched_skills),
        "all_skills": ", ".join(skill_names),
        "ranking_score": round(final_score, 2),
    })

df = pd.DataFrame(rows)
df = df.sort_values(by="ranking_score", ascending=False)

df.to_csv("ranked_candidates.csv", index=False)
df.to_excel("ranked_candidates.xlsx", index=False)

print("Created ranked_candidates.csv")
print("Created ranked_candidates.xlsx")
print("\nTop 5 Candidates:")
print(df[["candidate_id", "name", "ranking_score", "matched_skills"]].head())