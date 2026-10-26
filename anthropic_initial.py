
import os
import json

from dotenv import load_dotenv
from anthropic import (
    Anthropic,
    APIStatusError,
    APIConnectionError,
    RateLimitError,
    AuthenticationError,
)

# ============================================================
# 1. LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError(
        "ANTHROPIC_API_KEY not found.\n"
        "Please check your .env file."
    )


# ============================================================
# 2. INITIALIZE ANTHROPIC CLIENT
# ============================================================

anthropic_client = Anthropic(api_key=api_key)


# ============================================================
# 3. EXTRACT STRUCTURED JSON
# ============================================================

def extract_structured_json_via_prefilling(
    raw_text_data: str
) -> dict:
    """
    Extract organization and country names from text.

    Returns a Python dictionary containing:
    - organizations: list of organization names
    - countries: list of country names

    Note: This function no longer uses assistant prefilling.
    """

    system_prompt = """
    You are an entity extraction assistant.

    Extract organizations and countries from the provided text.

    Return a JSON object with exactly two keys:

    1. organizations: an array of organization names.
    2. countries: an array of country names.

    Rules:
    - Include only entities explicitly mentioned in the text.
    - Do not classify cities as countries.
    - Do not include explanations or Markdown.
    - Use empty arrays when no matching entities are found.
    """

    # Make the API request
    response = anthropic_client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=1000,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": raw_text_data,
            }
        ],
    )

    # ========================================================
    # 4. EXTRACT TEXT FROM THE API RESPONSE
    # ========================================================

    response_text = "".join(
        block.text
        for block in response.content
        if block.type == "text"
    ).strip()

    if not response_text:
        raise ValueError("The API returned an empty text response.")

    # ========================================================
    # 5. PARSE AND VALIDATE JSON
    # ========================================================

    result = json.loads(response_text)

    if not isinstance(result, dict):
        raise ValueError("The response must be a JSON object.")

    required_keys = {"organizations", "countries"}

    if set(result.keys()) != required_keys:
        raise ValueError(
            "JSON must contain exactly 'organizations' "
            "and 'countries'."
        )

    for key in required_keys:
        if not isinstance(result[key], list):
            raise ValueError(f"'{key}' must be a list.")

        if not all(isinstance(item, str) for item in result[key]):
            raise ValueError(
                f"Every item in '{key}' must be a string."
            )

    # ========================================================
    # 6. DISPLAY TOKEN USAGE
    # ========================================================

    print("\n--- API Usage ---")
    print("Input tokens:", response.usage.input_tokens)
    print("Output tokens:", response.usage.output_tokens)

    return result


# ============================================================
# 7. TEST THE FUNCTION
# ============================================================

if __name__ == "__main__":

    sample_data = (
        "Google expanding operations into Munich, Germany "
        "and Dublin, Ireland."
    )

    print("--- Input Text ---")
    print(sample_data)

    try:
        json_output = extract_structured_json_via_prefilling(
            sample_data
        )

        print("\n--- Extracted JSON ---")
        print(json.dumps(json_output, indent=4, ensure_ascii=False))

    except AuthenticationError:
        print("\nAuthentication failed.")
        print("Check your ANTHROPIC_API_KEY in the .env file.")

    except RateLimitError as e:
        print("\nRate limit or usage limit reached.")
        print(e.message)

    except APIStatusError as e:
        print(f"\nAnthropic API error: HTTP {e.status_code}")
        print(e.message)

    except APIConnectionError:
        print("\nCould not connect to Anthropic.")
        print("Check your internet connection.")

    except json.JSONDecodeError:
        print("\nThe API response was not valid JSON.")

    except ValueError as e:
        print(f"\nValidation error: {e}")

    except Exception as e:
        print(f"\nUnexpected error: {type(e).__name__}: {e}")


def stream_corporate_strategy(prompt_topic: str):
    print(f"\n[STREAM START] Topic: {prompt_topic}")
    
    try:
        # Open a context-managed stream block
        with anthropic_client.messages.stream(
            model="claude-3-5-sonnet",
            max_tokens=1500,
            temperature=0.7,
            messages=[{"role": "user", "content": f"Draft an executive summary on: {prompt_topic}"}]
        ) as stream:
            
            # Iterate through incoming server-sent events
            for event in stream:
                # Filter for text mutations
                if event.type == "content_block_delta":
                    # Access the nested delta text properties
                    print(event.delta.text, end="", flush=True)
                    
        print("\n[STREAM END]")
        
        # Accumulate terminal stream states to review final usage matrix
        final_message = stream.get_final_message()
        print(f"\nTotal Session Cost: {final_message.usage.input_tokens + final_message.usage.output_tokens} tokens.")

    except APIConnectionError as e:
        print(f"\nNetwork Connectivity Lost: {e}")
    except RateLimitError:
        print("\nRate limit hit (429). Initiating exponential backoff routine...")
