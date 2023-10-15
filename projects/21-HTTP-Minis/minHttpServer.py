import http.server as hs

PORT = 8080
Handler = hs.SimpleHTTPRequestHandler
# Note: SimpleHTTPRequestHandler is a
# predefined handler under
# BaseHTTPRequestHandler

with hs.HTTPServer(
        ("", PORT), Handler
    ) as daemon:
    print("serving at port", PORT)
    daemon.serve_forever()
