import os
from dotenv import load_dotenv
from llama_index.core import Document, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Load environment variables from the .env file
load_dotenv()

def run_lecture_1_pipeline():
    # Verify that the Anthropic key is present in the environment
    if not os.getenv("ANTHROPIC_API_KEY"):
        raise ValueError("Missing ANTHROPIC_API_KEY in your .env file.")

    print("=== [LECTURE 1] DATA PREPARATION & EMBEDDING PIPELINE ===")

    # -------------------------------------------------------------------------
    # GLOBAL CONFIGURATION: LOCAL EMBEDDINGS
    # -------------------------------------------------------------------------
    # Because we don't have an OpenAI key, we instruct LlamaIndex to use a free, 
    # open-source embedding model that runs 100% locally on your computer.
    print("Loading local HuggingFace embedding model (bge-small-en-v1.5)...")
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    print("Local embedding model loaded successfully.\n")

    # -------------------------------------------------------------------------
    # STEP 1: DOCUMENT LOADING & METADATA INGESTION
    # -------------------------------------------------------------------------
    print("--- Step 1: Ingesting Raw SEO Data ---")
    
    # Raw unstructured text representing a technical document or system audit file
    raw_seo_report = (
        "SEO Strategy Guide 2026. "
        "Core Web Vitals remain a crucial ranking factor for Google Search algorithms. "
        "Focus heavily on Interaction to Next Paint (INP), which has completely replaced First Input Delay (FID). "
        "Optimizing your Time to First Byte (TTFB) under 800ms gives websites an immediate crawl budget advantage."
    )

    # Convert the string into a structured LlamaIndex Document object.
    # We append metadata tags to make sorting and precise retrieval easier down the road.
    document = Document(
        text=raw_seo_report,
        metadata={
            "category": "Technical SEO",
            "author": "SEO Analytics Team",
            "year": "2026",
            "source_type": "Internal Document"
        }
    )
    print("Successfully generated standard Document object.")
    print(f"Attached Metadata: {document.metadata}\n")

    # -------------------------------------------------------------------------
    # STEP 2: CHUNKING / NODE PARSING
    # -------------------------------------------------------------------------
    print("--- Step 2: Parsing Document into Chunks (Nodes) ---")
    
    # We break documents down into smaller pieces so they fit cleanly into LLM text limitations.
    # chunk_size is measured in tokens; chunk_overlap keeps context fluent across splits.
    splitter = SentenceSplitter(chunk_size=40, chunk_overlap=10)
    nodes = splitter.get_nodes_from_documents([document])

    print(f"Total text chunks created: {len(nodes)}")
    for idx, node in enumerate(nodes):
        print(f"  [Chunk {idx} Text]: {node.get_content().strip()}")
        # Notice that LlamaIndex automatically copies the document's metadata to every single chunk!
        print(f"  [Chunk {idx} Metadata]: {node.metadata}")
    print("")

    # -------------------------------------------------------------------------
    # STEP 3: HIGH-DIMENSIONAL VECTOR EMBEDDINGS
    # -------------------------------------------------------------------------
    print("--- Step 3: Generating Vector Coordinates ---")
    
    # Grab the clean text from the first parsed node
    sample_text = nodes[0].get_content()
    
    # Convert that string into an array of floating-point numbers (vector embedding)
    vector_embedding = Settings.embed_model.get_text_embedding(sample_text)

    print("Embedding generation pipeline complete.")
    print(f"Vector Dimensions (Length of the array): {len(vector_embedding)}")
    print(f"First 5 Mathematical Coordinates: {vector_embedding[:5]}")
    print("========================================================\n")

if __name__ == "__main__":
    run_lecture_1_pipeline()
