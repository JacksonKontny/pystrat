from celery import shared_task

from src.core.client.gcp.cloud_storage import upload_blob


@shared_task(bind=True, name="tasks.backup_file")
def queue_backup_file_task(self, file_id, file_name):
    print("Queued file_management task received for file_id: %s" % file_id)
    try:
        upload_blob(file_id, file_name)
    except Exception as e:
        print("Error: %s" % e)
        raise self.retry(exc=e, countdown=60, max_retries=3)
