import tkinter as tk

# Add task function
def add_task():
    task = task_entry.get()
    if task.strip() != "":   # check empty task
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)  # clear entry box

# Delete task function
def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

# Clear all function
def clear_all():
    listbox.delete(0, tk.END)

# Window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.configure(bg="black")

# Entry
task_entry = tk.Entry(root, width=25, font=("Arial", 14))
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task, bg="light green")
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="red")
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All", command=clear_all, bg="orange")
clear_button.pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=30, height=10, font=("Arial", 12))
listbox.pack(pady=10)

root.mainloop()
