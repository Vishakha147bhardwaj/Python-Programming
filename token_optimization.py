import time
import random
from typing import List, Generator
import tiktoken

def generate_optimal_embedding_batches(
    chunks: List[str], 
    max_tokens_per_batch: int = 8192, 
    model_name: str = "text-embedding-3-small"
) -> Generator[List[str], None, None]:
    """
    Groups text chunks into optimized batches based on real-time token counts
    to prevent API overflows and minimize network overhead.
    """
    # Load the specific encoding model to ensure exact token counts
    tokenizer = tiktoken.encoding_for_model(model_name)
    current_batch = []
    current_batch_tokens = 0

    for chunk in chunks:
        # Calculate precise token usage for the text segment
        chunk_token_count = len(tokenizer.encode(chunk))
        
        # If a single chunk exceeds safety thresholds, truncate or split it
        if chunk_token_count > max_tokens_per_batch:
            chunk = tokenizer.decode(tokenizer.encode(chunk)[:max_tokens_per_batch])
            chunk_token_count = max_tokens_per_batch

        # If adding this chunk exceeds the batch limit, yield the current batch
        if current_batch_tokens + chunk_token_count > max_tokens_per_batch:
            yield current_batch
            current_batch = [chunk]
            current_batch_tokens = chunk_token_count
        else:
            current_batch.append(chunk)
            current_batch_tokens += chunk_token_count

    # Yield any remaining chunks
    if current_batch:
        yield current_batch

def execute_embedding_request_with_backoff(api_client, batch: List[str], max_retries: int = 5):
    """
    Executes network requests using exponential backoff to handle rate limits safely.
    """
    delay = 1.0
    for attempt in range(max_retries):
        try:
            return api_client.embeddings.create(input=batch, model="text-embedding-3-small")
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            # Introduce jittered exponential backoff to prevent thundering herd problems
            time.sleep(delay + random.uniform(0, 0.5))
            delay *= 2
