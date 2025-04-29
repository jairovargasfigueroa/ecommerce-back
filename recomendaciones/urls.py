# from django.urls import path
# from .views import RecomendacionAPIView, test_recomendaciones

# urlpatterns = [
#     path('', RecomendacionAPIView.as_view()),
#     path('test/', test_recomendaciones),
# ]
from django.urls import path
from .views import RecomendacionAprioriAPIView

urlpatterns = [
    path('api/recomendaciones/', RecomendacionAprioriAPIView.as_view()),
]
