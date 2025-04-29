from rest_framework.permissions import AllowAny

from core.viewsets import BaseViewSet
from .models import Categoria
from .serializers import CategoriaSerializer


# Create your views here.
class CategoriaViewSet(BaseViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    basename = 'categorias'

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]   # Si solo quieres liberar el listado
        return super().get_permissions()