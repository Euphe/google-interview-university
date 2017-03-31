from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import math

ACTION_CHOICES = (('building_up', 'upgrade'),)
class Timer(models.Model):
    timer_id = models.AutoField(primary_key=True)
    finish_time = models.DateTimeField()
    action = models.CharField(choices = ACTION_CHOICES, max_length=50)
    args = models.CharField(max_length=300)

    class Meta:
        ordering = ['finish_time']

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    resources = models.IntegerField(default=0) 

    def __str__(self):
        return 'City of {} owned by {}'.format(self.city_name, self.user.username)

class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City)
    building_name = models.CharField(max_length=100)
    level = models.IntegerField(default=1) 

    upgrade_scheduled = models.BooleanField(default=False)

    def resource_output(self):
        return 2**(2+self.level)

    def upgrade_time(self):
        return 2**(2+self.level)

    def upgrade(self):
        self.level += 1
        self.upgrade_scheduled = False
        self.save()

    def schedule_upgrade(self):
        self.upgrade_scheduled = True
        self.save()


@receiver(post_save, sender=User)
def create_user_city(sender, instance, created, **kwargs):
    if created:
        City.objects.create(user=instance, city_name="{}'s city".format(instance.username))

@receiver(post_save, sender=User)
def save_user_city(sender, instance, **kwargs):
    instance.city.save()

@receiver(post_save, sender=City)
def create_city_building(sender, instance, created, **kwargs):
    if created:
        building = Building.objects.create(city=instance, building_name="Resource building")
        building.save()