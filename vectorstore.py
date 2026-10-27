"""Build (or reload) a LlamaIndex vector index over ./data, answered by Claude.

.env expected:
    ANTHROPIC_API_KEY=sk-ant-...
    ANTHROPIC_WORKSPACE_ID=...          (needed for sk-ant-usr-... keys)
    ANTHROPIC_MODEL=claude-sonnet-5-5   (optional override)

Install:
    pip install -U llama-index llama-index-llms-anthropic \
        llama-index-embeddings-huggingface python-dotenv
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from llama_index.core import (
    Settings,
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
)
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.anthropic import Anthropic

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
load_dotenv(override=True)

API_KEY = os.getenv("ANTHROPIC_API_KEY", "").strip().strip('"').strip("'")
WORKSPACE_ID = os.getenv("ANTHROPIC_WORKSPACE_ID", "").strip()
MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-5-5").strip()

DATA_DIR = Path("./data")
STORAGE_DIR = Path("./storage")

if not API_KEY.startswith("sk-ant-"):
    sys.exit("ANTHROPIC_API_KEY is missing or malformed in .env")
if API_KEY.startswith("sk-ant-usr") and not WORKSPACE_ID:
    sys.exit("This key needs ANTHROPIC_WORKSPACE_ID in .env")

# ---------------------------------------------------------------------------
# Global models
# ---------------------------------------------------------------------------
Settings.llm = Anthropic(
    model=MODEL,
    api_key=API_KEY,
    # LlamaIndex always sends a temperature (its default is 0.1), and newer
    # Claude models reject anything but the API default, so pin it to 1.0.
    temperature=1.0,
    max_tokens=2048,
    default_headers={"anthropic-workspace-id": WORKSPACE_ID} if WORKSPACE_ID else None,
)

# Runs locally; the model (~130 MB) downloads once on first run.
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")


# ---------------------------------------------------------------------------
# Build or load the index
# ---------------------------------------------------------------------------
def get_index() -> VectorStoreIndex:
    if STORAGE_DIR.exists():
        print("📂 Loading existing index from ./storage ...")
        storage = StorageContext.from_defaults(persist_dir=str(STORAGE_DIR))
        return load_index_from_storage(storage)

    if not DATA_DIR.exists() or not any(DATA_DIR.iterdir()):
        sys.exit("./data is missing or empty. Add some .txt/.pdf/.md files and rerun.")

    print("🔨 Building index from ./data ...")
    documents = SimpleDirectoryReader(str(DATA_DIR), recursive=True).load_data()
    print(f"   Loaded {len(documents)} document chunks")

    index = VectorStoreIndex.from_documents(documents, show_progress=True)
    index.storage_context.persist(persist_dir=str(STORAGE_DIR))
    print("💾 Index saved to ./storage (delete that folder to rebuild)")
    return index


if __name__ == "__main__":
    index = get_index()
    print("📌 VectorStoreIndex ready.")

    query_engine = index.as_query_engine(similarity_top_k=3)
    response = query_engine.query("Summarize the key points in these documents.")
    print("\n[ANSWER]:\n", response)