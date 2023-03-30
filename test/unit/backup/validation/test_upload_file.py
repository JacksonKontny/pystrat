from unittest.mock import Mock

from src.backup.validation.upload_file import get_file_upload_errors


def test_no_errors(upload_request_context):
    assert get_file_upload_errors(upload_request_context.request) is None


def test_no_file(upload_request_context):
    upload_request_context.request.files = {}
    assert get_file_upload_errors(upload_request_context.request) == ["file required"]


def test_no_file(upload_request_context):
    mock_file = Mock()
    mock_file.filename = ""
    upload_request_context.request.files = {"file": mock_file}
    assert get_file_upload_errors(upload_request_context.request) == [
        "filename required"
    ]
