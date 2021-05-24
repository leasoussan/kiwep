from django.apps import AppConfig


class ContentConfig(AppConfig):
    name = 'content'
    """The ready def is to say when ever the app is ready, please run signals as they wont run automaticaly"""
    def ready(self):
        import content.signals