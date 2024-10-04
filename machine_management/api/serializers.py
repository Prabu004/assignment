from rest_framework import serializers
from .models import Machine, Axis

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

class AxisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Axis
        fields = '__all__'
