import os

from google.cloud import storage

from src.conf import UPLOAD_BUCKET_NAME, UPLOAD_FOLDER


def upload_blob(source_file_name, original_file_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(UPLOAD_BUCKET_NAME)
    blob = bucket.blob(source_file_name)

    # Optional: set a generation-match precondition to avoid potential race conditions
    # and data corruptions. The request to upload is aborted if the object's
    # generation number does not match your precondition. For a destination
    # object that does not yet exist, set the if_generation_match precondition to 0.
    # If the destination object already exists in your bucket, set instead a
    # generation-match precondition using its generation number.
    generation_match_precondition = 0

    blob.upload_from_filename(os.path.join(UPLOAD_FOLDER, source_file_name),
                              if_generation_match=generation_match_precondition)

    print(
        f"File {source_file_name} uploaded for {original_file_name}."
    )
