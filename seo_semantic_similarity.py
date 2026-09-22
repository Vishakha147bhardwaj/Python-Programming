import numpy as np
from sentence_transformers import SentenceTransformer, util

def run_semantic_gap_analysis(your_content, competitor_content, gap_threshold=0.55):
    """
    Identifies unique concepts in competitor content missing from your content.
    
    gap_threshold: Similarity scores BELOW this value mean your content does 
                   not adequately cover the competitor's topic.
    """
    # Initialize the encoder model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # 1. Chunk content into granular paragraphs/concepts
    your_chunks = [p.strip() for p in your_content.split('\n\n') if p.strip()]
    comp_chunks = [p.strip() for p in competitor_content.split('\n\n') if p.strip()]
    
    if not your_chunks or not comp_chunks:
        return {"error": "Content profiles must contain valid paragraph separation."}
    
    # 2. Compute Dense Vector Embeddings
    your_embeddings = model.encode(your_chunks, convert_to_tensor=True)
    comp_embeddings = model.encode(comp_chunks, convert_to_tensor=True)
    
    # 3. Calculate the Cosine Similarity Matrix between all variations
    # Shape: (Number of competitor chunks, Number of your chunks)
    similarity_matrix = util.cos_sim(comp_embeddings, your_embeddings)
    
    gaps_identified = []
    
    # 4. Iterate through competitor content to find unmapped nodes
    for index, comp_chunk in enumerate(comp_chunks):
        # Find your highest semantic coverage score for this specific competitor paragraph
        best_match_score = float(np.max(similarity_matrix[index].cpu().numpy()))
        best_match_idx = int(np.argmax(similarity_matrix[index].cpu().numpy()))
        
        # If the best match falls below the threshold, a content gap exists
        if best_match_score < gap_threshold:
            gaps_identified.append({
                "competitor_topic": comp_chunk,
                "highest_similarity_found": round(best_match_score, 3),
                "closest_matching_paragraph": your_chunks[best_match_idx] if best_match_score > 0.3 else "None"
            })
            
    return {
        "summary": {
            "total_competitor_topics": len(comp_chunks),
            "gaps_found": len(gaps_identified)
        },
        "detected_gaps": sorted(gaps_identified, key=lambda x: x["highest_similarity_found"])
    }

# --- Execution Example ---
my_article = """
Our software platform utilizes advanced encryption protocols to secure customer transactions.
We provide 24/7 customer support via email or live chat to resolve system disruptions quickly.
"""

competitor_article = """
Security operations leverage end-to-end AES-256 bit encryption algorithms to isolate financial transaction pipelines.
Our systems run automated daily database backups to ensure full data recovery during infrastructure failures.
Customer support desks handle standard operational inquiries within fifteen minutes.
"""

gap_report = run_semantic_gap_analysis(my_article, competitor_article, gap_threshold=0.60)
print(f"Gaps Found: {gap_report['summary']['gaps_found']}\n")
for gap in gap_report['detected_gaps']:
    print(f"⚠️ MISSING CONCEPT:\n   \"{gap['competitor_topic']}\"")
    print(f"   (Max Similarity Score: {gap['highest_similarity_found']})\n")
