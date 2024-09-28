from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/machines/', consumers.MachineDataConsumer.as_asgi()),
]
