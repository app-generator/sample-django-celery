# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('tasks', views.tasks, name="tasks"),
    path('tasks/run/<str:task_name>', views.run_task, name="run-task"),
    path('tasks/cancel/<str:task_id>', views.cancel_task, name="cancel-task"),
    path('tasks/output/<str:task_id>', views.task_output, name="task-output"),
    path('tasks/log/<str:task_id>'   , views.task_log, name="task-log"),
]