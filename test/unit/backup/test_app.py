import http
from http.client import BAD_REQUEST
from unittest.mock import patch

from src.backup.app import upload_file


def test_upload_file_error(upload_request_context):
    with patch("src.backup.app.save_file") as mock_save_file:
        with patch("src.backup.app.get_file_upload_errors") as validation_mock:
            validation_mock.return_value = ["error"]
            response = upload_file()
            assert response.status_code == BAD_REQUEST
            assert response.data == b"error"
            mock_save_file.assert_not_called()


def test_upload_file_success(upload_request_context):
    with patch("src.backup.app.save_file") as mock_save_file:
        with patch("src.backup.app.get_file_upload_errors") as validation_mock:
            validation_mock.return_value = None
            response = upload_file()
            assert response.status_code == http.client.FOUND
            assert mock_save_file.call_args_list[0][0][0].filename == "file_name"
