import logging
from rest_framework import viewsets
from core.permissions import PermisoPorRol

logger = logging.getLogger(__name__)

class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [PermisoPorRol]
    basename = ''
    filter_by_user = False

    def get_queryset(self):
        if getattr(self, 'filter_by_user', False):
            return self.queryset.filter(usuario=self.request.user)
        return self.queryset

    def list(self, request, *args, **kwargs):
        logger.info(f"[{request.user.rol}] accedió a {self.basename} (LIST)")
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        rol = getattr(request.user, 'rol', 'anónimo')
        usuario = getattr(request.user, 'username', 'anónimo')

        logger.info(f"[{usuario} | {rol}] creó algo en {self.basename}: {request.data}")
        return super().create(request, *args, **kwargs)
