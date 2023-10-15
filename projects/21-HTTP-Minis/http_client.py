import http.client

host = "de.wikipedia.org"

def request(method, uri):
    conn = http.client.HTTPSConnection(host)
    conn.request(method, uri, headers={"Host": host})
    return conn.getresponse()

def show_header(response):
    print(response.status, response.reason)
    for key in response.headers.keys():
        print(f"{key:20}: {response.headers[key]}")

def show_content(response):
    try:
        content_type_fragments = response.headers['content-type'].split(';')
        content_type = content_type_fragments[0]
        content_encoding = content_type_fragments[1].split('=')[1]
    except IndexError:
        content_encoding = 'utf-8'
    print(response.read().decode(content_encoding))



response = request("OPTIONS", "/wiki/Wikipedia:Hauptseite")
show_header(response)
print()
show_content(response)
