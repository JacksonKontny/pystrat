from celery import shared_task

from src.core.client.gcp.cloud_storage import upload_blob


@shared_task
def queue_backup_file_task(file_id, file_name):
    print("Queued backup task received for file_id: %s" % file_id)
    upload_blob(file_id, file_name)
