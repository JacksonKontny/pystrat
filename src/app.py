import os

from celery import Celery
from dotenv import load_dotenv
from flask import request, jsonify, Flask, flash, redirect, url_for

from src.conf import CELERY_BROKER_URL, SECRET_KEY
from src.core.backup.upload_file import handle_upload_file_request

flask_app = Flask(__name__)

load_dotenv()

flask_app.config["CELERY_BROKER_URL"] = CELERY_BROKER_URL
flask_app.config["SECRET_KEY"] = SECRET_KEY

celery = Celery(flask_app.name, broker=flask_app.config["CELERY_BROKER_URL"])
celery.conf.update(flask_app.config)


@flask_app.route('/', methods=['GET', 'POST'])
def upload_file_handler():
    if request.method == 'POST':
        return handle_upload_file_request(request)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
