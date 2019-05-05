from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # Ready function. Register signals here
    def ready(self):
        # Import user's signals 
        import users.signals 