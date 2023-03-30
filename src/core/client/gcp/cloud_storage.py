import os

from google.cloud import storage

from src.conf import UPLOAD_BUCKET_NAME, UPLOAD_FOLDER


def upload_blob(source_file_id, original_file_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(UPLOAD_BUCKET_NAME)
    blob = bucket.blob(source_file_id)
    blob.upload_from_filename(os.path.join(UPLOAD_FOLDER, source_file_id))
    print(f"File {source_file_id} uploaded for {original_file_name}.")
