import django_filters
from .models import Producto

class ProductoFilter(django_filters.FilterSet):
    categoria = django_filters.BaseInFilter(field_name='categoria', lookup_expr='in')

    class Meta:
        model = Producto
        fields = ['categoria']
