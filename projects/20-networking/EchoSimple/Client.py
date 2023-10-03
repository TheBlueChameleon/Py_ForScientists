import socket
from .Constants import HOST, PORT

MESSAGES = ["Hello World!", "Foo", "Bar"]


def client():
    print("starting client (C)")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"C: about to connect to {HOST, PORT}")
        s.connect((HOST, PORT))
        print("C: connection was accepted")

        for message in MESSAGES:
            size = len(message)
            print(f"C: sending message '{message}' ({size} bytes)")
            s.sendall(size.to_bytes() + message.encode())
        data = s.recv(1024)

    print(f"C: Received {data!r}")


if __name__ == "__main__":
    client()
