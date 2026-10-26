"""Competitor analysis with LangChain LCEL + Claude structured output.

.env expected:
    ANTHROPIC_API_KEY=sk-ant-api03-...      (required)
    ANTHROPIC_WORKSPACE_ID=...              (only if the key isn't workspace-scoped)
    ANTHROPIC_MODEL=claude-sonnet-5-5       (optional override)
"""

import os
import sys
from typing import Literal

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic


# ---------------------------------------------------------------------------
# 1. Config
# ---------------------------------------------------------------------------
load_dotenv(override=True)  # .env wins over any stale shell variables


def load_config() -> dict:
    api_key = os.getenv("ANTHROPIC_API_KEY", "").strip().strip('"').strip("'")
    workspace_id = os.getenv("ANTHROPIC_WORKSPACE_ID", "").strip()
    model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-5-5").strip()

    if not api_key:
        sys.exit("ANTHROPIC_API_KEY is missing from .env")

    if not api_key.startswith("sk-ant-"):
        sys.exit("ANTHROPIC_API_KEY doesn't look like an Anthropic key (should start with 'sk-ant-').")

    # Newer user-level keys (sk-ant-usr-...) aren't tied to one workspace,
    # so the API needs the workspace ID sent as a header.
    if api_key.startswith("sk-ant-usr") and not workspace_id:
        sys.exit(
            "This key (sk-ant-usr-...) needs a workspace ID.\n"
            "Copy it from console.anthropic.com -> Settings -> Workspaces -> <your workspace>,\n"
            "then add to .env:  ANTHROPIC_WORKSPACE_ID=<that id>"
        )

    return {"api_key": api_key, "workspace_id": workspace_id, "model": model}


# ---------------------------------------------------------------------------
# 2. Output schema
# ---------------------------------------------------------------------------
class CompetitorAnalysis(BaseModel):
    """Structured competitor assessment."""

    company_name: str = Field(description="Name of the competitor company")
    core_advantages: list[str] = Field(
        description="Up to 3 competitive advantages supported by the data",
        max_length=3,
    )
    weaknesses: list[str] = Field(description="Notable weaknesses or gaps")
    market_threat_level: Literal["HIGH", "MEDIUM", "LOW"] = Field(
        description="Overall threat this competitor poses"
    )
    rationale: str = Field(description="One or two sentences justifying the threat level")


# ---------------------------------------------------------------------------
# 3. Pipeline
# ---------------------------------------------------------------------------
PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert market research analyst. Provide objective, "
        "metrics-driven insights. Only include points supported by the data; "
        "never invent advantages or weaknesses to fill a list.",
    ),
    ("human", "Analyze the following competitor profile data:\n{raw_data}"),
])


def build_pipeline(cfg: dict):
    model = ChatAnthropic(
        model=cfg["model"],
        # No temperature: newer Claude models only accept the default value.
        max_tokens=1024,
        api_key=cfg["api_key"],
        default_headers=(
            {"anthropic-workspace-id": cfg["workspace_id"]} if cfg["workspace_id"] else None
        ),
    )
    # method="json_schema" uses Claude's native structured outputs instead of a
    # forced tool call (tool_choice), which newer models don't support.
    return PROMPT | model.with_structured_output(CompetitorAnalysis, method="json_schema")


def analyze(pipeline, raw_data: str) -> CompetitorAnalysis:
    try:
        return pipeline.invoke({"raw_data": raw_data})
    except Exception as e:  # turn common API errors into readable messages
        msg = str(e)
        if "invalid x-api-key" in msg:
            sys.exit("Anthropic rejected the API key (401). Create a new key and update .env.")
        if "not scoped to a workspace" in msg:
            sys.exit(
                "This key isn't tied to a workspace. Either create the key from inside a "
                "workspace in the Console, or add ANTHROPIC_WORKSPACE_ID=... to .env."
            )
        if "credit balance" in msg.lower():
            sys.exit("Your Anthropic org has no credits. Add billing in the Console.")
        if "not_found" in msg or "model" in msg.lower() and "404" in msg:
            sys.exit(f"Model '{os.getenv('ANTHROPIC_MODEL', 'claude-sonnet-5-5')}' not found for this key.")
        raise


# ---------------------------------------------------------------------------
# 4. Run
# ---------------------------------------------------------------------------
SAMPLE_DATA = """
NexusCorp has been taking our market share rapidly. They offer an intuitive drag-and-drop
UI that users love, and their licensing fees are 40% cheaper than ours. However, their
enterprise security protocols are weak, and they lack compliance certs for healthcare markets.
"""

if __name__ == "__main__":
    cfg = load_config()
    pipeline = build_pipeline(cfg)
    result = analyze(pipeline, SAMPLE_DATA)

    print("Structured Output Type:", type(result).__name__)
    print(result.model_dump_json(indent=2))