# ===== PYTHON SCRIPT FOR FILE ENCRYPTION/DECRYPTION ===== #

# import necessary libraries and os for file operations
from cryptography.fernet import Fernet
import getpass
import os


# Create function to generate a random key for encryption/decryption
def generate_key():
    # use Fernet, a high level encryption interface
    key = Fernet.generate_key()
    # write the random key to a file named encryption_key.key
    with open('encryption_key.key', 'wb') as key_file:
        key_file.write(key)


# only need to generate key once
generate_key()


# login system
def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    # for the purpose of this project, the username and password are already set.
    # Ideal practice is to store and validate username and password in database
    if username == "admin" and password == "password":
        return True
    else:
        return False


# Prompt for login
while not login():
    print("Invalid username or password. Please try again.")
print("Login successful!")


# Create a function to load the encryption key from the key file.
def load_key():
    # This function reads from the encryption key file
    return open('encryption_key.key', 'rb').read()


# Create function to encrypt file
def encrypt_file(filename, key):
    fernet = Fernet(key)
    # read contents of the file and store it in file_data
    with open(filename, 'rb') as file:
        file_data = file.read()
    # encrypt using the advanced encryption standard algorithm (AES)
    encrypt_data = fernet.encrypt(file_data)

    # save the new encrypted data to a new file with the .encrypted extension
    with open(filename + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypt_data)
    # Remove the original unencrypted file for security purposes
    os.remove(filename)


# create function to decrypt file
def decrypt_file(filename, key):
    fernet = Fernet(key)
    # read encrypted file and save it to variable
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    # decrypt it using AES and save it to decrypted data variable
    decrypted_data = fernet.decrypt(encrypted_data)

    # save decrypted variable to new file
    with open(filename[:-10], 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    # remove encrypted file for security purposes
    os.remove(filename)


# ===== usage of functions ===== #

# load encryption key
key = load_key()
# Encrypt a file - replace dummyfile.txt with your own file  # noqa
encrypt_file("dummyfile.txt", key)  # noqa
# decrypt and encrypted file
decrypt_file("dummyfile.txt.encrypted", key)  # noqa
