# Generated by Django 5.1.1 on 2024-10-04 06:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_id', models.BigIntegerField(unique=True)),
                ('machine_name', models.CharField(max_length=100)),
                ('tool_capacity', models.IntegerField()),
                ('tool_offset', models.FloatField()),
                ('feedrate', models.FloatField()),
                ('tool_in_use', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Axis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('axis_name', models.CharField(max_length=10)),
                ('max_acceleration', models.FloatField()),
                ('max_velocity', models.FloatField()),
                ('actual_position', models.FloatField()),
                ('target_position', models.FloatField()),
                ('distance_to_go', models.FloatField()),
                ('homed', models.BooleanField(default=False)),
                ('acceleration', models.FloatField()),
                ('velocity', models.FloatField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.machine')),
            ],
            options={
                'unique_together': {('axis_name', 'machine')},
            },
        ),
    ]
