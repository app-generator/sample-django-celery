from celery import shared_task

@shared_task
def check_db_health(self):
    ...

@shared_task
def check_disk_free(self):
    ...
@shared_task
def clean_database(self):
    ...

