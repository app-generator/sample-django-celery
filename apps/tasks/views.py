# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

@login_required(login_url="/login/")
def tasks(request):
    context = {'segment': 'tasks'}

    html_template = loader.get_template('tasks/index.html')
    return HttpResponse(html_template.render(context, request))

