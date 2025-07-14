#Secure Password Generator with AES Encryption (Python) Developed a secure password generator that encrypts passwords
# using AES - based Fernet encryption and stores them in a CSV file.Encryption keys are securely managed for decryption when needed.

#pip install cryptography
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_message(message, key):
    return Fernet(key).encrypt(message.encode()).decode()

def decrypt_message(encrypted_message, key):
        return Fernet(key).decrypt(encrypted_message.encode()).decode()
