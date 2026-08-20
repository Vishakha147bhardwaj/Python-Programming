from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load a lightweight, smart AI model
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Define three sentences to compare
sentences = [
    "How to fix a flat tire on a bicycle",
    "Steps for repairing a punctured bike wheel",
    "The weather forecast predicts heavy rain tomorrow"
]

# 3. Convert sentences into mathematical coordinates (Embeddings)
embeddings = model.encode(sentences)

# 4. Calculate similarity between our sentences
# Compare Sentence 0 with Sentence 1
sim_1_2 = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]

# Compare Sentence 0 with Sentence 2
sim_1_3 = cosine_similarity([embeddings[0]], [embeddings[2]])[0][0]

print(f"Similarity (Tire Fix vs Bike Repair): {sim_1_2:.4f}")
print(f"Similarity (Tire Fix vs Weather Forecast): {sim_1_3:.4f}")
