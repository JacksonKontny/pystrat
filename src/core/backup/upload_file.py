import os
import uuid
from http.client import BAD_REQUEST

from flask import Response, redirect
from werkzeug.utils import secure_filename

from src.conf import UPLOAD_FOLDER
from src.core.task.backup import queue_backup_file_task


def get_error(request):
    if 'file' not in request.files:
        return "file required"
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return "filename required"


def handle_upload_file_request(request):
    # check if the post request has the file part
    if error := get_error(request):
        return Response(error, status=BAD_REQUEST)

    file_id = str(uuid.uuid4())
    request.files['file'].save(os.path.join(UPLOAD_FOLDER, file_id))
    queue_backup_file_task.delay(file_id, secure_filename(request.files['file'].filename))

    return redirect('/')
