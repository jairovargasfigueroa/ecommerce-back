from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LoginView, UsuarioViewSet
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'', UsuarioViewSet, basename='usuario')

urlpatterns = [

    path('login/', LoginView.as_view(), name='custom_login'),


    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Agregamos las rutas del router al final
urlpatterns += router.urls
