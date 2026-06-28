from datetime import datetime
import wikipedia
import webbrowser
import urllib.parse

from speech import speak


def tell_time():
    current = datetime.now().strftime("%H:%M")
    speak(f"The time is {current}")


def tell_date():
    today = datetime.now().strftime("%d %B %Y")
    speak(today)


def search_wiki(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except:
        speak("Sorry, I couldn't find anything.")


def google_search(query):
    query = urllib.parse.quote(query)
    webbrowser.open(f"https://www.google.com/search?q={query}")


def open_google():
    webbrowser.open("https://www.google.com")


def open_youtube():
    webbrowser.open("https://www.youtube.com")


def open_repository():
    webbrowser.open("https://github.com/Amrendra2411/")