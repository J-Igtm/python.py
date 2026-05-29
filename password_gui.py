import tkinter as tk
import re

def check_password():
    password = entry.get()

    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    number = re.search(r"[0-9]", password)
    special = re.search(r"[@#$%^&*!]", password)

    if length and upper and lower and number and special:
        result.config(text="Strong Password ✅")
    else:
        result.config(text="Weak Password ❌")

window = tk.Tk()
window.title("Password Strength Meter")
window.geometry("350x200")

label = tk.Label(window, text="Enter Password:")
label.pack(pady=10)

entry = tk.Entry(window, show="*", width=30)
entry.pack(pady=5)

button = tk.Button(window, text="Check Password", command=check_password)
button.pack(pady=10)

result = tk.Label(window, text="")
result.pack(pady=10)

window.mainloop()