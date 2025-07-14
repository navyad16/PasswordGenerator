# password_encrypted_generator.py
import os
import csv
import string
import random

from encrypt_utils import generate_key, load_key, encrypt_message

CSV_FILE = "encrypted_passwords.csv"

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_chars = lower + upper + digits + symbols

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

def save_encrypted_to_csv(service, username, password, key):
    file_exists = os.path.exists(CSV_FILE)
    encrypted_password = encrypt_message(password, key)

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Service", "Username", "Encrypted Password"])
        writer.writerow([service, username, encrypted_password])
    print(f"✅ Encrypted password saved to {CSV_FILE}")

def main():
    if not os.path.exists("secret.key"):
        generate_key()
        print("🔐 New encryption key generated and saved to secret.key")

    key = load_key()

    try:
        service = input("Enter the service name (e.g., Gmail): ").strip()
        username = input("Enter your username or email: ").strip()
        length = int(input("Enter desired password length: "))
        password = generate_password(length)

        print(f"\n🔑 Your password is: {password}")
        save_encrypted_to_csv(service, username, password, key)

    except ValueError as ve:
        print(f"❌ Error: {ve}")

if __name__ == "__main__":
    main()

