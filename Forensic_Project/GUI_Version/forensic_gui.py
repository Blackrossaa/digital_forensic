import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib
import os

# Global variables to store hash and file
original_hash = None
selected_file = None

# Function to generate hash
def generate_hash():
    global original_hash, selected_file

    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    with open(file_path, "rb") as file:
        data = file.read()
        original_hash = hashlib.sha256(data).hexdigest()
        selected_file = file_path

    result_label.config(
        text="SHA-256 Hash Generated:\n" + original_hash
    )

# Function to verify integrity
def verify_integrity():
    if not selected_file or not original_hash:
        messagebox.showwarning(
            "Warning",
            "Please generate a hash first."
        )
        return

    with open(selected_file, "rb") as file:
        data = file.read()
        current_hash = hashlib.sha256(data).hexdigest()

    if current_hash == original_hash:
        messagebox.showinfo(
            "Integrity Status",
            "✔ File integrity preserved.\nNo modification detected."
        )
    else:
        messagebox.showerror(
            "Integrity Alert",
            "⚠ File has been modified!\nIntegrity compromised."
        )

# Create window
window = tk.Tk()
window.title("Digital Forensic File Integrity Tool (GUI)")
window.geometry("500x350")

title = tk.Label(
    window,
    text="Digital Forensic File Integrity Tool",
    font=("Arial", 16)
)
title.pack(pady=10)

btn_hash = tk.Button(
    window,
    text="Select File & Generate Hash",
    command=generate_hash
)
btn_hash.pack(pady=10)

btn_verify = tk.Button(
    window,
    text="Verify File Integrity",
    command=verify_integrity
)
btn_verify.pack(pady=10)

result_label = tk.Label(
    window,
    text="",
    wraplength=450
)
result_label.pack(pady=10)

window.mainloop()
