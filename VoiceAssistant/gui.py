import tkinter as tk

from commands import process_command
from speech import speak


def create_gui():

    root = tk.Tk()

    root.title("Voice Assistant")
    root.geometry("600x400")
    root.configure(bg="#2c3c4d")

    container = tk.Frame(root, bg="#2c3c4d")
    container.pack(expand=True)

    tk.Label(
        container,
        text="VOICE ASSISTANT\nHELLO USER!",
        font=("Consolas", 30, "bold"),
        fg="white",
        bg="#2c3c4d"
    ).pack(pady=20)

    tk.Label(
        container,
        text="Assistant: Click the button to speak.",
        font=("Consolas", 18),
        fg="white",
        bg="#2c3c4d"
    ).pack(pady=10)

    tk.Button(
        container,
        text="🎤 Listen",
        font=("Consolas", 18, "bold"),
        command=lambda: process_command(root)
    ).pack(pady=30)

    speak("Hello User")
    speak("Click the button to speak.")

    root.mainloop()