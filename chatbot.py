import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize model
model = ChatGoogleGenerativeAI(
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    model="gemini-2.5-flash"
)

# Streamlit page config
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 Simple AI Chatbot")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant")]

# Display chat history in chat-like UI
for msg in st.session_state.chat_history[1:]:  # skip system message
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# Chat input box (Enter to send)
if user_input := st.chat_input("Type your message..."):
    # Display user message
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get bot response
    result = model.invoke(st.session_state.chat_history)
    st.session_state.chat_history.append(AIMessage(content=result.content))

    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(result.content)
