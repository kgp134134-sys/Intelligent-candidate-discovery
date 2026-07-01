# Intelligent Candidate Discovery

This project is my solution for the Redrob AI Intelligent Candidate Discovery Challenge.

## Goal

The goal is to rank candidates for the Senior AI Engineer role using candidate profile data, skills, experience, and Redrob behavioral signals.

## Files

- `main.py` - Python code for candidate ranking
- `sample_candidates.json` - Sample candidate data
- `ranked_candidates.csv` - Ranked candidate output
- `ranked_candidates.xlsx` - Ranked candidate output in Excel format
- `requirements.txt` - Required Python libraries

## Ranking Logic

The ranking score is based on:

1. Matching AI/ML skills
2. Years of experience
3. GitHub activity score
4. Open-to-work signal

Important skills used for matching include:

- Python
- Machine Learning
- NLP
- LLM
- Fine-tuning LLMs
- Embeddings
- Vector Databases
- FAISS
- Pinecone
- Milvus
- RAG
- Data Pipelines
- Kafka
- Spark
- AWS
- GCP

## How to Run

Install requirements:

```bash
pip install -r requirements.txt