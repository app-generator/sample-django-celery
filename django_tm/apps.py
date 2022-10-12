from django.apps import AppConfig


class TasksConfig(AppConfig):

    """
    See https://docs.djangoproject.com/en/2.1/ref/applications/#django.apps.AppConfig
    """

    name = "django_tm"
    label = "django_tm"
    verbose_name = "Django Tasks Manager"

    def ready(self):
        from . import signals
