from speech import listen, speak

from utils import (
    tell_time,
    tell_date,
    search_wiki,
    google_search,
    open_google,
    open_youtube,
    open_repository
)


def process_command(root):

    command = listen()

    if any(word in command for word in ["hello", "hi", "hey"]):
        speak("Hi, how can I help you?")

    elif "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "").strip()
        search_wiki(topic)

    elif "youtube" in command:
        open_youtube()

    elif "search" in command:
        query = command.replace("search", "").strip()
        speak(f"Searching for {query}")
        google_search(query)

    elif "open google" in command:
        speak("Opening Google")
        open_google()

    elif "my repository" in command:
        open_repository()

    elif "bye" in command:
        speak("Goodbye")
        root.destroy()

    else:
        speak("Sorry, I can't do that yet.")