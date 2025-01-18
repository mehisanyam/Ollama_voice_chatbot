from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the coversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model = "orion")
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

# def handle_conv():
#     context = ""
#     print("Welcome to the AI chatbot! Type 'exit' to quit")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == "exit":
#             break

#         result = chain.invoke({"context": context, "question": user_input})
#         print("Orion 1.0: ",result)
#         context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    # handle_conv()
    while True:
        context = ""
        query = input("You: ")
        if query.lower() == "exit":
            break
        print("Thinking...\n")
        result = chain.invoke({"context": context, "question": query})
        print("Orion 1.0: ",result)
        context += f"\nUser: {query}\nAI: {result}"
