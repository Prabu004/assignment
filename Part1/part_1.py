import psycopg2
import random
from time import sleep

# Database connection
conn = psycopg2.connect(
    dbname="machine_data", 
    user="postgres", 
    password="12345", 
    host="localhost"
)
cursor = conn.cursor()

def generate_machine_data(machine_id, machine_name):
    tool_capacity = 24
    tool_offset = random.uniform(5, 40)  
    feedrate = random.randint(10000, 20000)  
    tool_in_use = random.randint(1, tool_capacity)

    cursor.execute("""
        INSERT INTO machine (machine_id, machine_name, tool_capacity, tool_offset, feedrate, tool_in_use)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (machine_id) DO UPDATE SET
            tool_offset = EXCLUDED.tool_offset,
            feedrate = EXCLUDED.feedrate,
            tool_in_use = EXCLUDED.tool_in_use
    """, (machine_id, machine_name, tool_capacity, tool_offset, feedrate, tool_in_use))

    conn.commit()

def generate_axis_data(machine_id):
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

        cursor.execute("""
            INSERT INTO axis (axis_name, max_acceleration, max_velocity, actual_position, target_position, distance_to_go, homed, acceleration, velocity, machine_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (axis_name, machine_id) DO UPDATE SET
                actual_position = EXCLUDED.actual_position,
                target_position = EXCLUDED.target_position,
                distance_to_go = EXCLUDED.distance_to_go,
                homed = EXCLUDED.homed,
                acceleration = EXCLUDED.acceleration,
                velocity = EXCLUDED.velocity
        """, (axis_name, max_acceleration, max_velocity, actual_position, target_position, distance_to_go, homed, acceleration, velocity, machine_id))

    conn.commit()

for i in range(1, 21):
    machine_id = 81258856 + i  
    machine_name = f'EMPX{i}'  
    generate_machine_data(machine_id, machine_name)
    generate_axis_data(machine_id)

while True:
    
    for i in range(1, 21):
        machine_id = 81258856 + i
        generate_axis_data(machine_id)
    
    sleep(900)  # Sleep for 15 minutes before the next update

cursor.close()
conn.close()
