from rest_framework.permissions import BasePermission

class PermisoPorRol(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            print("❌ Usuario no autenticado")
            return False

        rol = getattr(request.user, 'rol', None)
        permisos = {
            'admin': ['usuarios', 'productos', 'pedidos','notificaciones'],
            'cliente': ['catalogo', 'carrito', 'pedidos','notificaciones'],
            'delivery': ['pedidos','notificaciones']
        }

        view_name = getattr(view, 'basename', None)

        if not view_name and hasattr(view, 'queryset') and view.queryset is not None:
            view_name = view.queryset.model.__name__.lower() + 's'

        if not view_name:
            view_name = view.__class__.__name__.lower().replace('viewset', '')

        print(f"🔎 ROL: {rol} | VIEW_NAME: {view_name} | PERMITIDO: {view_name in permisos.get(rol, [])}")

        return view_name in permisos.get(rol, [])