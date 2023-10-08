import logging
import time
import typing
from pathlib import Path
from http import HTTPStatus

from .FormsHandler import FormDataElement
from .Constants import *

HOME_PATH = Path(__file__).parent / "html"
HOME_FILE = Path("index.html")

WORK_PATH = Path(__file__).parent / "workspace"


def get_file(requested_file) -> typing.Optional[str]:
    requested_path = HOME_PATH / prepare_path(requested_file)
    logging.debug("attempting to fetch file: %s", requested_path)

    if requested_path.exists():
        with open(requested_path, "r") as f:
            data = f.read()
        return data
    else:
        logging.info("did not find %s", requested_path)
        return None


def prepare_path(requested_file: Path) -> Path:
    if requested_file == "/":
        return HOME_FILE
    elif requested_file == "":
        return HOME_FILE
    else:
        return requested_file


def generate_error_page(error_description: str):
    template = get_file("error.html")
    result = template.replace("<!-- error_description -->", error_description)
    return result


def generate_post_successful_page(path: str, parsed_data: dict[str, FormDataElement]):
    metadata = []

    for key, value in parsed_data.items():
        metadata.append("<tr>")
        for header_key, header_value in value.header.items():
            metadata.append(f"  <td><b>{header_key}</b></td>")
            metadata.append(f'  <td style="min-width:50px">{header_value}</td>')
        metadata.append("</tr>")

    template = get_file("post_successful.html")
    result = template.replace("<!-- path -->", path)
    result = result.replace("<!-- metadata -->", "\n".join(metadata))
    return result


def handle_request_print(print_request: dict[str, FormDataElement]) -> tuple[AnswerTypes, HTTPStatus, str]:
    def store(filename, content):
        with open(filename, "wb") as f:
            f.write(content)

    target_dir = WORK_PATH / f"request_{time.time()}"
    target_dir.mkdir(parents=True)

    file_to_print = print_request['file']
    printer_settings = print_request['PSF']

    original_filename = Path(file_to_print.header["filename"])
    if len(str(original_filename)) > 0:
        original_extension = original_filename.suffix
        store(target_dir / f"file_to_print{original_extension}", file_to_print.content)

        if len(printer_settings.header["filename"]) > 0:
            store(target_dir / "printer_settings.json", printer_settings.content)

        return AnswerTypes.html, HTTPStatus.ACCEPTED, generate_post_successful_page("request_print", print_request)
    else:
        return AnswerTypes.error, HTTPStatus.BAD_REQUEST, "no file to print!"


def handle_request_psf(psf_request: dict[str, FormDataElement]) -> tuple[AnswerTypes, HTTPStatus, str]:
    json_file = "{" + LINE_BREAK + "\t" + \
                f",{LINE_BREAK}\t".join(f'"{key}": "{value.content}"' for key, value in psf_request.items()) + \
                LINE_BREAK + "}"

    return AnswerTypes.file, HTTPStatus.OK, json_file
