#Created a Python password generator that generates strong passwords and stores them securely in a CSV file along
#with the associated service and username

import random
import string
import csv
import os

CSV_FILE = "saved_passwords.csv"

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lower + upper + digits + symbols

    # Ensure each password has at least one of each
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

def save_to_csv(service, username, password):
    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Service", "Username", "Password"])  # Header
        writer.writerow([service, username, password])
    print(f"✅ Saved to {CSV_FILE}")


def main():
    try:
        service = input("Enter the service name (e.g., Gmail, Facebook): ").strip()
        username = input("Enter your username or email: ").strip()
        length = int(input("Enter desired password length: "))

        password = generate_password(length)
        print(f"\n🔐 Your password for {service} is:\n{password}\n")

        save_to_csv(service, username, password)

    except ValueError as ve:
        print(f"❌ Error: {ve}")

if __name__ == "__main__":
    main()

#######################################################################################################################
