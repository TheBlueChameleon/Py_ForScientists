from http import HTTPStatus
import urllib.request as ur
import urllib.error   as ue
from urllib.parse import quote

HOST = "https://de.wikipedia.org/wiki/" + quote("Universität Regensburg")
MAX_LINES_TO_SHOW = 5


def get_charset(headers:dict[str, str]):
    content_type = headers['content-type']
    elements = content_type.split(';')
    if len(elements) == 1:
        return 'ascii'
    else:
        content_type_parameters = dict(foo.strip().split('=') for foo in elements[1:])
        return content_type_parameters.get('charset', 'ascii')


try:
    with ur.urlopen(HOST) as f:
        if (f.status == HTTPStatus.OK):
            headers = dict(f.getheaders())
            for key, value in headers.items():
                print(f"{key:25}: {value}")
            print()

            encoding = get_charset(headers)
            data = f.read().decode(encoding)
            data_lines = data.splitlines()
            lines_to_show = min(MAX_LINES_TO_SHOW, len(data_lines))
            for line in data_lines[:lines_to_show]:
                print(line)

        else:
            print(f"Unexpected non-error response when requesting '{HOST}':")
            print(f.reason)

except ValueError as e:
    print(f"Could not resolve URL '{HOST}'")
    print(f"Reason: {e}")

except ue.HTTPError as e:
    print(f"An error occurred while loading '{HOST}':")
    print(e)
