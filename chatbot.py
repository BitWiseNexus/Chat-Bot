from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import os
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(google_api_key=os.getenv("GOOGLE_API_KEY"), model="gemini-2.5-flash")

chat_history=[
    SystemMessage(content="You are a helpful assistant")
]

while(True):
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("Bot: ",result.content)

