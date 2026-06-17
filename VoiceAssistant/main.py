import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


speak("Hello Amrendra, I am your assistant.")



import speech_recognition as sr


def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

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

while True:
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
        break
    elif command==" ":
        speak("Empty command")
    else:
        speak("Sorry , I can't do that yet?")

            