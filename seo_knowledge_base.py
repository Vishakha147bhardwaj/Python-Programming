"""SEO policy knowledge base: index a playbook and answer audit questions with Claude.

.env expected:
    ANTHROPIC_API_KEY=sk-ant-...
    ANTHROPIC_WORKSPACE_ID=...          (needed for sk-ant-usr-... keys)
    ANTHROPIC_MODEL=claude-sonnet-5-5   (optional override)
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.base.base_query_engine import BaseQueryEngine
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.anthropic import Anthropic

# Own folder, so files from other scripts in ./data don't mix into retrieval.
DATA_DIR = Path("./seo_data")
PLAYBOOK = DATA_DIR / "seo_knowledge.txt"

PLAYBOOK_TEXT = (
    "=== CORPORATE SEO CONTENT PLAYBOOK ===\n\n"
    "RULE #1: TARGET METADATA STRATEGY\n"
    "Meta descriptions must remain between 120 and 155 characters. Every description "
    "must end with an explicit, high-conversion action verb CTA such as 'Download guide free' "
    "or 'Start trial today'. Never use vague assertions like 'Learn more here'.\n\n"
    "RULE #2: CORE WEB VITALS PERMANENT COMPLIANCE\n"
    "Image content must be uploaded in .webp format. No raw .png formats are allowed "
    "on high-traffic production landing web directories, to prevent degrading page "
    "speed metrics below compliance targets.\n"
)


def configure_models() -> None:
    load_dotenv(override=True)

    api_key = os.getenv("ANTHROPIC_API_KEY", "").strip().strip('"').strip("'")
    workspace_id = os.getenv("ANTHROPIC_WORKSPACE_ID", "").strip()
    model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-5-5").strip()

    if not api_key.startswith("sk-ant-"):
        sys.exit("ANTHROPIC_API_KEY is missing or malformed in .env")
    if api_key.startswith("sk-ant-usr") and not workspace_id:
        sys.exit("This key needs ANTHROPIC_WORKSPACE_ID in .env")

    Settings.llm = Anthropic(
        model=model,
        api_key=api_key,
        temperature=1.0,  # newer Claude models only accept the API default
        max_tokens=1024,
        default_headers={"anthropic-workspace-id": workspace_id} if workspace_id else None,
    )
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")


def ensure_playbook() -> None:
    """Create the sample playbook only if it doesn't exist (never overwrite edits)."""
    DATA_DIR.mkdir(exist_ok=True)
    if not PLAYBOOK.exists():
        PLAYBOOK.write_text(PLAYBOOK_TEXT, encoding="utf-8")
        print(f"   Created sample playbook at {PLAYBOOK}")


def setup_seo_knowledge_base() -> BaseQueryEngine:
    configure_models()
    ensure_playbook()

    print("[1/3] Loading corporate policy documents...")
    documents = SimpleDirectoryReader(str(DATA_DIR)).load_data()

    print("[2/3] Building vector index...")
    index = VectorStoreIndex.from_documents(documents)

    # top_k=3: with more than one policy file, a single chunk can miss the rule.
    return index.as_query_engine(similarity_top_k=3)


def ask(engine: BaseQueryEngine, question: str) -> None:
    print(f"User Query: '{question}'")
    response = engine.query(question)
    print(f"System Answer:\n{response}\n")
    for node in response.source_nodes:  # show what the answer was grounded in
        print(f"   ↳ source: {node.metadata.get('file_name')} (score {node.score:.2f})")
    print("-" * 60)


if __name__ == "__main__":
    seo_brain = setup_seo_knowledge_base()
    print("[3/3] Engine ready. Running audit queries...\n")

    ask(seo_brain, "What are the specific character limits and CTA constraints for our meta descriptions?")
    ask(seo_brain, "Can a team member upload a standard high-res PNG image onto a new product marketing page?")