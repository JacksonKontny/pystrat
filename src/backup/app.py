from http.client import BAD_REQUEST

from flask import Blueprint, Response, request, redirect

from src.backup.validation.upload_file import get_file_upload_errors
from src.core.file_management import save_file

backup_service = Blueprint("backup", __name__, url_prefix="/backup")

SIMPLE_UPLOAD_HTML = """
<!doctype html>
<title>Upload new File</title>
<h1>Upload new File</h1>
<form method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Upload>
</form>
"""


@backup_service.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if errors := get_file_upload_errors(request):
            return Response(errors, status=BAD_REQUEST)
        save_file(request.files["file"])
        return redirect("/backup")

    return SIMPLE_UPLOAD_HTML
