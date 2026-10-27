import numpy as np
from langchain_community.embeddings import HuggingFaceEmbeddings

# 1. Initialize our embedding encoder engine
# We use a lightweight, production-grade 384-dimensional dense transformer model
embeddings_engine = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 2. Define target text strings demonstrating conceptual variance
anchor_text = "How to fix a flat tire on a vehicle"
semantically_close = "Steps for repairing a punctured passenger car wheel"
lexically_close_but_unrelated = "Fix a flat pricing structure for marketing firms"

# 3. Generate mathematical dense vectors
vector_anchor = np.array(embeddings_engine.embed_query(anchor_text))
vector_close = np.array(embeddings_engine.embed_query(semantically_close))
vector_lexical = np.array(embeddings_engine.embed_query(lexically_close_but_unrelated))

# 4. Define a Cosine Similarity calculator formula
def calculate_cosine_similarity(vec_a, vec_b):
    dot_product = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    return dot_product / (norm_a * norm_b)

# 5. Measure conceptual proximity metrics
score_semantic = calculate_cosine_similarity(vector_anchor, vector_close)
score_lexical = calculate_cosine_similarity(vector_anchor, vector_lexical)

print("--- Vector Proximity Metrics ---")
print(f"Dimension count per text block: {len(vector_anchor)}")
print(f"Semantic match similarity metric: {score_semantic:.4f} (High affinity)")
print(f"Lexical match similarity metric:  {score_lexical:.4f} (Low affinity)")
