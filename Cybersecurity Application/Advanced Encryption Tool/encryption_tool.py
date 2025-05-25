import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
import base64
import hashlib
import os

# Function to select a file
def select_file():
    file_path.set(filedialog.askopenfilename())

# Function to generate a key from password
def generate_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

# Encrypt the selected file
def encrypt_file():
    path = file_path.get()
    pwd = password.get()

    if not path or not pwd:
        messagebox.showwarning("Warning", "Please select a file and enter a password.")
        return

    key = generate_key(pwd)
    f = Fernet(key)

    try:
        with open(path, 'rb') as file:
            data = file.read()

        encrypted = f.encrypt(data)
        with open(path + ".enc", 'wb') as file:
            file.write(encrypted)

        messagebox.showinfo("Success", "File encrypted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed.\n{e}")

# Decrypt the selected file
def decrypt_file():
    path = file_path.get()
    pwd = password.get()

    if not path or not pwd:
        messagebox.showwarning("Warning", "Please select a file and enter a password.")
        return

    key = generate_key(pwd)
    f = Fernet(key)

    try:
        with open(path, 'rb') as file:
            data = file.read()

        decrypted = f.decrypt(data)

        new_path = path.replace(".enc", "")
        with open(new_path, 'wb') as file:
            file.write(decrypted)

        messagebox.showinfo("Success", "File decrypted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed.\n{e}")

# -------- UI Setup --------
root = tk.Tk()
root.title("Advanced Encryption Tool")
root.geometry("800x500")
root.resizable(False, False)

# Load and place background image
try:
    bg_image = Image.open("encryption_tool.png")
    bg_image = bg_image.resize((800, 500), Image.LANCZOS)
    bg = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"Background image couldn't be loaded: {e}")

# Transparent frame on top of background
frame = tk.Frame(root, bg="#f7f7f7", bd=0)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
title = tk.Label(frame, text="🔐 Secure File Encryptor", font=("Segoe UI", 18, "bold"), fg="#2e2e2e", bg="#f7f7f7")
title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

file_path = tk.StringVar()
password = tk.StringVar()

# File Selection
tk.Label(frame, text="No file selected", textvariable=file_path, bg="#f7f7f7", fg="#555", font=("Segoe UI", 9)).grid(row=1, column=0, columnspan=2)
tk.Button(frame, text="📁 Select File", command=select_file, bg="#3498db", fg="white", font=("Segoe UI", 10, "bold"), padx=10, pady=5).grid(row=2, column=0, columnspan=2, pady=10)

# Password input
tk.Label(frame, text="🔐 Enter Password", bg="#f7f7f7", fg="#333", font=("Segoe UI", 10, "bold")).grid(row=3, column=0, columnspan=2)
tk.Entry(frame, textvariable=password, show="*", font=("Segoe UI", 10), width=30).grid(row=4, column=0, columnspan=2, pady=5)

# Buttons
tk.Button(frame, text="🛡️ Encrypt File", command=encrypt_file, bg="#2ecc71", fg="white", font=("Segoe UI", 10, "bold"), padx=10, pady=5).grid(row=5, column=0, pady=20, padx=5)
tk.Button(frame, text="🔓 Decrypt File", command=decrypt_file, bg="#e74c3c", fg="white", font=("Segoe UI", 10, "bold"), padx=10, pady=5).grid(row=5, column=1, pady=20, padx=5)

# Footer
footer = tk.Label(root, text="Made  ❤  by Keerthana", font=("Segoe UI", 9), bg="#f7f7f7", fg="#666")
footer.pack(side="bottom", pady=10)

root.mainloop()
