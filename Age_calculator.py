import tkinter as tk
from datetime import datetime

#FUNCTION:
def calculate_age():
    birth_year=int(entry.get())
    current_year=datetime.now().year
    age=current_year-birth_year
    result_label.config(text=f"Your age is {age}")

#ROOT:
root=tk.Tk()
root.title("Age calculator")
root.geometry("400x300")
root.configure(bg="lightblue")
root.resizable(False,False)
root.attributes("-topmost",True)

#LABEL:
label=tk.Label(root,text="Enter your birth year:",bg="lightblue")
label.pack()

#ENTRY:
entry=tk.Entry(root)
entry.pack()

#BUTTON:
button=tk.Button(root,text="calculate age",command=calculate_age)
button.pack()

#RESULT LABEL:
result_label=tk.Label(root,text="",bg="lightblue")
result_label.pack()
root.mainloop()