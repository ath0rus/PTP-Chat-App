import socket
from lib.parse_args import parse_args

if __name__ == "__main__":
    args = parse_args()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",int(args.port)))
    s.connect((args.ip, int(args.port))) # replace 0.0.0.0 with other clients public ip

    s.send("Hello!".encode())
    print(s.recv(1024).decode())