import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

def run_chat_loop():
    print("💬 Interactive Terminal Chat with Claude started.")
    print("Type 'exit' or 'quit' at any time to end the session.\n")
    
    # This array acts as the model's ongoing memory log
    conversation_history = []
    
    while True:
        try:
            # Get prompt from user terminal
            user_input = input("\nYou: ")
            if user_input.strip().lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
                
            if not user_input.strip():
                continue
                
            # 1. Append the new user message to our history log
            conversation_history.append({"role": "user", "content": user_input})
            
            print("\nClaude: ", end="", flush=True)
            
            # 2. Track assistant's response tokens streamingly
            assistant_response = ""
            with client.messages.stream(
                model="claude-sonnet-5",
                max_tokens=1000,
                system="You are a helpful, precise engineering assistant.",
                messages=conversation_history
            ) as stream:
                for text in stream.text_stream:
                    print(text, end="", flush=True)
                    assistant_response += text
            print() # Print clean new line at completion
            
            # 3. Append the assistant's complete final answer back to memory
            conversation_history.append({"role": "assistant", "content": assistant_response})
            
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            break

if __name__ == "__main__":
    run_chat_loop()
