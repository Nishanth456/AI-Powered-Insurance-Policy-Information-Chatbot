import streamlit as st
from chatbot import ask_chatbot, fallback_to_human_agent, match_keywords, escalation_keywords
import json
import os

HISTORY_FILE = "chat_history_streamlit.json"

# Load previous chat history (optional)
def load_chat_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

# Save current chat history
def save_chat_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

# Page setup
st.set_page_config(page_title="SBI Home Insurance Chatbot", page_icon="💬")
st.title("💬 SBI Home Insurance Chatbot")
st.markdown("Ask me anything about the SBI Home Insurance Policy.")

# Initialize chat history in session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = load_chat_history()

# User input box
user_input = st.chat_input("Type your question here...")

if user_input:
    # Escalation check
    fallback_triggered = False
    for issue, keyword_sets in escalation_keywords.items():
        if match_keywords(user_input.lower(), keyword_sets):
            response = fallback_to_human_agent(user_input, issue if issue != 'human' else None)
            fallback_triggered = True
            break

    # Get bot response
    if fallback_triggered:
        bot_response = response
    else:
        bot_response = ask_chatbot(user_input)

    # Store in session and save
    st.session_state.chat_history.append({"user": user_input, "bot": bot_response})
    save_chat_history(st.session_state.chat_history)

# Display full chat history
for message in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(message["user"])
    with st.chat_message("assistant"):
        st.markdown(message["bot"])
