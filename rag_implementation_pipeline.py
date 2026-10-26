import os
import sys
from importlib.metadata import version, PackageNotFoundError

from dotenv import load_dotenv
from llama_index.core import Document, VectorStoreIndex, Settings
from llama_index.llms.anthropic import Anthropic
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Load your Anthropic API Key securely from the environment
load_dotenv()

# Change the model in one place (or set CLAUDE_MODEL in your .env)
MODEL_NAME = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-5-20250929")


def print_versions():
    """Show installed package versions - the #1 cause of 'Empty Response'."""
    for pkg in ["llama-index-core", "llama-index-llms-anthropic", "anthropic"]:
        try:
            print(f"   {pkg}: {version(pkg)}")
        except PackageNotFoundError:
            print(f"   {pkg}: NOT INSTALLED")


def preflight_llm_check(llm):
    """
    Call Claude directly (no RAG) before building anything.
    If this returns empty text, the problem is the model/wrapper,
    not your retrieval pipeline.
    """
    print("--- Preflight: Testing Claude connection directly ---")
    try:
        result = llm.complete("Reply with exactly: Connection OK")
    except Exception as e:
        print(f"[ERROR] Claude call failed: {type(e).__name__}: {e}")
        print("Check your model name and API key, then try again.")
        sys.exit(1)

    text = (result.text or "").strip()
    print(f"[Claude replied]: {text!r}")

    if not text:
        print("\n[ERROR] Claude returned an EMPTY reply.")
        print("Fix: upgrade the LlamaIndex Anthropic wrapper inside your venv:")
        print("   pip install -U llama-index-llms-anthropic llama-index-core anthropic")
        print("Or try a newer model by setting CLAUDE_MODEL in your .env.")
        sys.exit(1)

    print("Preflight passed.\n")


def run_lecture_2_pipeline():
    # Safety Check: Ensure the API key exists before executing
    if not os.getenv("ANTHROPIC_API_KEY"):
        raise ValueError("Missing ANTHROPIC_API_KEY in your .env file.")

    print("=== [LECTURE 2] INDEXING & RETRIEVAL-AUGMENTED GENERATION (RAG) ===")
    print("Installed versions:")
    print_versions()
    print()

    # -------------------------------------------------------------------------
    # GLOBAL CONFIGURATION: ANTHROPIC + LOCAL EMBEDDINGS
    # -------------------------------------------------------------------------
    # 1. Claude is our reasoning model. Low temperature (0.1) keeps answers
    #    grounded; explicit max_tokens avoids truncated or empty replies.
    Settings.llm = Anthropic(model=MODEL_NAME, temperature=0.1, max_tokens=1024)

    # 2. Local, free embedding model from Lecture 1.
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    print(f"System initialized with {MODEL_NAME} & local embeddings.\n")

    # Verify Claude actually answers before running the full pipeline
    preflight_llm_check(Settings.llm)

    # -------------------------------------------------------------------------
    # STEP 1: PREPARING THE SEO DATASET
    # -------------------------------------------------------------------------
    print("--- Step 1: Loading Dataset into Memory ---")
    seo_kb_data = [
        Document(
            text="To optimize for voice search, target long-tail keywords phrased as natural questions. Use conversational structures and implement schema markup (FAQPage) to capture Google rich snippets.",
            metadata={"topic": "Voice Search", "tactic": "On-Page Optimization"},
        ),
        Document(
            text="Backlink building strategies should strictly target high Domain Authority (DA) websites within your vertical. Avoid automated link insertion networks; search engines easily detect these patterns and penalize target domains.",
            metadata={"topic": "Link Building", "tactic": "Off-Page Optimization"},
        ),
        Document(
            text="Programmatic SEO involves generating landing pages at scale using database variables. Ensure each page features unique localized content, programmatic title modifications, and distinct meta tags to avoid duplicate content penalties.",
            metadata={"topic": "Programmatic SEO", "tactic": "Scale Engineering"},
        ),
    ]
    print(f"Dataset successfully created with {len(seo_kb_data)} reference documents.")

    # -------------------------------------------------------------------------
    # STEP 2: BUILDING THE VECTOR STORE INDEX
    # -------------------------------------------------------------------------
    print("\n--- Step 2: Building VectorStoreIndex ---")
    # Loops through documents, embeds them with the local model,
    # and stores the vectors in an in-memory vector store.
    index = VectorStoreIndex.from_documents(seo_kb_data)
    print("Vector database index built completely.")

    # -------------------------------------------------------------------------
    # STEP 3: CREATING THE QUERY ENGINE
    # -------------------------------------------------------------------------
    print("\n--- Step 3: Assembling the Query Engine ---")
    # similarity_top_k=1 -> retrieve only the single best-matching chunk.
    # (allow_empty removed: it only hides failures instead of fixing them.)
    query_engine = index.as_query_engine(
        similarity_top_k=1,
        response_mode="compact",
    )
    print("Query Engine configuration complete.")

    # -------------------------------------------------------------------------
    # STEP 4: EXECUTING USER WORKFLOWS (RAG TRACER)
    # -------------------------------------------------------------------------
    print("\n--- Step 4: Dispatching Production Prompt to Claude ---")
    user_question = "What are the structural risks of using automated link insertion networks?"
    print(f"[User Input]: {user_question}")
    print("Processing vector search and requesting answer from Anthropic...")

    response = query_engine.query(user_question)

    print("\n===================[ CLAUDE'S RESPONSE ]===================")
    if response.response and response.response.strip():
        print(response.response)
    else:
        print("[WARNING] Synthesizer returned no text.")
        print(f"Raw response value: {response.response!r}")
    print("============================================================\n")

    # -------------------------------------------------------------------------
    # STEP 5: VERIFYING TRACE DATA (PROVING THE RAG CONTEXT)
    # -------------------------------------------------------------------------
    print("--- Diagnostic Check: Document Sources Used by Claude ---")
    # Shows the exact chunk fetched from the vector store to ground the answer.
    for source in response.source_nodes:
        print(f"-> Closest Node Match: '{source.node.get_content()[:110]}...'")
        print(f"-> Source Metadata: {source.node.metadata}")
        score = round(source.score, 4) if source.score is not None else "n/a"
        print(f"-> Similarity Score: {score}")
    print("========================================================\n")


if __name__ == "__main__":
    run_lecture_2_pipeline()