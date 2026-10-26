import os
from collections import Counter
from dotenv import load_dotenv
import anthropic
import chromadb
from chromadb.utils import embedding_functions

# ==========================================
# 1. INITIALIZATION & ENVIRONMENT SETUP
# ==========================================
# Automatically look for a .env file and load ANTHROPIC_API_KEY into os.environ
load_dotenv()

# Verify that the API key was successfully extracted
if not os.environ.get("ANTHROPIC_API_KEY"):
    raise ValueError("CRITICAL ERROR: ANTHROPIC_API_KEY not found. Ensure your .env file is formatted correctly.")

# Initialize the Anthropic and ChromaDB clients
client = anthropic.Anthropic()
chroma_client = chromadb.Client()

# Set up Chroma's default local embedding function (SentenceTransformers)
embedding_fn = embedding_functions.DefaultEmbeddingFunction()
collection = chroma_client.create_collection(
    name="hybrid_search_store", 
    embedding_function=embedding_fn
)

# ==========================================
# 2. SAMPLE DATASET CONFIGURATION
# ==========================================
# A sample dataset containing precise technical identifiers (SKUs) and context strings
documents = [
    {
        "id": "doc1", 
        "text": "The model enterprise version relies on isolated AWS infrastructure with SKU-9920X."
    },
    {
        "id": "doc2", 
        "text": "Our software offers secure cloud hosting solutions for large corporations."
    },
    {
        "id": "doc3", 
        "text": "Legacy database systems often struggle with high-throughput modern microservices."
    }
]

# Populate the dense vector database collection
for doc in documents:
    collection.add(
        documents=[doc["text"]],
        ids=[doc["id"]]
    )

# ==========================================
# 3. SPARSE SEARCH UTILITY (TERM MATCHING)
# ==========================================
def compute_sparse_scores(query: str, docs: list) -> dict:
    """
    Computes a basic keyword frequency (TF-IDF equivalent) matching rank.
    Returns a dictionary mapping document IDs to raw match counts.
    """
    query_words = query.lower().split()
    sparse_scores = {}
    for d in docs:
        text_lower = d["text"].lower()
        # Count occurrences of each query word in the document text
        score = sum(text_lower.count(word) for word in query_words)
        sparse_scores[d["id"]] = float(score)
    return sparse_scores

# ==========================================
# 4. HYBRID RETRIEVAL PIPELINE EXECUTION
# ==========================================
# A query requiring BOTH meaning ("cloud hosting") and exact matching ("SKU-9920X")
query_text = "What cloud hosting option matches enterprise SKU-9920X?"

# --- Step A: Dense Semantic Query ---
dense_results = collection.query(query_texts=[query_text], n_results=3)

# Flatten list out of Chroma's batch structure and map to zero-indexed ranks
dense_ids = dense_results['ids'][0] if dense_results['ids'] else []
dense_ranked = {res_id: rank for rank, res_id in enumerate(dense_ids)}

# --- Step B: Sparse Keyword Query ---
sparse_scores = compute_sparse_scores(query_text, documents)
# Sort documents by score descending to determine keyword ranks
sorted_sparse = sorted(sparse_scores.items(), key=lambda x: x[1], reverse=True)
sparse_ranked = {doc_id: rank for rank, (doc_id, score) in enumerate(sorted_sparse)}

# --- Step C: Reciprocal Rank Fusion (RRF) ---
rrf_scores = {}
k_factor = 60  # Smoothing constant to mitigate the impact of low/extreme ranks

for doc in documents:
    d_id = doc["id"]
    
    # If a document doesn't show up in a list, assign a severe penalty rank
    dense_rank = dense_ranked.get(d_id, 999)
    sparse_rank = sparse_ranked.get(d_id, 999)
    
    # Calculate RRF Score (higher score = better overall blended match rank)
    score = (1.0 / (k_factor + dense_rank)) + (1.0 / (k_factor + sparse_rank))
    rrf_scores[d_id] = score

# Identify the absolute highest-scoring blended document ID
best_doc_id = max(rrf_scores, key=rrf_scores.get)
retrieved_context = next(d["text"] for d in documents if d["id"] == best_doc_id)

# ==========================================
# 5. GENERATIVE RESPONSE GENERATION VIA CLAUDE
# ==========================================
# Forward the highly accurate context directly into Anthropic Claude
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=300,
    system="You are an expert system. Answer the user query using strictly the provided context.",
    messages=[
        {
            "role": "user", 
            "content": f"Context: {retrieved_context}\n\nQuery: {query_text}"
        }
    ]
)

# Output results to console
print("\n" + "="*50)
print("🎯 HYBRID RETRIEVAL PIPELINE COMPLETE")
print("="*50)
print(f"Blended Top Context Found:\n > \"{retrieved_context}\"\n")
print(f"Claude Response:\n{response.content[0].text}")
print("="*50)
