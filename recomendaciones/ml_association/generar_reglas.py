import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import pickle
import django
import os
import sys

# Configurar entorno Django
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()


from pedidos.models import Pedido

print("🚀 Generando reglas de recomendación con Apriori...")

# 1️⃣ Extraer transacciones desde los pedidos reales
transacciones = []

for pedido in Pedido.objects.all():
    productos = [item.producto.nombre for item in pedido.items.all() if item.producto]
    if productos:
        transacciones.append(productos)


if not transacciones:
    print("⚠️ No se encontraron pedidos con productos. Abortando...")
    exit()

# 2️⃣ One-Hot Encoding
all_items = set(item for t in transacciones for item in t)
encoded_vals = [{item: (item in trans) for item in all_items} for trans in transacciones]

df = pd.DataFrame(encoded_vals)

# 3️⃣ Aplicar Apriori
frequent_items = apriori(df, min_support=0.03, use_colnames=True)
rules = association_rules(frequent_items, metric="lift", min_threshold=1.0)

# 4️⃣ Guardar reglas generadas
ruta_reglas = os.path.join(BASE_DIR, 'recomendaciones', 'ml_association', 'reglas.pkl')

with open(ruta_reglas, 'wb') as f:
    pickle.dump(rules, f)

print(f"✅ Reglas generadas correctamente: {len(rules)} reglas guardadas en {ruta_reglas}")
