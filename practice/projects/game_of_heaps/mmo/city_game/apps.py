from django.apps import AppConfig


class CityGameConfig(AppConfig):
    name = 'city_game'

    def ready(self):
    	from .tasks import execute_timers
    	execute_timers(repeat=10)
