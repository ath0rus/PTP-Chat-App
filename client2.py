import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",5050))
s.connect(("0.0.0.0", 5050)) # replace 0.0.0.0 with other clients public ip

s.send("Hello!".encode())
print(s.recv(1024).decode())