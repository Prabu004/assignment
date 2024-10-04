from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Machine, Axis
from .serializers import MachineSerializer, AxisSerializer
from rest_framework import status
from .permissions import IsSuperAdmin, IsManager, IsSupervisor, IsOperator
from rest_framework.permissions import BasePermission
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your views here.

@api_view(['POST'])
def generate_token(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.get(username=username)
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists()

class IsSupervisor(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Supervisor').exists()

class IsOperator(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Operator').exists()

class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='SUPERADMIN').exists()



@api_view(['GET', 'POST'])
@permission_classes([IsManager | IsSuperAdmin])
def machine_list(request):
    if request.method == 'GET':
        machines = Machine.objects.all()
        serializer = MachineSerializer(machines, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsManager | IsSuperAdmin])
def machine_detail(request, pk):
    try:
        machine = Machine.objects.get(pk=pk)
    except Machine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MachineSerializer(machine)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MachineSerializer(machine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        machine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
