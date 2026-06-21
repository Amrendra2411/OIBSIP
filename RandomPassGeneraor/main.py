import tkinter as tk
from tkinter import messagebox
import random
import string

root = tk.Tk()

root.title("Password Generator")
root.geometry("400x350")
root.resizable(True,True)

length_label = tk.Label(root,text="Password Length")
length_label.pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack()



#Uppercase
uppercase = tk.BooleanVar()
tk.Checkbutton(
        root,
        text="Uppercase",
        variable=uppercase
).pack()

#numbers
numbers = tk.BooleanVar()
tk.Checkbutton(
        root,
        text="Numbers",
        variable=numbers
).pack()

#symbols
symbols = tk.BooleanVar()
tk.Checkbutton(
        root,
        text="Symbols",
        variable=symbols
).pack()


result = tk.Entry(

            root,

            width=35

)

result.pack()




def generate_password():

    length = int(length_entry.get())


    chars = string.ascii_lowercase


    if uppercase.get():
        chars += string.ascii_uppercase


    if numbers.get():
        chars += string.digits


    if symbols.get():
        chars += string.punctuation


    password = ''.join(

        random.choice(chars)

        for _ in range(length)

    )


    result.delete(0,tk.END)  #to delete the previous password

    result.insert(0,password)

def copy_password():

    root.clipboard_clear()

    root.clipboard_append(

                result.get()

    )


    messagebox.showinfo(

        "Copied",

        "Password copied"

    )

button = tk.Button(

            root,

            text="Generate",

            command=generate_password

)
button.pack(pady=10)
copy_btn = tk.Button(

            root,

            text="Copy",

            command=copy_password

)

copy_btn.pack(pady=5)


root.mainloop()