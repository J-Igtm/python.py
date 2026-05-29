# Simple Facebook Style UI using Python Tkinter
# Save as facebook_clone.py and run:
# python facebook_clone.py

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Facebook Clone")
root.geometry("900x600")
root.config(bg="#f0f2f5")

# =========================
# HEADER
# =========================
header = tk.Frame(root, bg="#1877f2", height=60)
header.pack(fill="x")

logo = tk.Label(
    header,
    text="facebook",
    fg="white",
    bg="#1877f2",
    font=("Arial", 24, "bold")
)
logo.pack(side="left", padx=20, pady=10)

search = tk.Entry(header, font=("Arial", 14), width=30)
search.pack(side="left", pady=15)

# =========================
# LEFT MENU
# =========================
left_menu = tk.Frame(root, bg="white", width=200)
left_menu.pack(side="left", fill="y")

menu_title = tk.Label(
    left_menu,
    text="Menu",
    font=("Arial", 18, "bold"),
    bg="white"
)
menu_title.pack(pady=20)

buttons = ["Home", "Friends", "Messages", "Videos", "Marketplace", "Logout"]

for item in buttons:
    btn = tk.Button(
        left_menu,
        text=item,
        font=("Arial", 14),
        width=18,
        bg="#e4e6eb",
        relief="flat"
    )
    btn.pack(pady=8)

# =========================
# MAIN FEED
# =========================
feed = tk.Frame(root, bg="#f0f2f5")
feed.pack(side="left", fill="both", expand=True)

post_box = tk.Frame(feed, bg="white", bd=1, relief="solid")
post_box.pack(pady=20, padx=20, fill="x")

post_entry = tk.Text(post_box, height=4, font=("Arial", 14))
post_entry.pack(padx=10, pady=10, fill="x")

posts_frame = tk.Frame(feed, bg="#f0f2f5")
posts_frame.pack(fill="both", expand=True)

def create_post():
    text = post_entry.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Write something first!")
        return

    post_card = tk.Frame(posts_frame, bg="white", bd=1, relief="solid")
    post_card.pack(padx=20, pady=10, fill="x")

    user = tk.Label(
        post_card,
        text="👤 User",
        font=("Arial", 12, "bold"),
        bg="white"
    )
    user.pack(anchor="w", padx=10, pady=5)

    content = tk.Label(
        post_card,
        text=text,
        font=("Arial", 13),
        bg="white",
        wraplength=500,
        justify="left"
    )
    content.pack(anchor="w", padx=10, pady=5)

    like_btn = tk.Button(
        post_card,
        text="👍 Like",
        bg="#e4e6eb",
        relief="flat"
    )
    like_btn.pack(side="left", padx=10, pady=10)

    comment_btn = tk.Button(
        post_card,
        text="💬 Comment",
        bg="#e4e6eb",
        relief="flat"
    )
    comment_btn.pack(side="left", padx=5)

    share_btn = tk.Button(
        post_card,
        text="↗ Share",
        bg="#e4e6eb",
        relief="flat"
    )
    share_btn.pack(side="left", padx=5)

    post_entry.delete("1.0", tk.END)

post_button = tk.Button(
    post_box,
    text="Post",
    font=("Arial", 12, "bold"),
    bg="#1877f2",
    fg="white",
    command=create_post
)
post_button.pack(pady=10)

# =========================
# RIGHT PANEL
# =========================
right_panel = tk.Frame(root, bg="white", width=220)
right_panel.pack(side="right", fill="y")

contacts_title = tk.Label(
    right_panel,
    text="Contacts",
    font=("Arial", 18, "bold"),
    bg="white"
)
contacts_title.pack(pady=20)

friends = ["Aman", "Rahul", "Priya", "Neha", "Karan"]

for friend in friends:
    lbl = tk.Label(
        right_panel,
        text="🟢 " + friend,
        font=("Arial", 14),
        bg="white"
    )
    lbl.pack(anchor="w", padx=20, pady=5)

root.mainloop()