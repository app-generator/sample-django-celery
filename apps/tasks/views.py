# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import imp
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from celery import current_app
from .tasks import execute_script, users_in_db
from django_celery_results.models import TaskResult
from celery.contrib.abortable import AbortableAsyncResult
import time
from core.celery import app


@login_required(login_url="/login/")
def tasks(request):
    context = {'segment': 'tasks','tasks':get_celery_all_tasks()}

    html_template = loader.get_template('tasks/index.html')
    return HttpResponse(html_template.render(context, request))

def run_task(request,task_name):
    tasks=[execute_script,users_in_db]

    for task in tasks:
        if task.__name__==task_name:
            if task.__name__==execute_script.__name__:
                task.delay({"script":request.POST.get("script")})
            else:
                task.delay()
    time.sleep(1)

    return redirect("tasks")
    
def cancel_task(request,task_id):
    result=TaskResult.objects.get(task_id=task_id)
    abortable_result=AbortableAsyncResult(result.task_id,task_name=result.task_name,app=app)
    if not abortable_result.is_aborted():
        abortable_result.revoke(terminate=True)
    time.sleep(1)
    return redirect("tasks")

    

    



def get_celery_all_tasks():
    current_app.loader.import_default_modules()
    tasks = list(sorted(name for name in current_app.tasks                         
             if not name.startswith('celery.')))
    tasks=[{"name":name.split(".")[-1],"script":name } for name in tasks]
    for task in tasks:
        last_task=TaskResult.objects.filter(task_name=task["script"]).order_by("date_created").last()
        if last_task:
            task["id"]=last_task.task_id
            task["has_result"]=True
            task["status"]=last_task.status
            task["successfull"]=last_task.status=="SUCCESS" or last_task.status=="STARTED"
            task["date_created"]=last_task.date_created
            task["date_done"]=last_task.date_done
            task["result"]=last_task.result



    return tasks

