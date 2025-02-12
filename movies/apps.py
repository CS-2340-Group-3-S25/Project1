from django.apps import AppConfig
from django.db.models.signals import post_migrate

def load_initial_data(sender, **kwargs):
    Movie = sender.get_model('Movie')
    Movie.load_initial_data()

class MoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies'

    def ready(self):
        post_migrate.connect(load_initial_data, sender=self)
