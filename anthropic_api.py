# import os
# from dotenv import load_dotenv
# from anthropic import Anthropic

# # Load environment variables from your local .env file
# load_dotenv()

# # Initialize the official Anthropic client
# client = Anthropic()

# def ask_claude():
#     try:
#         response = client.messages.create(
#             model="claude-sonnet-5",
#             max_tokens=500,         
#             system="You are a senior code auditor. Keep responses punchy, clear, and objective.", 
#             messages=[
#                 {
#                     "role": "user", 
#                     "content": "Review this logic block for vulnerabilities: 'if user.role == \"admin\" or \"superadmin\": grant_access()'"
#                 }
#             ]
#         )
        
#         print("--- Claude's Response ---")
#         # FIX: Access the first element of the list, then grab its text property
#         print(response.content[0].text)
        
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     ask_claude()

import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

# Initialize client
client = Anthropic()

def stream_audit():
    prompt = "Write a comprehensive essay on BRICS 2026 summit, focusing on its geopolitical implications and economic strategies. Ensure the essay is well-structured, with an introduction, body, and conclusion. Use formal language and provide in-depth analysis."
    
    print("🤖 Claude is thinking... Streaming response below:\n")
    print("--- Claude's Live Response ---")
    
    try:
        # Open a secure streaming context using an active model
        with client.messages.stream(
            model="claude-sonnet-5",
            max_tokens=1500,
            system="You are an elite Geopolitics expert. Be brief and informative.",
            messages=[{"role": "user", "content": prompt}]
        ) as stream:
            # text_stream yields strings token-by-token in real time
            for text in stream.text_stream:
                print(text, end="", flush=True)
                
        print("\n\n--- Stream Completed Successfully ---")
        
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    stream_audit()
