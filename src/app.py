from celery import Celery
from dotenv import load_dotenv
from flask import Flask

from src.backup.app import backup_service
from src.conf import CELERY_BROKER_URL, SECRET_KEY

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["CELERY_BROKER_URL"] = CELERY_BROKER_URL
    app.config["SECRET_KEY"] = SECRET_KEY
    app.register_blueprint(backup_service)
    return app


flask_app = create_app()
celery = Celery(flask_app.name, broker=flask_app.config["CELERY_BROKER_URL"])
celery.conf.update(flask_app.config)
flask_app.celery = celery
