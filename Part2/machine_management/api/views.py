from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Machine
from .serializers import MachineSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

def has_permission(user, action):
    if user.role == 'superadmin':
        return True
    if user.role == 'manager':
        return action in ['list', 'create']
    if user.role == 'supervisor':
        return action in ['list', 'create', 'retrieve', 'update']
    if user.role == 'operator':
        return action in ['list', 'retrieve']
    return False

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    user_data = {
        'username': request.user.username,
        'role': request.user.role
    }
    return Response(user_data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def machine_list_create(request):
    action = request.method.lower()
    
    if not has_permission(request.user, action):
        return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        machines = Machine.objects.all()
        serializer = MachineSerializer(machines, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        if request.user.role == 'manager' and 'tool_in_use' in request.data:
            return Response({'detail': 'Permission denied for tool_in_use.'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = MachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'detail': 'Invalid data.', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def machine_update_delete(request, pk):
    try:
        machine = Machine.objects.get(pk=pk)
    except Machine.DoesNotExist:
        return Response({'detail': 'Machine not found.'}, status=status.HTTP_404_NOT_FOUND)

    action = request.method.lower()
    if not has_permission(request.user, action):
        return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = MachineSerializer(machine)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MachineSerializer(machine, data=request.data)
        if serializer.is_valid():
            if request.user.role == 'operator' and 'tool_in_use' in request.data:
                return Response({'detail': 'Permission denied for tool_in_use.'}, status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data)
        return Response({'detail': 'Invalid data.', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        machine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def machine_history(request, machine_id):
   
    return Response({'detail': 'Machine history not implemented.'})


def websocket_test_view(request):
    return render(request, 'api/test_websocket.html')