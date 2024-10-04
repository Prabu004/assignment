import os
import random
import django
from time import sleep


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "machine_management.settings")  # Replace with your project name
django.setup()

from api.models import Machine, Axis  
def generate_machine_data(machine_id, machine_name):
    tool_capacity = 24
    tool_offset = random.uniform(5, 40)  
    feedrate = random.randint(10000, 20000)  
    tool_in_use = random.randint(1, tool_capacity)

   
    machine, created = Machine.objects.update_or_create(
        machine_id=machine_id,
        defaults={
            'machine_name': machine_name,
            'tool_capacity': tool_capacity,
            'tool_offset': tool_offset,
            'feedrate': feedrate,
            'tool_in_use': tool_in_use
        }
    )
    return machine  
def generate_axis_data(machine):
    axis_names = ['X', 'Y', 'Z', 'A', 'C']

    for axis_name in axis_names:
        max_acceleration = 200
        max_velocity = 60
        actual_position = random.uniform(-190, 190)
        target_position = random.uniform(-190, 191)
        distance_to_go = target_position - actual_position
        homed = random.choice([True, False])
        acceleration = random.randint(100, 150)
        velocity = random.randint(40, 80)

       
        axis, created = Axis.objects.update_or_create(
            machine=machine,
            axis_name=axis_name,
            defaults={
                'max_acceleration': max_acceleration,
                'max_velocity': max_velocity,
                'actual_position': actual_position,
                'target_position': target_position,
                'distance_to_go': distance_to_go,
                'homed': homed,
                'acceleration': acceleration,
                'velocity': velocity
            }
        )

# Generate initial machine and axis data
for i in range(1, 21):
    machine_id = 81258856 + i  
    machine_name = f'EMPX{i}'  
    machine = generate_machine_data(machine_id, machine_name)  
    generate_axis_data(machine)  

while True:
    for i in range(1, 21):
        machine_id = 81258856 + i
        machine = Machine.objects.get(machine_id=machine_id)  
        generate_axis_data(machine)  
    
    sleep(900)  
