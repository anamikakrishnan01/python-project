import tkinter as tk
from tkinter import messagebox

def countdown(count):
    if count >= 0:
        mins, secs = divmod(count, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        label.config(text=time_format)
        root.after(1000, countdown, count - 1)
    else:
        messagebox.showinfo("Time's up", "Countdown finished!")

def start_timer():
    try:
        total_seconds = int(entry.get())
        if total_seconds < 0:
            raise ValueError
        countdown(total_seconds)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number of seconds")

# Main window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("300x200")

# Input field
entry = tk.Entry(root, justify="center", font=("Arial", 14))
entry.pack(pady=10)
entry.insert(0, "Enter seconds")

# Label to display time
label = tk.Label(root, text="00:00", font=("Arial", 24))
label.pack(pady=10)

# Start button
start_button = tk.Button(root, text="Start", command=start_timer)
start_button.pack(pady=10)

root.mainloop()