from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Initialize a text encoder model
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Generate vector matrices
sample_vector = embed_model.get_text_embedding("Internal linking maximizes domain authority.")

print(f"Vector Space Dimensionality: {len(sample_vector)}")
print(f"Sample Float Value Coordinates: {sample_vector[:5]}")
