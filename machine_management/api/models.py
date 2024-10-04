from django.db import models

# Create your models here.

from django.contrib.auth.models import User, Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    # Create default user roles/groups
    Group.objects.get_or_create(name='SUPERADMIN')
    Group.objects.get_or_create(name='Manager')
    Group.objects.get_or_create(name='Supervisor')
    Group.objects.get_or_create(name='Operator')


class Machine(models.Model):
    machine_id = models.BigIntegerField(unique=True)
    machine_name = models.CharField(max_length=100)
    tool_capacity = models.IntegerField()
    tool_offset = models.FloatField()
    feedrate = models.FloatField()
    tool_in_use = models.IntegerField()

    def __str__(self):
        return self.machine_name

class Axis(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    axis_name = models.CharField(max_length=10)
    max_acceleration = models.FloatField()
    max_velocity = models.FloatField()
    actual_position = models.FloatField()
    target_position = models.FloatField()
    distance_to_go = models.FloatField()
    homed = models.BooleanField(default=False)
    acceleration = models.FloatField()
    velocity = models.FloatField()

    class Meta:
        unique_together = ('axis_name', 'machine')

    def __str__(self):
        return f"{self.machine.machine_name} - {self.axis_name}"
