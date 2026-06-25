import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.resizable(True, True)
root.configure(bg= "#2c3c4d")
root.grid_columnconfigure(0,weight=1)


input_frame = tk.Frame(root,bg="#2c3c4d")
input_frame.grid(row=0,column=0,sticky="n")

weight_label = tk.Label(input_frame, text="Weight (kg)",bg="#2c3c4d",fg="white",font = ("Consolas",15,"bold"))
weight_label.grid(row=0,column=0,padx=10,pady=20,sticky="w")
weight_entry = tk.Entry(input_frame,font = ("Consolas",15,"bold"),width=15)
weight_entry.grid(row=0,column=1)


height_label = tk.Label(input_frame, text="Height (m)",bg="#2c3c4d",fg="white",font = ("Consolas",15,"bold"))
height_label.grid(row=1,column=0,padx=10,pady=20,sticky="w")
height_entry = tk.Entry(input_frame,font = ("Consolas",15,"bold"),width=15)
height_entry.grid(row=1,column=1)


output_frame = tk.Frame(root,bg="#2c3c4d")
output_frame.grid(row=1,column=0,sticky="n" )

result_label = tk.Label(output_frame,text="BMI:",font = ("Consolas",18,"bold"),fg="white",bg="#2c3c4d")
result_label.grid(row=1,column=0)


import csv
import os

BASE_DIR = os.path.dirname(__file__)
CSV_FILE = os.path.join(BASE_DIR, "bmi_history.csv")
def create_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE,"w",newline="") as file:
            writer=csv.writer(file)
            writer.writerow([
                "Date",
                "Weight",
                "Height",
                "BMI",
                "Category"
                ]
            )

from datetime import datetime

create_csv()

def save_history(weight,height,bmi,category):
        with open(CSV_FILE,"a",newline="") as file:
            date = datetime.now().strftime("%d/%m/%Y %H:%M")
            writer = csv.writer(file)
            writer.writerow([
                    date,
                             
                    f"{weight:.2f}",
                             
                    f"{height:.2f}",

                    f"{bmi:.2f}",

                    category,
                             
                    ]
                    
                )



def calculate_bmi():

    try:

        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if height<=0:
            raise ValueError
        if weight<=0:
            raise ValueError
        bmi = weight / (height ** 2)

    except ValueError:
        messagebox.showerror(
            "Error",
             "Weight and Height must be positive numbers."
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
        fg=color)
    save_history(weight,height,bmi,category)

    


def clear():
    weight_entry.delete(0,tk.END)
    height_entry.delete(0,tk.END)
    result_label.config(text="BMI:",fg="white")

def view_history():
    history_window = tk.Toplevel(root)
    history_window.title("BMI History")
    history_window.geometry("800x400")
    history_window.configure(bg="#2c3c4d")

    container = tk.Frame(history_window,bg="#2c3c4d")
    container.pack(fill="both", expand=True)

    scrollbar= tk.Scrollbar(container)
    
    text_box = tk.Text(
        container,
        width=80,
        height=20,
        bg="#2c3c4d",
        fg="white",
        font=("Consolas",12),
        yscrollcommand=scrollbar.set
        )
    
    text_box.pack(in_=container, side="left", fill="both", expand=True)
    scrollbar.pack(in_=container, side="right", fill="y")
    scrollbar.config(command=text_box.yview)
  
    
    # text_box.insert(tk.END, "DATE\t\tWEIGHT HEIGHT\tBMI\tCATEGORY\n\n")  
    #{"DATE":20}     --->Put the date here and reserve 20 characters for it.
    text_box.insert(
    tk.END,
    f"{'DATE':<20}{'WEIGHT':<10}{'HEIGHT':<10}{'BMI':<10}{'CATEGORY':<15}\n\n"
    )


    with open(CSV_FILE,"r") as file:
        reader = csv.reader(file)
        next(reader,None)
        # for row in reader:
        #     text_box.insert(tk.END," \t".join(row)+"\n")
        for row in reader:

            text_box.insert(
            tk.END,

                f"{row[0]:<20}"
                f"{row[1]:<10}"
                f"{row[2]:<10}"
                f"{row[3]:<10}"
                f"{row[4]:<15}\n"
            )
    text_box.config(state="disabled")

button = tk.Button(
    output_frame,
    text="Calculate BMI",
    font = ("Consolas",14,"bold"),
    fg= "#FFFFFF",
    bg = "#4859DD",
    cursor="hand2",
    command=calculate_bmi
)
button.grid(row=0,column=0,pady=10)


clear_button = tk.Button(
    output_frame,
    text="CLEAR ALL",
    font = ("Consolas",14,"bold"),
    fg= "#FFFFFF",
    bg = "#4859DD",
    cursor="hand2",
    command=clear
)
clear_button.grid(row=2,column=0,pady=10)

history_button = tk.Button(
    output_frame,
    text="VIEW HISTORY",
    font = ("Consolas",14,"bold"),
    fg= "#FFFFFF",
    bg = "#4859DD",
    cursor="hand2",
    command=view_history
    
)
history_button.grid(row=3,column=0)

root.mainloop() 
