import socket

PROTECTED_HTTP_PORT = 80
FALLBACK_PORT = 8080

def get_http_port(verbose = False):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = PROTECTED_HTTP_PORT
    try:
        s.bind(('', port))
    except PermissionError as e:
        port = FALLBACK_PORT

    if verbose:
        if port == PROTECTED_HTTP_PORT:
            print(f"working under super user conditions -- using protected port {PROTECTED_HTTP_PORT}.")
        else:
            print(f"working under restricted conditions -- using fallback port {FALLBACK_PORT}.")

    return port

def main():
    print("Portfinder utility -- determines which port can be used given current user rights.")
    print("Try running this as super user.")
    get_http_port(True)


if __name__ == '__main__':
    main()