import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",5050))
while True:
    s.connect(("0.0.0.0", 5050)) #replace with the other clients public ip
    print(s.recv(1024).decode())
    s.send("Hello there!".encode())
    s.close()
    break

