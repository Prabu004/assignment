from django.urls import path
from . import views
from .views import websocket_test_view

urlpatterns = [
    path('user/', views.get_user, name='get_user'),
    path('machines/', views.machine_list_create, name='machine_list_create'),
    path('machines/<int:pk>/', views.machine_update_delete, name='machine_update_delete'),
    path('machines/<int:machine_id>/history/', views.machine_history, name='machine_history'),
    path('test-websocket/', websocket_test_view, name='websocket_test'),
]
