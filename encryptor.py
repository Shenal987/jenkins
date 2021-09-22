# Encryption Script
from cryptography.fernet import Fernet

#key = Fernet.generate_key()
key = 'JKxOVROyEUfsMsON6-qf88EutwXN1f-0VCrjwVTPXQ4='
print("Key : %s", key)

input_file = './plain-text/config.ini'
output_file = './encrypted/config.ini'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)
