import selectors
import socket
import types

from uuid import uuid4 as get_unique_ID
from time import time as now
from types import SimpleNamespace

from .Constants import *


def make_session_descriptor(uid, client_name, last_active):
    return SimpleNamespace(uid=uid, client_name=client_name, last_active=last_active)


class Server:
    TIMEOUT_SECONDS = 1
    MAX_CONNECTIONS = 5
    MAX_SESSIONS = 8

    def __init__(self, max_runtime_seconds):
        self.msg("starting")
        self.max_runtime_seconds = max_runtime_seconds
        self.boot_time = now()
        self.active_session_IDs = dict()
        self.selector = selectors.DefaultSelector()

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection_delegator:
            connection_delegator.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            connection_delegator.bind((HOST, PORT))
            connection_delegator.listen(self.MAX_CONNECTIONS)
            connection_delegator.setblocking(False)
            self.selector.register(connection_delegator, selectors.EVENT_READ, data=None)
            self.msg(f"listening for connections on {HOST, PORT}")

            try:
                while self.ready():
                    events: list[tuple[selectors.SelectorKey, int]]
                    events = self.selector.select(timeout=self.TIMEOUT_SECONDS)
                    for key, mask in events:
                        if key.data is None:
                            self.accept_wrapper(key.fileobj)
                        else:
                            self.service_connection(key, mask)
            finally:
                self.msg(f"planned shutdown after {self.TIMEOUT_SECONDS} seconds")
                self.selector.unregister(connection_delegator)
                connection_delegator.close()
                self.selector.close()

    def ready(self) -> bool:
        return now() < (self.boot_time + self.max_runtime_seconds)

    def accept_wrapper(self, connection_request: socket.socket):
        conn, addr = connection_request.accept()
        self.msg(f"accepted connection from {addr}")
        conn.setblocking(False)
        data = SimpleNamespace(addr=addr, received=b"", to_send=b"")
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.selector.register(conn, events, data=data)

    def service_connection(self, key: selectors.SelectorKey, mask: int):
        sock: socket.socket
        sock = key.fileobj
        data: types.SimpleNamespace
        data = key.data

        if mask & selectors.EVENT_READ:
            data.received = sock.recv(1024)
            data.addr = sock.getpeername()
            data.to_send = self.get_response_to(data)

        if mask & selectors.EVENT_WRITE:
            if data.to_send:
                self.msg(f"sending [0x{data.to_send.hex()}] to {sock.getpeername()}")
                sock.sendall(data.to_send)
                data.to_send = None

            self.msg(f"closing connection to {sock.getpeername()}")
            self.selector.unregister(sock)
            sock.close()

    def get_response_to(self, data):
        message_type = data.received[:LENGTH_MESSAGE_TYPE]
        data.received = data.received[LENGTH_MESSAGE_TYPE:]

        if message_type == MSG_REQUEST_SESSION_ID:
            return self.handle_request_session_id(data)
        elif message_type == MSG_REQUEST_PROCESS_MESSAGE:
            return self.handle_request_process_message(data)

    def handle_request_session_id(self, data):
        client_name = data.received.decode('utf-8')
        uid = get_unique_ID()
        hex_id = uid.hex
        self.msg(f"assigning session ID {hex_id} to {client_name} on address {data.addr}")
        if self.active_session_IDs.get(hex_id):
            self.msg("key in use")
            return b''
        else:
            self.active_session_IDs[hex_id] = make_session_descriptor(uid, client_name, now())

        return uid.bytes

    def handle_request_process_message(self, data):
        session_and_payload = self.handle_session_id(data)
        if session_and_payload:
            session: types.SimpleNamespace
            payload: bytes
            session, payload = session_and_payload
            self.msg(f"RECEIVED {payload} from {session.client_name}")
            message = payload.decode('utf-8')
            answer = f"processed '{message}'"
            return answer.encode('utf-8')
        else:
            self.msg(f"RECEIVED DATA FROM UNKNWON SESSION: {data}")
            return b''

    def handle_session_id(self, data):
        session_id = data.received[:LENGTH_SESSION_ID].hex()
        session_descriptor = self.active_session_IDs.get(session_id)
        payload = data.received[LENGTH_SESSION_ID:]
        if session_descriptor:
            session_descriptor.last_active = now()
            return session_descriptor, payload
        else:
            return None

    @staticmethod
    def msg(msg):
        print(f"{'server':{LOGS_WIDTH}}: {msg}\n", end="")
