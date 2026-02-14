import tkinter as tk

#function
def calculator_bmi():
    weight=float(weight_entry.get())
    height=float(height_entry.get())
    height=height*height
    bmi=weight/(height)
    if bmi<=0:
        result_label.config(text="please enter valid input")
    result_label.config(text="Your BMI is :"+str(bmi))

#root setup
root=tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")

#weight input
weight_label=tk.Label(root,text="enter weight in kg")
weight_label.pack()
weight_entry=tk.Entry(root)
weight_entry.pack()

#height input
height_label=tk.Label(root,text="enter height in m")
height_label.pack()
height_entry=tk.Entry(root)
height_entry.pack()

#button
button=tk.Button(root,text="calculate BMI",command=calculator_bmi)
button.pack()

#result label
result_label=tk.Label(root,text="")
result_label.pack()
root.mainloop()