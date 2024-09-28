from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('superadmin', 'SuperAdmin'),
        ('manager', 'Manager'),
        ('supervisor', 'Supervisor'),
        ('operator', 'Operator'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set", 
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set_permissions",  
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

class Machine(models.Model):
    machine_id = models.CharField(max_length=100, primary_key=True)
    machine_name = models.CharField(max_length=255)
    tool_capacity = models.IntegerField()
    tool_offset = models.FloatField()
    feedrate = models.IntegerField()
    tool_in_use = models.IntegerField()

    class Meta:
        db_table = 'machine'  

    def __str__(self):
        return f'Machine {self.machine_id}'

class Axis(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    axis_name = models.CharField(max_length=1)
    actual_position = models.FloatField()
    target_position = models.FloatField()
    distance_to_go = models.FloatField()
    velocity = models.IntegerField()
    acceleration = models.IntegerField()