from enum import StrEnum


class HttpHeaders(StrEnum):
    content_length = "content-length"
    content_type = "content-type"


class FormDataFields(StrEnum):
    type_multipart = "multipart/form-data"
    type_plain = "application/x-www-form-urlencoded"
    name = "name"
    psf = "PSF"


class AnswerTypes(StrEnum):
    html = "html"
    file = "file"
    error = "error"


LINE_BREAK = "\r\n"
