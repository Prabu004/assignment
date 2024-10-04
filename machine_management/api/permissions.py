from rest_framework.permissions import BasePermission

class IsSuperAdmin(BasePermission):
    """
    Allows access only to users in the SUPERADMIN group.
    """
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='SUPERADMIN').exists()

class IsManager(BasePermission):
    """
    Allows access only to users in the Manager group.
    """
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Manager').exists()

class IsSupervisor(BasePermission):
    """
    Allows access only to users in the Supervisor group.
    """
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Supervisor').exists()

class IsOperator(BasePermission):
    """
    Allows access only to users in the Operator group.
    """
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Operator').exists()
