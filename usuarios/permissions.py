from rest_framework.permissions import BasePermission

class EsAdministrador(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 'administrador'

class EsCliente(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 'cliente'

class EsDelivery(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 'delivery'
