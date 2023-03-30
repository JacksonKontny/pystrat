from unittest.mock import patch

import pytest
from celery.exceptions import Retry

from src.task.backup import queue_backup_file_task


def test_retry_on_exception():
    with patch("src.task.backup.upload_blob") as mock_upload_blob:
        upload_exception = Exception("test")
        mock_upload_blob.side_effect = upload_exception
        with patch("src.task.backup.queue_backup_file_task.retry") as mock_retry:
            mock_retry.side_effect = Retry("test")
            with pytest.raises(Retry):
                queue_backup_file_task("file_id", "file_name")
    mock_upload_blob.assert_called_once_with("file_id", "file_name")
    mock_retry.assert_called_once_with(
        exc=upload_exception, countdown=60, max_retries=3
    )


def test_file_uploaded():
    with patch("src.task.backup.upload_blob") as mock_upload_blob:
        with patch("src.task.backup.queue_backup_file_task.retry") as mock_retry:
            queue_backup_file_task("file_id", "file_name")
    mock_upload_blob.assert_called_once_with("file_id", "file_name")
    mock_retry.assert_not_called()
