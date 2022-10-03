# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.tasks import views

urlpatterns = [
    path('tasks', views.tasks, name="tasks"),
]