import tkinter as tk

def update_timer():
    global seconds
    seconds += 1
    label.config(text=str(seconds))
    root.after(1000, update_timer)  # 1000 ms = 1 second

root = tk.Tk()
root.title("Timer")

seconds = 0

label = tk.Label(root, text="0", font=("Arial", 30))
label.pack()

start_button = tk.Button(root, text="Start", command=update_timer)
start_button.pack()

root.mainloop()
