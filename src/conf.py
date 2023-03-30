import os

from dotenv import load_dotenv

load_dotenv()

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://redis:6379")
SECRET_KEY = os.getenv("SECRET_KEY", "b6f82a7bb00a10a7baa2370b69c58a25")
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "./uploads")
UPLOAD_BUCKET_NAME = os.getenv("UPLOAD_BUCKET_NAME")
