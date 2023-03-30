from typing import List

from flask import Request


def get_file_upload_errors(request: Request) -> List[str]:
    if "file" not in request.files:
        return ["file required"]
    file = request.files["file"]
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == "":
        return ["filename required"]
