import pickle
import pandas as pd
import os

# Ruta del archivo generado
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
ruta_reglas = os.path.join(BASE_DIR, 'recomendaciones', 'ml_association', 'reglas.pkl')

# Cargar reglas guardadas
with open(ruta_reglas, 'rb') as f:
    rules = pickle.load(f)

# Convertir a DataFrame si no lo está
if not isinstance(rules, pd.DataFrame):
    rules = pd.DataFrame(rules)

# Ordenar por lift descendente
rules_sorted = rules.sort_values(by='lift', ascending=False)

# Seleccionar top N reglas
top_n = 20
top_rules = rules_sorted.head(top_n)

print(f"✅ Mostrando las top {top_n} reglas con mayor lift:\n")

for idx, row in top_rules.iterrows():
    antecedents = ', '.join(row['antecedents'])
    consequents = ', '.join(row['consequents'])
    print(f"- Si compra: [{antecedents}] → también compra: [{consequents}]")
    print(f"  → soporte: {row['support']:.2f}, confianza: {row['confidence']:.2f}, lift: {row['lift']:.2f}\n")
