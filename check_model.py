
import os
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("Available Gemini models:\n")

for model in client.models.list():
    if model.supported_actions:
        if "generateContent" in model.supported_actions:
            print(model.name)

