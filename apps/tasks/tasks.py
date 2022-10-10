
import os
from core.celery import app
from celery.contrib.abortable import AbortableTask
import subprocess
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from django.conf import settings
import time

@app.task(bind=True,base=AbortableTask)
def users_in_db(self):
    users=User.objects.all()
    time.sleep(12)
    return {"users":"\n".join([u.email for u in users])}
 

@app.task(bind=True,base=AbortableTask)
def execute_script(self,data:dict):
    script_name=data.get("script")   
    script=settings.CELERY_SCRIPTS.get(script_name)

    if script_name and script:
        # Executing related script
        script_path=os.path.join(settings.CELERY_SCRIPTS_DIR,script)
        process = subprocess.Popen(f"python {script_path}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(8)
        if process.wait()==0: # If script execution successfull
            stdout=process.stdout.read().decode()
        else:
            stderr=process.stderr.read().decode()
            raise Exception(stderr)

        
        return {"stdout":stdout}







