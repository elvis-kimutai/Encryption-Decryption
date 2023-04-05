import tkinter as tk
import tkinter.filedialog as fd
from tkinter import ttk

import cryptography
from cryptography.fernet import Fernet

#generate a key for encryption and decryption
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key
def load_key():
    return open("key.key", "rb").read()

# Function to encrypt a file
def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

# Function to decrypt a file
def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

# Function to handle the "Encrypt" button click event
def on_encrypt_click():
    key = key_entry.get()
    filename = fd.askopenfilename(title="Select File to Encrypt")
    if filename:
        encrypt(filename, key)
        result_label.config(text="File encrypted successfully.")

# Function to handle the "Decrypt" button click event
def on_decrypt_click():
    key = key_entry.get()
    filename = fd.askopenfilename(title="Select File to Decrypt")
    if filename:
        decrypt(filename, key)
        result_label.config(text="File decrypted successfully.")

# Create the main window
root = tk.Tk()
root.title("File Encryption/Decryption")

# Set the background color to lavender
root.configure(bg="#E6E6FA")

# Create the key label and entry widget
key_label = tk.Label(root, text="Encryption/Decryption Key:")
key_label.pack()
key_entry = tk.Entry(root, show="*")
key_entry.pack()

# Create the "Encrypt" and "Decrypt" buttons
encrypt_button = tk.Button(root, text="Encrypt", command=on_encrypt_click, bg="#FFA07A", fg="white", font=("Arial", 16))
encrypt_button.pack(pady=50)
decrypt_button = tk.Button(root, text="Decrypt", command=on_decrypt_click, bg="#20B2AA", fg="white", font=("Arial", 16))
decrypt_button.pack(pady=50)

# Create the result label
result_label = tk.Label(root, text="")

root.mainloop()
