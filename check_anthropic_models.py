
import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load variables from the .env file
load_dotenv()

# Read the API key
api_key = os.getenv("ANTHROPIC_API_KEY")

# Stop if the key is missing
if not api_key:
    raise ValueError(
        "API key not found. Check your .env file."
    )

# Initialize the client with the API key
client = Anthropic(api_key=api_key)

try:
    # List models available to this API key
    models = client.models.list(limit=100)

    print("\nAvailable Anthropic models:\n")

    for model in models.data:
        print(model.id)

except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")