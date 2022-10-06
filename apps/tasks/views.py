# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from celery import current_app

@login_required(login_url="/login/")
def tasks(request):
    context = {'segment': 'tasks','tasks':get_celery_all_tasks()}

    html_template = loader.get_template('tasks/index.html')
    return HttpResponse(html_template.render(context, request))


def get_celery_all_tasks():
    current_app.loader.import_default_modules()
    tasks = list(sorted(name for name in current_app.tasks                         
             if not name.startswith('celery.')))
    return tasks

