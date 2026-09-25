import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Bootstrapping environment variables from .env file
load_dotenv()

def main():
    if not os.getenv("ANTHROPIC_API_KEY"):
        raise ValueError("CRITICAL: ANTHROPIC_API_KEY not found in environment or .env file.")

    llm = ChatAnthropic(model="claude-sonnet-4-5", temperature=0.7)

    # 1. Construct the Stateful Prompt Layout
    # MessagesPlaceholder dynamically injects the chat message array into the prompt.
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an elite SEO content editor helping to refine structural outlines."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{user_input}")
    ])

    # The baseline pipeline remains completely stateless
    stateless_chain = chat_prompt | llm | StrOutputParser()

    # 2. Setup the Memory Storage Layer
    # An ephemeral dictionary simulation of a real database tracking isolated user sessions
    session_database = {}

    def get_session_history(session_id:   str) -> InMemoryChatMessageHistory:
        """Retrieves or creates a fresh history bucket for a unique user session ID."""
        if session_id not in session_database:
            session_database[session_id] = InMemoryChatMessageHistory()
        return session_database[session_id]

    # 3. Wrap the Chain with State Management Orchestration
    stateful_session_chain = RunnableWithMessageHistory(
        stateless_chain,
        get_session_history,
        input_messages_key="user_input",
        history_messages_key="chat_history"
    )

    # =========================================================================
    # MULTI-TURN CONVERSATION EXECUTION DEMO
    # =========================================================================
    # Declaring a unique tracker ID for this user session
    config_session_1 = {"configurable": {"session_id": "seo_editor_session_995"}}

    print("--- Turn 1: Passing contextual outline information ---")
    turn_1_input = "I am writing a blog outline about Kubernetes. Can you suggest 3 catchy titles?"
    print(f"User: {turn_1_input}")
    
    response_1 = stateful_session_chain.invoke(
        {"user_input": turn_1_input}, 
        config=config_session_1
    )
    print(f"AI: {response_1}\n")

    print("--- Turn 2: Verifying active session memory retrieval ---")
    # The prompt below explicitly checks if the model remembers what the topic is without re-stating it
    turn_2_input = "Give me two more options, but ensure they include the word 'Secrets' and focus on the same topic."
    print(f"User: {turn_2_input}")
    
    response_2 = stateful_session_chain.invoke(
        {"user_input": turn_2_input}, 
        config=config_session_1
    )
    print(f"AI: {response_2}\n")

    print("--- Turn 3: Isolated Session Verification (Testing Multi-tenant separation) ---")
    # Setting up a completely different user session ID to prove isolation
    config_session_2 = {"configurable": {"session_id": "different_user_session_abc"}}
    turn_3_input = "What topic was I working on earlier?"
    print(f"User (Session 2): {turn_3_input}")
    
    response_3 = stateful_session_chain.invoke(
        {"user_input": turn_3_input}, 
        config=config_session_2
    )
    print(f"AI (Session 2): {response_3}")
    print("*(Notice that Session 2 has no access to Session 1's Kubernetes data.)*")

if __name__ == "__main__":
    main()
