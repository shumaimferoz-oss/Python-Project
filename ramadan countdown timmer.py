import tkinter as tk
from datetime import datetime

#  Start Countdown
def calculate_countdown():
    global target_date
    year = int(Year_entry.get())
    month = int(Month_entry.get())
    date = int(Date_entry.get())
    

    target_date = datetime(year, month, date)
    update_timer()

#  Update Timer
def update_timer():
    now = datetime.now()
    remaining_time = target_date - now

    if remaining_time.total_seconds() > 0:
        days = remaining_time.days
        seconds = remaining_time.seconds

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        result_label.config(
            text=f"{days} Days {hours} Hours {minutes} Minutes {seconds} Seconds"
        )

        root.after(1000, update_timer)
    else:
        result_label.config(text="Time's Up!")

#🔹 Root
root = tk.Tk()
root.title("Ramadan Countdown Timer")
root.geometry("400x300")
root.configure(bg="black")

#  Frame
frame = tk.Frame(root, bg="darkgrey")
frame.pack(pady=30)

#  Year
tk.Label(frame, text="Enter Year", bg="darkgrey").pack()
Year_entry = tk.Entry(frame)
Year_entry.pack(padx=10, pady=10)

#  Month
tk.Label(frame, text="Enter Month", bg="darkgrey").pack()
Month_entry = tk.Entry(frame)
Month_entry.pack(padx=10, pady=10)

#  Day
tk.Label(frame, text="Enter Date", bg="darkgrey").pack()
Date_entry = tk.Entry(frame)
Date_entry.pack(padx=10, pady=10)

#  Button
tk.Button(frame, text="Start Countdown", bg="light blue",
          command=calculate_countdown).pack(pady=20)

#  Result
result_label = tk.Label(root, text="", bg="black",
                        fg="white", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
