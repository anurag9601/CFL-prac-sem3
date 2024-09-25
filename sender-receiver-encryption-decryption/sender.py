#How encryption and decryption working

# from Crypto.Cipher import AES

# key = b"HEYIAMAKINGKEYAA"
# salt = b"HEYIAMAKINSALTA"

# cipher = AES.new(key, AES.MODE_EAX, salt)
# cipher_text = cipher.encrypt(b"Hey Abhinav")

# print(cipher_text)

# cipher = AES.new(key, AES.MODE_EAX , salt)
# print(cipher.decrypt(cipher_text))

import socket

from Crypto.Cipher import AES

key = b"HEYIAMAKINGKEYAA"
salt = b"HEYIAMAKINSALTA"

cipher = AES.new(key, AES.MODE_EAX , salt)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8080))

data = input("Enter the text here: ").encode("utf-8")

encrypted_data= cipher.encrypt(data)

client.send(encrypted_data)

client.close()

