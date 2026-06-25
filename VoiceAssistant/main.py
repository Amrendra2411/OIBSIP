import pyttsx3
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("600x400")
root.configure(bg="#2c3c4d")
root.grid_columnconfigure(0, weight=1)
container = tk.Frame(root,bg="#2c3c4d")
container.grid(row=0,column=0)



tk.Label(container,text="VOICE ASSISTANT\n HELLO USER!",
         font = ("Consolas",30,"bold"),bg="#2c3c4d",fg="white").grid(row=0,column=0,pady=20)

Assistant_label=tk.Label(container,text="Assistant: Click the button to speak.",
                        font = ("Consolas",20,"bold"),bg="#2c3c4d",fg="white")
Assistant_label.grid(row=2,column=0,pady=20)


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


speak("Hello User")
speak("Click the button to speak.")



import speech_recognition as sr


def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        # Assistant_label.config(text="Listening..")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)


    try:

        command = recognizer.recognize_google(audio)

        print("You said:", command)

        return command.lower()


    except:

        return ""

from datetime import datetime

def tell_time():

    current = datetime.now().strftime("%H:%M")
    
    speak(f"The time is {current}")


def tell_date():

    today = datetime.now().strftime("%d %B %Y")
    
    speak(today)

import wikipedia
def search_wiki(query):

    result = wikipedia.summary(query, sentences=2)
    
    speak(result)


import webbrowser
import urllib.parse

def google_search(query):
    query = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={query}"
    
    webbrowser.open(url)

def button():
   
    command = listen()
  

    if any(word in command for word in ["hello", "hi", "hey"]):
       print("Assistant: Hi, How can I help you?")
       speak(" Hi, How can I help you?")
    
    elif "time" in command:
        tell_time()
    
    elif "date" in command:
        tell_date()

    elif "wikipedia" in command:
       
        topic = command.replace("wikipedia","")
        search_wiki(topic)
    elif "youtube" in command:

        webbrowser.open("https://youtube.com")

    elif "google" in command:

         webbrowser.open("https://google.com")
    elif "my repository" in command:

         webbrowser.open("https://github.com/Amrendra2411/")

    elif "search" in command:
        query = command.replace("search", "").strip()
        speak(f"Searching for {query}")
        google_search(query)

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")


    elif "bye" in command:
        print("Assistant: Byeee Byee")
        
        speak("Byeee Byee")
        root.destroy()
    elif command==" ":
        speak("Empty command")
    else:
        speak("Sorry , I can't do that yet?")
tk.Button(container,text="Listen",font = ("Consolas",20,"bold"),
          fg="white",bg="#2c3c4d",command=button).grid(row=1,column=0,pady=20)

root.mainloop()

            