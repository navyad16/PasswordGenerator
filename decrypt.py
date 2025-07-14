##########################################  Decrypt ################################################################

import csv
import os
from encrypt_utils import load_key, decrypt_message

CSV_FILE = "encrypted_passwords.csv"


def decrypt_passwords():
    if not os.path.exists(CSV_FILE):
        print("❌ Encrypted CSV file not found.")
        return
    if not os.path.exists("secret.key"):
        print("❌ Encryption key file not found.")
        return

    key = load_key()

    print("\n🔓 Decrypted Passwords:\n")

    with open(CSV_FILE, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                decrypted = decrypt_message(row["Encrypted Password"], key)
                print(f"Service: {row['Service']}\nUsername: {row['Username']}\nPassword: {decrypted}\n{'-' * 40}")
            except Exception as e:
                print(f"⚠️ Failed to decrypt one entry: {e}")


if __name__ == "__main__":
    decrypt_passwords()