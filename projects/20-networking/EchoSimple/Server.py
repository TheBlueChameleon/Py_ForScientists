import socket
from .Constants import PORT, HOST


def server():
    print("starting server (S)")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))

        print(f"S: listening on {HOST, PORT}...")
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"S: connected to {addr}.")
            while True:
                try:
                    size_bytes = conn.recv(1)
                except ConnectionResetError:
                    print("S: connection closed on client side -- shutting down server")
                    break

                if not size_bytes:
                    print("S: transmission from client ended -- shutting down server")
                    break
                else:
                    size = int.from_bytes(size_bytes)
                    print(f"S: incoming message of size: {size}")
                    data = conn.recv(size)
                    print(f"S: received: {data}")
                    print("S: replying to client with same message")
                    conn.sendall(data)

if __name__ == "__main__":
    server()
