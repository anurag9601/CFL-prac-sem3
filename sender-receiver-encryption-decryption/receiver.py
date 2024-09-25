import socket 

from Crypto.Cipher import AES

key = b"HEYIAMAKINGKEYAA"
salt = b"HEYIAMAKINSALTA"

cipher = AES.new(key, AES.MODE_EAX , salt)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8080))

server.listen()

data, addr = server.accept()

encrypt_data = data.recv(1024)

decrypt_data = cipher.decrypt(encrypt_data)

print("message:", decrypt_data.decode("utf-8"))
