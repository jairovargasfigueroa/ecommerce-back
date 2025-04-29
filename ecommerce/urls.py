"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path,re_path
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),   
    path('api/productos/', include('productos.urls')),
    path('api/carrito/', include('carrito.urls')),  # Rutas para la app carrito
    path('api/usuarios/', include('usuarios.urls')),
    path('api/pedidos/', include('pedidos.urls')),
    path('api/pagos/', include('pagos.urls')),
    path('', include('recomendaciones.urls')),
    path('api/notificaciones/', include('notificaciones.urls')),

    # path('api/recomendaciones/', include('recomendaciones.urls')),
    re_path(r'^.*$', TemplateView.as_view(template_name="index.html")),

]

# Sirve archivos media (como imágenes) durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
