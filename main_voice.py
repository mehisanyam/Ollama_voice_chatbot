import speech_recognition as sr
import pyaudio
import os
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice' , voices[1].id)

template = """
Answer the question below.

Here is the coversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model = "orion")
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
    # r.energy_threshold()
        print("Say anything : ")
        audio= r.listen(source)
        try:
            query = r.recognize_google(audio)
            print(f"You said: {query}\n")
        except Exception as e:
            print("Sorry, I could not understand. Could you please say that again?")  
            return "quit"
    return query

if __name__ == "__main__":
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    while True:
        context = ""
        query = takeCommand().lower()
        
        if 'quit' in query or 'stop it' in query or 'stop' in query:
            break
        print("Thinking...\n")
        result = chain.invoke({"context": context, "question": query})
        print("Orion 1.0: ",result)
        speak(result)
        context += f"\nUser: {query}\nAI: {result}"