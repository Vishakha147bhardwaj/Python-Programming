import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser

# Bootstrapping environment variables from .env file
load_dotenv()

def main():
    if not os.getenv("ANTHROPIC_API_KEY"):
        raise ValueError("CRITICAL: ANTHROPIC_API_KEY not found in environment or .env file.")

    print("[1/4] Constructing the Prompt Template...")
    template = (
        "You are an elite developer evangelist. Explain the concept of '{topic}' "
        "to a junior engineer in exactly two punchy sentences. Use a confident tone."
    )
    prompt_template = PromptTemplate.from_template(template)

    print("[2/4] Initializing the Chat Model (Anthropic)...")
    model = ChatAnthropic(
        model="claude-sonnet-4-5", 
        temperature=0.3
    )

    print("[3/4] Instantiating the Output Parser...")
    output_parser = StrOutputParser()

    print("[4/4] Composing the LCEL Pipeline Chain...")
    tech_chain = prompt_template | model | output_parser

    input_payload = {"topic": "Docker Containers"}
    print(f"\n---> Invoking chain with input: {input_payload}")
    
    try:
        response = tech_chain.invoke(input_payload)
        print("\n=== AI PIPELINE RESPONSE ===")
        print(response)
        print("============================\n")
    except Exception as e:
        print(f"An error occurred during chain execution: {str(e)}")

if __name__ == "__main__":
    main()
