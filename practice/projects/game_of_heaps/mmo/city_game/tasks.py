from background_task import background
from .models import Building, Timer
from heapq import heappop
import time
import json
import datetime

@background()
def execute_timers(*args, **kwargs):
    # lookup user by id and send them a message
    now_time = datetime.datetime.now()
    timers = Timer.objects.filter(finish_time__lte=now_time)
    for timer in timers:
        if timer.action == 'building_up':
            timer_args = json.loads(timer.args)
            target_building_id = timer_args['target']

            building = Building.objects.get(pk=target_building_id)
            print(building)
            building.upgrade()
            print('Building upgraded!')

        timer.delete()