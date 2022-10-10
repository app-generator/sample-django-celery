from django_celery_results.models import TaskResult
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import os

@receiver(post_save, sender=TaskResult)
def result_updated(sender, **kwargs):
    if 'instance' not in kwargs:
        return
    result=kwargs.pop("instance")
    if result.status!="STARTED":
        add_log(result)


def add_log(result:TaskResult):
    """
    Adds log file to celery logs with formatted date as name.
    :param result TaskResult: Result of executed celery task
    :rtype: None
    """
    if not result.task_name:
        return
    log_file_path=os.path.join(settings.CELERY_LOGS_DIR,f"{result.date_created.strftime(r'%Y%m%d-%H%M%S')}-{result.task_name}-{result.status}-{result.id}.log")
    with open(log_file_path,"w+") as f:
        if result.status=="FAILURE":
            f.writelines([result.result,result.traceback])
        else:
            f.write(result.result)

        f.close()
        

    