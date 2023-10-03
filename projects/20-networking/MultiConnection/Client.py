import socket

from .Constants import *

MESSAGES = [f"message #{i}" for i in range(3)]


class Client:
    def __init__(self, client_id):
        self.client_id = client_id
        self.session_id = None
        self.msg("starting")

    def run(self):
        self.comm_wrapper(self.request_session_id)

        if self.session_id:
            for msg in MESSAGES:
                self.comm_wrapper(self.request_process_message, msg)

        else:
            self.msg(f"received no session ID -- stopping communication and being sad :(")
            return

    def comm_wrapper(self, comm_action, *args):
        connection = self.get_connection()
        if connection:
            try:
                comm_action(connection, *args)
            except ConnectionResetError as e:
                self.msg(f"connection broken: {e}")
            finally:
                connection.close()
        else:
            self.msg("server could not be reached")

    def get_connection(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.msg(f"about to connect to {HOST, PORT}")
        try:
            s.connect((HOST, PORT))
            self.msg(f"connection was accepted as {s.getsockname()}.")
            return s

        except ConnectionRefusedError as e:
            self.msg(f"server refused connection: {e}")
            return None

    def request_session_id(self, connection):
        my_name = f"Client #{self.client_id}"
        connection.sendall(MSG_REQUEST_SESSION_ID + my_name.encode('utf-8'))
        self.session_id = connection.recv(LENGTH_SESSION_ID)
        if self.session_id:
            self.msg(f"got session ID {self.session_id.hex()}")

    def request_process_message(self, connection, msg : str):
        connection.sendall(MSG_REQUEST_PROCESS_MESSAGE +self.session_id + msg.encode('utf-8'))
        answer = connection.recv(1024).decode('utf-8')
        self.msg(f"received answer: \"{answer}\"")

    def msg(self, msg):
        name = f"client #{self.client_id}"
        print(f"{name:{LOGS_WIDTH}}: {msg}\n", end="")
