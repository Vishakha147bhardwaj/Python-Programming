import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import CommaSeparatedListOutputParser, StrOutputParser

# Bootstrapping environment variables from .env file
load_dotenv()

def main():
    if not os.getenv("ANTHROPIC_API_KEY"):
        raise ValueError("CRITICAL: ANTHROPIC_API_KEY not found in environment or .env file.")

    # Core engine initialization
    # Adjust the model ID based on your current active Anthropic endpoints (e.g., claude-3-7-sonnet-latest)
    llm = ChatAnthropic(model="claude-sonnet-4-5", temperature=0.2)

    # =========================================================================
    # STEP 1: DEFINE THE KEYWORD EXTRACTION PIPELINE
    # =========================================================================
    list_parser = CommaSeparatedListOutputParser()
    
    kw_template = (
        "You are an expert SEO data miner. Provide exactly 4 highly targeted keywords "
        "for a technical article about the topic: '{topic}'.\n"
        "Return ONLY the requested list items, separated exactly as instructed below. "
        "Do not include introduction text or preamble.\n"
        "{format_instructions}"
    )
    
    kw_prompt = PromptTemplate(
        template=kw_template,
        input_variables=["topic"],
        partial_variables={"format_instructions": list_parser.get_format_instructions()}
    )
    
    # Chain 1: Outputs a real Python List because of the list_parser
    keyword_chain = kw_prompt | llm | list_parser

    # =========================================================================
    # STEP 2: DEFINE THE OUTLINE GENERATOR PIPELINE
    # =========================================================================
    outline_template = (
        "You are a principal tech blogger. Write a comprehensive SEO blog post outline "
        "targeting an audience of: {audience}.\n"
        "You must structurally integrate these exact keywords into your sections: {keywords}.\n"
        "Use H1, H2, and H3 markdown structures cleanly."
    )
    
    outline_prompt = PromptTemplate.from_template(outline_template)
    
    # Chain 2: Outputs a standard clean string layout
    outline_chain = outline_prompt | llm | StrOutputParser()

    # =========================================================================
    # STEP 3: WORKFLOW EXECUTION & DATA HANDSHAKE
    # =========================================================================
    target_topic = "Docker Containerization for Beginners"
    target_audience = "Junior Frontend Engineers looking to learn DevOps basics"
    
    print(f"[Execution] Launching Step 1: Mining keywords for '{target_topic}'...")
    extracted_keywords_list = keyword_chain.invoke({"topic": target_topic})
    print(f"-> Successfully extracted: {extracted_keywords_list}\n")

    print("[Execution] Launching Step 2: Running the programmatic Data Handshake...")
    # Transforming the Python list object into a single, clean string for the next prompt
    joined_keywords_str = ", ".join(extracted_keywords_list)

    print("[Execution] Launching Step 3: Generating final structured layout blueprint...")
    final_blog_outline = outline_chain.invoke({
        "audience": target_audience,
        "keywords": joined_keywords_str
    })

    print("\n================ FINAL GENERATED ARTICLE BLUEPRINT ================")
    print(final_blog_outline)
    print("====================================================================\n")

if __name__ == "__main__":
    main()
