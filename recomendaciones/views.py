
# from rest_framework.views import APIView
# from rest_framework.response import Response
# import pickle

# # Cargar las reglas una sola vez
# with open('ml_association/reglas.pkl', 'rb') as f:
#     reglas = pickle.load(f)

# class RecomendacionAprioriAPIView(APIView):
#     authentication_classes = []
#     permission_classes = []

#     def post(self, request):
#         carrito = request.data.get('productos', [])
#         recomendaciones = set()

#         for _, row in reglas.iterrows():
#             if set(row['antecedents']).issubset(carrito):
#                 recomendaciones.update(row['consequents'])

#         from productos.models import Producto
#         productos_recomendados = Producto.objects.filter(nombre__in=recomendaciones)
#         from productos.serializers import ProductoSerializer
#         serializer = ProductoSerializer(productos_recomendados, many=True)
        # return Response({"recomendaciones": serializer.data})
from rest_framework.views import APIView
from rest_framework.response import Response
import pickle
import os

# Ruta absoluta al archivo de reglas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ruta_reglas = os.path.join(BASE_DIR, 'recomendaciones', 'ml_association', 'reglas.pkl')

with open(ruta_reglas, 'rb') as f:
    reglas = pickle.load(f)
    

class RecomendacionAprioriAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        carrito = request.data.get('productos', [])
        recomendaciones = set()
        print("Reglas del modelo",reglas)
        for _, row in reglas.iterrows():
            if set(row['antecedents']).issubset(carrito):
                recomendaciones.update(row['consequents'])

        from productos.models import Producto
        productos_recomendados = Producto.objects.filter(nombre__in=recomendaciones)
        from productos.serializers import ProductoSerializer
        serializer = ProductoSerializer(productos_recomendados, many=True)

        return Response({"recomendaciones": serializer.data})
        
