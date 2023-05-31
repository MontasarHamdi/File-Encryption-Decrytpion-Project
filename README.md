# FILE ENCRYPTION/DECRYPTION USING AES ALGORITHM

This implementation provides a basic understanding of file encryption and decryption using AES in Python. 
For production use, consider additional security measures and error handling.

Steps:
Step 1: Import Libraries
- from cryptography.fernet import Fernet
- getpass
- import os

Step 2: login System
- Use getpass to create login system.

Step 3: Generate Encryption Key
- Generate secure encryption key that will be used for decryption/encryption

Step 4: Load Encryption Key
- Load the encryption key from the key file.

Step 5: Encrypt File
- Encrypt a file using the loaded encryption key.

Step 6: Decrypt File
- Decrypt an encrypted file using the loaded encryption key.


