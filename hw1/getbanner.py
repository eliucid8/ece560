import socket
import sys

def main():
    if len(sys.argv) < 3:
        print("usage: getbanner.py <host> <port>")
    host = sys.argv[1]
    port = int(sys.argv[2])

    # pulling implemetation from https://docs.python.org/3/library/socket.html#socket-objects
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        _ = s.send('QUIT\n'.encode())

        while True:
            data = s.recv(1024)
            if not data:
                s.close()
                return
            print(data.decode(), end="")

if __name__ == "__main__":
    main()
