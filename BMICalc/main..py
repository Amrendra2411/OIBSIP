import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("BMI Calculator")
root.geometry("400x300")
root.resizable(True, True)
root.configure(bg= "#2c3c4d")
root.grid_columnconfigure(0,weight=1)

input_frame = tk.Frame(root,bg="#2c3c4d")
input_frame.grid(

row=0,

column=0,

sticky="n"
)

weight_label = tk.Label(

    input_frame, 

    text="Weight (kg)",

    bg="#2c3c4d",
    
    fg="white",

    font = ("Calibri",15,"bold")

    )

weight_label.grid(row=0,column=0,padx=10,pady=20,sticky="w")

weight_entry = tk.Entry(input_frame,font = ("Calibri",15,"bold"),width=15)
weight_entry.grid(row=0,column=1)


height_label = tk.Label(
    input_frame, 

    text="Height (m)",

    bg="#2c3c4d",
    
    fg="white",

    font = ("Calibri",15,"bold")

    )

height_label.grid(row=1,column=0,padx=10,pady=20,sticky="w")

height_entry = tk.Entry(input_frame,font = ("Calibri",15,"bold"),width=15)

height_entry.grid(row=1,column=1)


output_frame = tk.Frame(root,bg="#2c3c4d")
output_frame.grid(row=1,column=0,sticky="n" )

result_label = tk.Label(
    output_frame,
    text="BMI:",
    font = ("Calibri",18,"bold"),
    fg="white",
    bg="#2c3c4d"
)

result_label.grid(row=1,column=0)


def calculate_bmi():

    try:

        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi = weight / (height ** 2)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid numbers."
        )
        return
    color = "white"

    if bmi < 18.5:
        category = "Underweight"
        color="yellow"

    elif bmi < 25:
        category = "Normal"
        color="green"

    elif bmi < 30:
        category = "Overweight"
        color="orange"

    else:
        category = "Obese"
        color="red"

    result_label.config(
        text=f"BMI: {bmi:.2f}\nCategory: {category}",
        fg=color

    )


button = tk.Button(
    output_frame,
    text="Calculate BMI",
    font = ("Calibri",14,"bold"),
    fg= "#FFFFFF",
    bg = "#4859DD",
    cursor="hand2",
    command=calculate_bmi
)
def clear():
    weight_entry.delete(0,tk.END)
    height_entry.delete(0,tk.END)
    result_label.config(text="BMI",fg="white")

button.grid(row=0,column=0,pady=10)
clear_button = tk.Button(
    output_frame,
    text="CLEAR ALL",
    font = ("Calibri",14,"bold"),
    fg= "#FFFFFF",
    bg = "#4859DD",
    cursor="hand2",
    command=clear
)
clear_button.grid(row=3,column=0,pady=10)


root.mainloop() 