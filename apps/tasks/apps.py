from django.apps import AppConfig


class TasksConfig(AppConfig):

    """
    See https://docs.djangoproject.com/en/2.1/ref/applications/#django.apps.AppConfig
    """

    name = "apps.tasks"
    label = "tasks"
    verbose_name = "Tasks app"

    def ready(self):
        from . import signals
