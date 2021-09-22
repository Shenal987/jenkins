# Decryption Script
from cryptography.fernet import Fernet

key = ''
print("Key : %s", key)

input_file = 'encrypted/config.ini'
output_file = 'plain-text/config.ini'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)