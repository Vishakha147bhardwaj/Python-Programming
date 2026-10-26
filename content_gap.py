import re
import numpy as np

class RecursiveTextChunker:
    """Splits raw text down into logical semantic windows using structural delimiters."""
    def __init__(self, chunk_size: int = 200, overlap: int = 40):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split_text(self, text: str) -> list:
        # Separate by sentences or structural white spaces
        tokens = text.split(" ")
        chunks = []
        start = 0
        
        while start < len(tokens): 
            end = min(start + self.chunk_size, len(tokens))
            chunk_words = tokens[start:end]
            chunks.append(" ".join(chunk_words))
            # Step forward by chunk size minus overlap to retain narrative continuity
            start += (self.chunk_size - self.overlap)
            if end == len(tokens):
                break
        return chunks

def detect_content_gaps(my_portfolio_vectors: np.ndarray, competitor_vectors: np.ndarray, threshold: float = 0.65) -> list:
    """
    Identifies index positions of competitor content that have no matching coverage 
    within our portfolio based on a similarity threshold.
    """
    gap_indices = []
    
    for idx, comp_vec in enumerate(competitor_vectors):
        # Calculate dot products against all items in our portfolio simultaneously
        similarities = np.dot(my_portfolio_vectors, comp_vec) / (
            np.linalg.norm(my_portfolio_vectors, axis=1) * np.linalg.norm(comp_vec)
        )
        max_similarity = np.max(similarities)
        
        # If our closest article is below the threshold, it's a content gap
        if max_similarity < threshold:
            gap_indices.append((idx, max_similarity))
            
    return gap_indices

# Execution Simulation
if __name__ == "__main__":
    raw_document = (
        "Data egress fees are the unadvertised risk of enterprise cloud adoption. "
        "Providers charge premium flat rates per terabyte transferred out of their zones. "
        "Multi-cloud architectures compound this specific overhead significantly."
    )
    
    chunker = RecursiveTextChunker(chunk_size=15, overlap=4)
    processed_chunks = chunker.split_text(raw_document)
    print(f"Generated Chunks:\n{processed_chunks}\n")
    
    # Simulate vector representations
    np.random.seed(42)
    mock_my_content = np.random.randn(5, 128)      # 5 articles we wrote
    mock_competitor = np.random.randn(3, 128)      # 3 articles they wrote
    
    gaps = detect_content_gaps(mock_my_content, mock_competitor, threshold=0.25)
    print(f"Detected Competitor Content Gaps (Index, Closest Match Score): {gaps}")
