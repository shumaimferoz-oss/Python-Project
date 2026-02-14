import tkinter as tk
from tkinter import messagebox

# Function for calculation
def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = a + b
        elif operation == "Subtract":
            result = a - b
        elif operation == "Multiply":
            result = a * b
        elif operation == "Divide":
            if b != 0:
                result = a / b
            else:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
        else:
            result = "Select operation"

        result_label.config(text="Result: " + str(result))

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


# Window setup
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("350x250")

# Input fields
tk.Label(window, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(window)
entry1.pack(pady=5)

tk.Label(window, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack(pady=5)

# Operation dropdown
operation_var = tk.StringVar()
operation_var.set("Select Operation")  # default value

operations = ["Add", "Subtract", "Multiply", "Divide"]
tk.OptionMenu(window, operation_var, *operations).pack(pady=10)

# Calculate button
tk.Button(window, text="Calculate", command=calculate).pack(pady=10)

# Result label
result_label = tk.Label(window, text="Result: ")
result_label.pack(pady=10)

# Run the GUI
window.mainloop()

