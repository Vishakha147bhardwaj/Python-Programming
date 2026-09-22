import json
from typing import Dict, Any

# 1. Define the Prompt Template with Variables
ADVANCED_PROMPT_TEMPLATE = """
Role:
You are an expert Data Quality Engineer specializing in unstructured text parsing and PII (Personally Identifiable Information) compliance.

Task:
Analyze the provided user raw text log. Extract key metadata, identify potential security risks, and classify the sentiment.

Variables:
- CURRENT_DATE: {current_date}
- RAW_TEXT_LOG: {raw_text_log}

Chain-of-Thought Requirements:
Before generating the final JSON output, you MUST execute your reasoning steps inside a scratchpad.
In your scratchpad, document:
1. An inspection of the text for PII flags (emails, phones, keys).
2. The logic used to determine sentiment polarity.
3. A extraction plan for metadata.

Output Constraints:
- Return your response strictly as a valid JSON object.
- Do NOT wrap the JSON in markdown code blocks (e.g., do not use ```json ... ```).
- Do NOT include conversational filler or introductory text.
- Follow the JSON Schema provided below exactly.

JSON Schema Response Format:
{{
    "scratchpad": {{
        "pii_analysis": "string detailing the step-by-step PII check",
        "sentiment_logic": "string detailing how sentiment was weighed",
        "extraction_steps": "string listing steps to extract fields"
    }},
    "extracted_data": {{
        "user_id": "string or null",
        "resolved_email": "string or null",
        "system_components": ["string"]
    }},
    "compliance_metrics": {{
        "contains_pii": boolean,
        "risk_score": integer (scale 1-10)
    }},
    "sentiment": "STRONG_NEGATIVE" | "NEGATIVE" | "NEUTRAL" | "POSITIVE" | "STRONG_POSITIVE",
    "processed_at": "string (YYYY-MM-DD)"
}}
"""

def run_pipeline(user_log: str, date_str: str) -> Dict[str, Any]:
    # 2. Inject variables into the template dynamically
    formatted_prompt = ADVANCED_PROMPT_TEMPLATE.format(
        current_date=date_str,
        raw_text_log=user_log
    )
    
    # Mocking the LLM API call response for demonstration execution.
    # In production, this string is returned directly by an LLM like GPT-4, Claude, or Gemini.
    mock_llm_raw_response = """{
    "scratchpad": {
        "pii_analysis": "Scanned text. Found email pattern 'john.doe@enterprise.com'. No credit cards or phone numbers visible.",
        "sentiment_logic": "Tokens include 'frustrated', 'broken API', 'complete failure'. This indicates intense negative sentiment. Classifying as STRONG_NEGATIVE.",
        "extraction_steps": "Identified system component 'AuthGateway'. User ID explicitly stated as 'USR-9021'."
    },
    "extracted_data": {
        "user_id": "USR-9021",
        "resolved_email": "john.doe@enterprise.com",
        "system_components": ["AuthGateway"]
    },
    "compliance_metrics": {
        "contains_pii": true,
        "risk_score": 7
    },
    "sentiment": "STRONG_NEGATIVE",
    "processed_at": "2026-09-17"
}"""

    # 3. Parse and validate the output directly into downstream systems
    try:
        parsed_json = json.loads(mock_llm_raw_response)
        return parsed_json
    except json.JSONDecodeError as e:
        print(f"Failed to parse LLM response as JSON: {e}")
        return {}

# --- Execution ---
if __name__ == "__main__":
    sample_log = "Error 500 from AuthGateway for user USR-9021. I am extremely frustrated, your broken API caused a complete failure. Fix it or contact me at john.doe@enterprise.com."
    current_execution_date = "2026-09-17"
    
    result = run_pipeline(sample_log, current_execution_date)
    
    # Verify the structure is a real python dictionary now
    print(f"Successfully processed structured data.")
    print(f"Risk Score: {result['compliance_metrics']['risk_score']}/10")
    print(f"Sentiment: {result['sentiment']}")
    print(f"Reasoning Scratchpad Summary: {result['scratchpad']['sentiment_logic']}")
