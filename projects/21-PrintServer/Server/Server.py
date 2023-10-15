import http.server as hs
import logging
import sys

from .RequestHandler import RequestHandler


def run(ip, port):
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s at %(asctime)s : %(message)s")
    logging.info("starting server")
    server_address = (ip, port)
    print(file=sys.stderr)  # makes the log better readable

    daemon = hs.HTTPServer(server_address, RequestHandler)
    daemon.serve_forever()
