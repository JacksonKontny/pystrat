import os
from unittest.mock import Mock, patch

from src.core.client.gcp.cloud_storage import upload_blob


@patch("src.core.client.gcp.cloud_storage.UPLOAD_BUCKET_NAME", "bucket_name")
@patch("src.core.client.gcp.cloud_storage.UPLOAD_FOLDER", "upload_folder")
def test_upload_blob():
    gcs_client_mock = Mock()
    with patch(
        "src.core.client.gcp.cloud_storage.storage.Client", return_value=gcs_client_mock
    ):
        upload_blob("file_id", "file_name")
    gcs_client_mock.bucket.assert_called_once_with("bucket_name")
    gcs_client_mock.bucket().blob.assert_called_once_with("file_id")
    gcs_client_mock.bucket().blob().upload_from_filename.assert_called_once_with(
        os.path.join("upload_folder", "file_id")
    )
