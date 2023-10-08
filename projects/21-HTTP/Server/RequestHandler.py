import http.server as hs
import sys
from http import HTTPStatus

from .Constants import *
from .FilesHandler import *
from .FormsHandler import parse_form_data, FormDataElement


class RequestHandler(hs.BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        logging.debug("%s started with\n\targs: %s\n\tkwargs: %s",
                      str(self.__class__.__name__), args, kwargs)
        print(file=sys.stderr)  # makes the log better readable

        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.log_incoming_request()

        request_data = get_file(self.path)
        if request_data:
            self.answer_html(request_data)
        else:
            self.answer_html(
                generate_error_page(f"Error {HTTPStatus.NOT_FOUND}: Could not find '{self.path[1:]}'"),
                response_code=HTTPStatus.NOT_FOUND
            )

            # simpler version that does not look so fancy in the browser:
            # self.send_error(HTTPStatus.NOT_FOUND, "error message")

        print(file=sys.stderr)  # makes the log better readable

    def do_POST(self):
        self.log_incoming_request()
        request = self.path[1:]  # remove the leading slash
        parsed_content = self.parse_post_data()
        logging.info("POST message header data for request '%s'", request)
        for form_data_element in parsed_content.values():
            logging.info(f"  {form_data_element.header}")

        answer_type, code, answer = dispatch_post(request, parsed_content)
        if answer_type == AnswerTypes.html:
            self.answer_html(answer, response_code=code)
        elif answer_type == AnswerTypes.error:
            error_page = generate_error_page(f"Error {code}: '{answer}'")
            self.answer_html(error_page, response_code=code)
        elif answer_type == AnswerTypes.file:
            self.answer_file(file=answer.encode('ascii'), filename="psf.json", response_code=code)

        print(file=sys.stderr)  # makes the log better readable

    def log_incoming_request(self):
        # note: self.request is the socket for this connection
        logging.info("Incoming Request from %s", self.request.getpeername())
        logging.debug("  request line: %s", self.requestline)
        for key, value in self.headers.items():
            logging.debug(f"    {key:30}: {value}")
        print(file=sys.stderr)  # makes the log better readable

    def answer(self, header_dict: dict, data: bytes, response_code: HTTPStatus):
        logging.info(f"sending answer:\n\t{LINE_BREAK.join(f'{key}: {value}' for key, value in header_dict.items())}")
        if not header_dict.get(HttpHeaders.content_length):
            header_dict[HttpHeaders.content_length] = str(len(data))

        self.send_response(response_code)
        for key, value in header_dict.items():
            self.send_header(key, value)
        self.end_headers()

        self.wfile.write(data)

    def answer_html(self, html: str, response_code: HTTPStatus = HTTPStatus.OK):
        self.answer(
            {HttpHeaders.content_type: "text/html", },
            html.encode('utf-8'),
            response_code
        )

    def answer_file(self, file: bytes, filename: str, response_code: HTTPStatus = HTTPStatus.OK):
        self.answer(
            {
                HttpHeaders.content_type: "application/octet-stram",
                "content-disposition": "attachment; filename=\"" + filename + "\""
            },
            file,
            response_code
        )

    def parse_post_data(self) -> dict[str, FormDataElement]:
        content_length = int(self.headers[HttpHeaders.content_length])
        content_type = self.headers[HttpHeaders.content_type]
        content = self.rfile.read(content_length)
        return parse_form_data(content, content_type)


KNOWN_POST_REQUESTS = {
    "request_print": handle_request_print,
    "request_psf": handle_request_psf
}


def dispatch_post(path: str, parsed_content: dict[str, FormDataElement]) -> tuple[AnswerTypes, HTTPStatus, str]:
    handler = KNOWN_POST_REQUESTS.get(path)

    if handler:
        return handler(parsed_content)
    else:
        return AnswerTypes.error, HTTPStatus.BAD_REQUEST, f"bad request: '{path}'"
