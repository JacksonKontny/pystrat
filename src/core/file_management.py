import os
import uuid

from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from src.conf import UPLOAD_FOLDER
from src.task.backup import queue_backup_file_task


def save_file(file: FileStorage):
    file_id = str(uuid.uuid4())
    file.save(os.path.join(UPLOAD_FOLDER, file_id))

    queue_backup_file_task.delay(file_id, secure_filename(file.filename))
