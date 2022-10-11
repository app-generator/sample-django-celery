from django_celery_results.models import TaskResult
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.conf import settings
import os
import json


@receiver(pre_save, sender=TaskResult)
def pre_result_updated(sender, **kwargs):
    if 'instance' not in kwargs:
        return
    instance=kwargs.pop("instance")
    if instance.status!="STARTED":
        result=json.loads(instance.result)
        if result.get("error"):
            instance.status="FAILURE"
            instance.traceback=result.get("logs")
        


@receiver(post_save, sender=TaskResult)
def post_result_updated(sender, **kwargs):
    if 'instance' not in kwargs:
        return
    instance=kwargs.pop("instance")
    if instance.status!="STARTED":
        add_log(instance)


def add_log(result:TaskResult):
    """
    Adds log file to celery logs with formatted date as name.
    :param result TaskResult: Result of executed celery task
    :rtype: None
    """
    if not result.task_name:
        return
    _input= json.loads(result.result).get("input")
    if _input:
        log_file_path=os.path.join(settings.CELERY_LOGS_DIR,f"{result.date_created.strftime(r'%Y%m%d-%H%M%S')}-{result.task_name}-{_input}-{result.status}-{result.id}.log")

    else:
        log_file_path=os.path.join(settings.CELERY_LOGS_DIR,f"{result.date_created.strftime(r'%Y%m%d-%H%M%S')}-{result.task_name}-{result.status}-{result.id}.log")
    with open(log_file_path,"w+") as f:
        if result.status=="FAILURE":
            f.writelines([result.result,result.traceback])
        else:
            f.write(result.result)

        f.close()
        

    