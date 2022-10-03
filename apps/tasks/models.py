# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# Create your models here.

'''
Tasks: 
- id (PK), 
- name,         # user input  
- script_name,  # Dynamic list -> celery_scripts
- description   # user input
'''

'''
TaskStatus: 
- id (PK),       
- task_id,      # linked to tasks.ID
- ts_start,     # Unix timestamp (seconds)
- ts_end,       # Unix timestamp (seconds)
- state:        # RUNNING, FINISHED, CANCELED, UNKNOWN 
- status:       # OK, FAILED, UNKNOWN 
- log_file      # None or file saved in celery_logs DIRECTORY
'''