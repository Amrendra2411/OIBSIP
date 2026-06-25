import tkinter as tk
from tkinter import messagebox
import random
import string

root = tk.Tk()

root.title("Password Generator")
root.geometry("550x250")
root.resizable(True,True)
root.configure(bg="#7db0e6")


input_frame = tk.Frame(root,bg="#7db0e6")
input_frame.grid(row=0,column=0,sticky="ew")

output_frame = tk.Frame(root,bg="#7db0e6")
output_frame.grid(row=1,column=0)

length_label = tk.Label(input_frame,text="Password Length",font = ("Consolas",15,"bold"),fg= "black",bg="#7db0e6")
length_label.grid(row=0,column=0,padx= 10,pady=10)

length_entry = tk.Entry(input_frame,font = ("Consolas",15,"bold"))
length_entry.grid(row=0,column=1,padx=10,pady=10)



#Uppercase
uppercase = tk.BooleanVar()
tk.Checkbutton(
        input_frame,
        text="Uppercase",
        variable=uppercase,
        font = ("Consolas",15,"bold"),
        cursor="hand2",
        bg="#7db0e6"
).grid(row= 1,column=0)

#numbers
numbers = tk.BooleanVar()
tk.Checkbutton(
        input_frame,
        text="Numbers",
        variable=numbers,
        font = ("Consolas",15,"bold"),
        cursor="hand2",
        bg="#7db0e6"
).grid(row=1,column=1)

#symbols
symbols = tk.BooleanVar()
tk.Checkbutton(
        input_frame,
        text="Symbols",
        variable=symbols,
        font = ("Consolas",15,"bold"),
        cursor="hand2",
        bg="#7db0e6"
        
).grid(row=1,column=2)


result = tk.Entry(

            output_frame,
            font = ("Consolas",15,"bold"),

            width=35

)

result.grid(row=0,column=0)


 

def generate_password():
    try:

        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error","Only integers are allowed")
            


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
    Message.config(text="PASSWORD GENERATED!",font = ("Consolas",15,"bold"),fg= "black",bg="#7db0e6")

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

            input_frame,

            text="Generate",
            font = ("Consolas",15,"bold"),
            width=20,
            cursor="hand2",
            command=generate_password

)
button.grid(row=2,column=1,pady=10)
copy_btn = tk.Button(

            output_frame,

            text="Copy",
            font = ("Consolas",15,"bold"),
            width=10,
            cursor="hand2",
            command=copy_password

)

copy_btn.grid(row=0,column=1,padx=10,pady=10)

Message = tk.Label(output_frame,text="",font = ("Consolas",15,"bold"),fg= "black",bg="#7db0e6")
Message.grid(row=1,column=0,columnspan=3 )


root.mainloop()