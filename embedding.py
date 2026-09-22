from sentence_transformers import SentenceTransformer

# Load a lightweight, highly accurate production model (384 dimensions)
model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "How to optimize a website for search engines.",
    "SEO best practices for higher rankings."
]

# Generate dense vector representations
embeddings = model.encode(sentences)
print(embeddings)  # Output: (2, 384)
