
### **Code Snippet (passvault.py)**

import os
import base64
import json
from cryptography.fernet import Fernet

# Generate or load encryption key
KEY_FILE = "key.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    return open(KEY_FILE, "rb").read()

if not os.path.exists(KEY_FILE):
    generate_key()

cipher = Fernet(load_key())

def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()

def save_passwords(data):
    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)

def load_passwords():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            return json.load(file)
    return {}

# Example Usage
passwords = load_passwords()
email = "myemail@example.com"
passwords[email] = encrypt_password("MySecurePassword!")
save_passwords(passwords)

# Retrieve password
print("Decrypted Password:", decrypt_password(passwords[email]))
