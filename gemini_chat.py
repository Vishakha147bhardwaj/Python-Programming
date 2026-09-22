
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


# --------------------------------------------------
# 1. Load API key from .env
# --------------------------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found. "
        "Check your .env file."
    )


# --------------------------------------------------
# 2. Create Gemini client
# --------------------------------------------------

client = genai.Client(
    api_key=api_key
)


# --------------------------------------------------
# 3. Create chat session
# --------------------------------------------------

chat = client.chats.create(
    model="gemini-3.6-flash",
    config=types.GenerateContentConfig(
        system_instruction=(
            "You are a helpful, precise engineering assistant."
        ),
    )
)


# --------------------------------------------------
# 4. Interactive chat loop
# --------------------------------------------------

def run_chat_loop():

    print("💬 Interactive Terminal Chat with Gemini started.")
    print("Type 'exit' or 'quit' at any time to end the session.\n")

    while True:

        try:

            # Get input from user
            user_input = input("\nYou: ")

            # Exit condition
            if user_input.strip().lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            # Ignore empty input
            if not user_input.strip():
                continue

            print("\nGemini: ", end="", flush=True)

            # --------------------------------------------------
            # Stream Gemini response
            # --------------------------------------------------

            for chunk in chat.send_message_stream(
                message=user_input
            ):

                if chunk.text:
                    print(
                        chunk.text,
                        end="",
                        flush=True
                    )

            print()

        except Exception as e:

            print(f"\nAn error occurred: {e}")


# --------------------------------------------------
# 5. Start the application
# --------------------------------------------------

if __name__ == "__main__":
    run_chat_loop()

