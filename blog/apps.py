from django.apps import AppConfig
from django.conf import settings


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        # print(
        #     settings.DB_PASS, settings.DB_USER, settings.DB_DB
        # )
        pass
