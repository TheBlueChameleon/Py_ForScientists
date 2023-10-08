import typing

from .Constants import *


# ==================================================================================================================== #

class FormDataElement(typing.NamedTuple):
    content: bytes
    header: dict[str, str]


# ==================================================================================================================== #


def parse_multipart(message: bytes, content_descriptor_elements: list[str]) -> dict[str, FormDataElement]:
    """
    A POST message looks like this:
      '--[segment][segment][...]--'

    in which each [segment] corresponds to a html form item and looks like
      '[boundary]\\r\\n[header]\\r\\n\\r\\n[content]--'

    The [boundary] is given in content_descriptor_elements[1] as a string of the form
        "boundary=[boundary]"

    The header is expected to contain the field "name" from the html form item.
    This function splits the message into segments constructs a FormDataElement for each of them.
    These FormDataElement will be returned as a dict which maps the "name" field to the corresponding data.

    :param message: the raw bytes message from the HTTP POST
    :param content_descriptor_elements: The elements from HTTP header Content-Type, split at ";"
    :return: a dict mapping the form item names to their corresponding values and header data
    """

    result = dict()

    boundary_line = content_descriptor_elements[1]
    boundary_pos = boundary_line.find("=") + 1
    boundary = boundary_line[boundary_pos:].encode('ascii')

    segments = message.split(boundary)[1:-1]  # first and last segment only contain "--"
    for s in segments:
        content, header = parse_multipart_segment(s)
        fde = FormDataElement(content=content, header=header)
        result[header[FormDataFields.name]] = fde
    return result


def parse_multipart_segment(segment: bytes) -> tuple[bytes, dict[str, str]]:
    """
    This function expects a POST message segment in the form:
        '\\r\\n<header>\\r\\n\\r\\n<content>--\\r\\n'
    and transforms it into a tuple of content and a header dict

    :param segment: the data pertaining to one html form item, with two padding bytes in front and back each for easier
        use with str.split()
    :return: a tuple of (form item payload, dict of header data)
    """

    relevant_part = segment[2:-4]
    header_raw, content = relevant_part.split((LINE_BREAK * 2).encode('ascii'), 1)
    header_str = header_raw.decode('ascii')
    header_dct = parse_multipart_header(header_str)
    if not header_dct.get(HttpHeaders.content_length):
        header_dct[HttpHeaders.content_length] = str(len(content))
    return content, header_dct


def parse_multipart_header(header: str) -> dict[str, str]:
    """
    The header is a multiline string comprised of key-value pairs of the form
        "key: value"
    The first line, however has a special form:
        "Content-Disposition: form-data; key=value; key=value; ..."

    This function extracts all key-value pairs and makes them into a single dict

    :param header: The header part of the HTTP POST message pertaining to a single html form item
    :return: a dict
    """

    result = dict()
    lines: list[str] = header.split(LINE_BREAK * 2)

    # first line starts with "Content-Disposition: form-data;"
    # Only text behind that is relevant
    first_line_relevant_index = lines[0].find(";")
    first_line_relevant = lines[0][first_line_relevant_index + 1:]
    first_line_components = first_line_relevant.split(";")
    for component in first_line_components:
        key, value = component.split("=")
        key = key.strip()
        value = value[1:-1]  # remove quotation marks
        result[key] = value

    for line in lines[1:]:
        key, value = line.split(":")
        key = key.lower()
        value = value.strip()
        result[key] = value
    return result


# -------------------------------------------------------------------------------------------------------------------- #
def parse_plain(content: bytes, content_type: list[str]) -> dict[str, FormDataElement]:
    content_str = content.decode('ascii')
    content_pairs = list((item.split("=")) for item in content_str.split("&"))
    result = dict((key, FormDataElement(header={}, content=content)) for key, content in content_pairs)
    return result


# -------------------------------------------------------------------------------------------------------------------- #

CONTENT_HANDLERS = {
    FormDataFields.type_plain: parse_plain,
    FormDataFields.type_multipart: parse_multipart,
}


def parse_form_data(form_data: bytes, content_descriptor: str) -> dict[str, FormDataElement]:
    content_descriptor_elements: list[str] = content_descriptor.split(";")
    content_type: str = content_descriptor_elements[0].lower()
    content_handler = CONTENT_HANDLERS[FormDataFields(content_type)]
    return content_handler(form_data, content_descriptor_elements)
