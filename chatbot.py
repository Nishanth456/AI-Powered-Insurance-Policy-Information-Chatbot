import os
from dotenv import load_dotenv
from groq import Groq
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import json

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=groq_api_key)

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
db = FAISS.load_local("vector_store", embeddings=embedding, allow_dangerous_deserialization=True)

chat_history = []

# Fallback function to connect to a human agent
def fallback_to_human_agent(query, issue=None):
    if issue:
        return f"Connecting you to a human agent for assistance with the {issue} process. Kindly wait for a response."
    return "I'm unable to provide a satisfactory answer. Redirecting you to a human agent. Please wait."

# Chatbot function with history context
def ask_chatbot(query, first_interaction=False):
    history_context = ""
    for entry in chat_history:
        history_context += f"User: {entry['user']}\nChatbot: {entry['bot']}\n"

    history_context += f"User: {query}\nChatbot:"

    prompt = f"""
    You are an AI-powered assistant representing SBI's Home Insurance Policy.
    Your job is to help users by answering their questions about the SBI Home Insurance Policy.
    Be clear, concise, and structured in your responses.
    Answer only based on the provided context. If insufficient, guide the user to contact support.

    {history_context}
    """
    
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    chatbot_response = response.choices[0].message.content.strip()
    chat_history.append({"user": query, "bot": chatbot_response})
    return chatbot_response

# Define escalation intent keywords
escalation_keywords = {
    "application": [["how", "apply"], ["application", "process"], ["apply", "policy"], ["get", "policy"]],
    "claim": [["claim", "process"], ["how", "claim"], ["file", "claim"], ["processing", "time"], ["steps", "claim"]],
    "frustration": [["not", "helping"], ["not", "useful"], ["don’t", "understand"], ["wasting", "time"], ["not", "working"], ["not", "answering"]],
    "human": [["connect", "human"], ["talk", "human"], ["need", "help"], ["speak", "agent"]]
}

def match_keywords(user_input, keyword_sets):
    return any(all(word in user_input for word in keywords) for keywords in keyword_sets)

# For testing
if __name__ == "__main__":
    print("\nChatbot: Hello! I am an AI-powered assistant for SBI Home Insurance Policy. How can I assist you today?")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["exit", "quit", "end"]:
            break

        # Check for escalation triggers
        fallback_triggered = False
        for issue, keyword_sets in escalation_keywords.items():
            if match_keywords(user_input.lower(), keyword_sets):
                response = fallback_to_human_agent(user_input, issue if issue != 'human' else None)
                print(f"\nChatbot: {response}")
                
                chat_history.append({"user": user_input, "bot": response})
                fallback_triggered = True
                break

        if fallback_triggered:
            continue

        # Get Chatbot response
        answer = ask_chatbot(user_input)
        print(f"\nChatbot: {answer}")

    # Saving the chat history to a file at the end
    with open("chat_history.json", "w") as f:
        json.dump(chat_history, f, indent=4)


