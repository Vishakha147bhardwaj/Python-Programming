"""SEO content pipeline: strategy -> article -> metadata, built with LangChain LCEL.

.env expected:
    ANTHROPIC_API_KEY=sk-ant-...
    ANTHROPIC_WORKSPACE_ID=...          (needed for sk-ant-usr-... keys)
    ANTHROPIC_MODEL=claude-sonnet-5-5   (optional override)
"""

import os
import sys

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_anthropic import ChatAnthropic


# ---------------------------------------------------------------------------
# Config & model
# ---------------------------------------------------------------------------
load_dotenv(override=True)

API_KEY = os.getenv("ANTHROPIC_API_KEY", "").strip().strip('"').strip("'")
WORKSPACE_ID = os.getenv("ANTHROPIC_WORKSPACE_ID", "").strip()
MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-5-5").strip()

if not API_KEY.startswith("sk-ant-"):
    sys.exit("ANTHROPIC_API_KEY is missing or malformed in .env")
if API_KEY.startswith("sk-ant-usr") and not WORKSPACE_ID:
    sys.exit("This key needs ANTHROPIC_WORKSPACE_ID in .env")


def make_llm(max_tokens: int) -> ChatAnthropic:
    # No temperature: newer Claude models only accept the default.
    return ChatAnthropic(
        model=MODEL,
        max_tokens=max_tokens,
        api_key=API_KEY,
        default_headers={"anthropic-workspace-id": WORKSPACE_ID} if WORKSPACE_ID else None,
    )


small_llm = make_llm(1024)   # strategy + metadata
writer_llm = make_llm(8000)  # long-form article needs room


# ---------------------------------------------------------------------------
# Step 1: Keyword & intent strategy
# ---------------------------------------------------------------------------
class KeywordStrategy(BaseModel):
    primary_angle: str = Field(description="The unique angle or hook for the article")
    semantic_keywords: list[str] = Field(
        description="Top 5 closely related search terms", min_length=5, max_length=5
    )
    target_audience: str = Field(description="Profile of the ideal reader")


keyword_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an elite SEO strategist. Analyze topics for search intent."),
    ("human", "Develop an organic search strategy for the core topic: '{topic}'"),
])

keyword_chain = keyword_prompt | small_llm.with_structured_output(
    KeywordStrategy, method="json_schema"
)


# ---------------------------------------------------------------------------
# Step 2: Article writer (with revision history)
# ---------------------------------------------------------------------------
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a professional content marketer. Write engaging, comprehensive "
               "blog posts in Markdown."),
    MessagesPlaceholder("chat_history", optional=True),
    ("human",
     "Write a high-converting blog post based on these directions:\n"
     "Topic: {topic}\n"
     "Angle: {primary_angle}\n"
     "Keywords to include: {semantic_keywords}\n"
     "Target audience: {target_audience}\n\n"
     "Tone: authoritative yet approachable. Write at least 3 detailed sections."),
])

writer_chain = writer_prompt | writer_llm | StrOutputParser()


# ---------------------------------------------------------------------------
# Step 3: Metadata
# ---------------------------------------------------------------------------
class MetaData(BaseModel):
    meta_title: str = Field(description="SEO-optimized title", max_length=60)
    meta_description: str = Field(description="Compelling meta description", max_length=155)
    slug: str = Field(description="URL-friendly hyphenated slug", pattern=r"^[a-z0-9]+(-[a-z0-9]+)*$")


metadata_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a technical SEO specialist. Title must be under 60 characters, "
               "description under 155, slug lowercase and hyphenated."),
    ("human", "Generate the metadata for this article:\n\n{article_body}"),
])

metadata_chain = metadata_prompt | small_llm.with_structured_output(
    MetaData, method="json_schema"
)


# ---------------------------------------------------------------------------
# Full pipeline as one LCEL chain
# ---------------------------------------------------------------------------
def _writer_inputs(state: dict) -> dict:
    s: KeywordStrategy = state["strategy"]
    return {
        "topic": state["topic"],
        "primary_angle": s.primary_angle,
        "semantic_keywords": ", ".join(s.semantic_keywords),
        "target_audience": s.target_audience,
        "chat_history": state.get("chat_history", []),
    }


seo_pipeline = (
    RunnablePassthrough.assign(strategy=keyword_chain)
    | RunnablePassthrough.assign(article=_writer_inputs | writer_chain)
    | RunnablePassthrough.assign(
        metadata=(lambda s: {"article_body": s["article"]}) | metadata_chain
    )
)

# Session history, so follow-up revision requests see earlier drafts.
history = InMemoryChatMessageHistory()


def run_seo_automation_pipeline(topic: str) -> dict:
    print(f"🚀 Running SEO pipeline for: '{topic}'")
    result = seo_pipeline.invoke({"topic": topic, "chat_history": history.messages})

    history.add_user_message(f"Generate article for {topic}")
    history.add_ai_message(result["article"])

    return {
        "seo_strategy": result["strategy"].model_dump(),
        "article_content": result["article"],
        "metadata_configuration": result["metadata"].model_dump(),
    }


if __name__ == "__main__":
    out = run_seo_automation_pipeline("The Future of Serverless Databases in 2027")

    print("\n" + "=" * 50 + "\n🔥 PIPELINE RUN COMPLETE\n" + "=" * 50)
    print("\n[STRATEGY]:\n", out["seo_strategy"])
    print("\n[METADATA]:\n", out["metadata_configuration"])
    print("\n[ARTICLE PREVIEW]:\n", out["article_content"][:500] + "...")