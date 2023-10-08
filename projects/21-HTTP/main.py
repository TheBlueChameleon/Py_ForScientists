# HTTP SERVER EXAMPLE
# Run this code, preferably with admin rights (~> sudo)
# Then, start your web browser of choice.
# In the address bar, type ...
#   ... if you can run this with admin rights:
#       localhost
#   ... otherwise:
#       localhost:8080
#
# By interacting with the website displayed in your browser, you should either be able to "upload" files to the server
#   => check the directory ./Server/workspace for new subdirectories
# or to "download" a file "psf.json"
#   => check your downloads folder

from Portfinder import get_http_port
from Server import Server

def main():
    ip = ''
    port = get_http_port()
    Server.run(ip, port)


if __name__ == '__main__':
    main()
