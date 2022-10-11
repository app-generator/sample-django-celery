
import os
from core.celery import app
from celery.contrib.abortable import AbortableTask
import subprocess
from django.contrib.auth.models import User
import time
from django.conf import settings
from os import listdir
from os.path import isfile, join


def get_scripts():
    return [f for f in listdir(settings.CELERY_SCRIPTS_DIR) if isfile(join(settings.CELERY_SCRIPTS_DIR, f))]


@app.task(bind=True, base=AbortableTask)
def users_in_db(self, data: dict):
    """
    Outputs all users in DB
    :param data dict: contains data needed for task execution.
    :rtype: None
    """
    users = User.objects.all()
    time.sleep(12)
    return {"output": "\n".join([u.email for u in users])}


@app.task(bind=True, base=AbortableTask)
def execute_script(self, data: dict):
    """
    This task executes scripts found in settings.CELERY_SCRIPTS_DIR and logs are later generated and stored in settings.CELERY_LOGS_DIR
    :param data dict: contains data needed for task execution. Example `input` which is the script to be executed.
    :rtype: None
    """
    script = data.get("input")
    if script and script in get_scripts():
        # Executing related script
        script_path = os.path.join(settings.CELERY_SCRIPTS_DIR, script)
        process = subprocess.Popen(
            f"python {script_path}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(8)
        error = False
        if process.wait() == 0:  # If script execution successfull
            logs = process.stdout.read().decode()
        else:
            logs = process.stderr.read().decode()
            error = True

        return {"logs": logs, "input": script, "error": error, "output": ""}
