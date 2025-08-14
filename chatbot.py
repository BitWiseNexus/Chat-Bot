from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import os
from dotenv import load_dotenv
import datetime

# Load environment variables
load_dotenv()

# Initialize model
model = ChatGoogleGenerativeAI(
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    model="gemini-2.5-flash"
)

# Chat history
chat_history = [
    SystemMessage(content="You are a helpful assistant")
]

# Log file for saving chat
log_file = f"chat_log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

print("🤖 ChatBot is running! Type 'exit' to quit.")
print("Type 'history' to view chat history, 'save' to save the conversation.")

while True:
    user_input = input("You: ").strip()

    if not user_input:
        continue

    # Exit
    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    # Show history
    if user_input.lower() == "history":
        print("\n📜 Chat History:")
        for msg in chat_history:
            role = "You" if isinstance(msg, HumanMessage) else "Bot" if isinstance(msg, AIMessage) else "System"
            print(f"{role}: {msg.content}")
        print()
        continue

    # Save chat to file
    if user_input.lower() == "save":
        with open(log_file, "w", encoding="utf-8") as f:
            for msg in chat_history:
                role = "You" if isinstance(msg, HumanMessage) else "Bot" if isinstance(msg, AIMessage) else "System"
                f.write(f"{role}: {msg.content}\n")
        print(f"💾 Chat saved to {log_file}")
        continue

    # Append user message and get AI response
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))

    # Print AI response
    print("Bot:", result.content)
