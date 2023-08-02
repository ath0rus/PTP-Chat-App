import socket
from lib.parse_args import parse_args

if __name__ == "__main__":
    args = parse_args()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",int(args.port)))
    while True:
        s.connect((args.ip, int(args.port))) #replace with the other clients public ip
        print(s.recv(1024).decode())
        s.send("Hello there!".encode())
        s.close()
        break

