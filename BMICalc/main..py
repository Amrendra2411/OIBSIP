import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("BMI Calculator")
root.geometry("400x300")
root.resizable(True, True)


weight_label = tk.Label(root, text="Weight (kg)")
weight_label.pack(pady=5)

weight_entry = tk.Entry(root)
weight_entry.pack()


height_label = tk.Label(root, text="Height (m)")
height_label.pack(pady=5)

height_entry = tk.Entry(root)
height_entry.pack()


result_label = tk.Label(
    root,
    text="BMI:",
    font=("Arial",14)
)

result_label.pack()


def calculate_bmi():

    try:

        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi = weight / (height ** 2)

    except:
        messagebox.showerror(
            "Error",
            "Please enter valid numbers."
        )
        return


    if bmi < 18.5:
        category = "Underweight"

    elif bmi < 25:
        category = "Normal"

    elif bmi < 30:
        category = "Overweight"

    else:
        category = "Obese"

    result_label.config(
        text=f"BMI: {bmi:.2f}\nCategory: {category}"
    )


button = tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi
)

button.pack(pady=15)


root.mainloop()