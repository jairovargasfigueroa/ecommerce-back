from fastapi import FastAPI
from pydantic import BaseModel
import spacy

app = FastAPI()
nlp = spacy.load("es_core_news_sm")  # o "es_core_news_md" si querés más precisión

class TextoEntrada(BaseModel):
    texto: str

@app.post("/interpretar/")
async def interpretar(entrada: TextoEntrada):
    texto = entrada.texto.lower()
    doc = nlp(texto)

    # Clasificar tipo de acción
    if any(pal in texto for pal in ['añade', 'agrega', 'pon']):
        tipo = 'agregar'
    elif any(pal in texto for pal in ['elimina', 'quita', 'borra']):
        tipo = 'eliminar'
    elif any(pal in texto for pal in ['buscar', 'muéstrame', 'ver', 'enséñame']):
        tipo = 'buscar'
    elif 'compra' in texto or 'completa' in texto:
        tipo = 'comprar'
    else:
        tipo = 'desconocido'

    # Extraer múltiples productos con cantidad
    productos = []
    cantidad_actual = 1
    PALABRAS_IGNORADAS = {"carrito", "del", "al", "la", "el", "de", "porfa", "por", "favor"}

    for i, token in enumerate(doc):
        if token.like_num:
            try:
                cantidad_actual = int(token.text)
            except ValueError:
                continue
        elif token.pos_ in ("NOUN", "PROPN") and token.text not in PALABRAS_IGNORADAS:
            productos.append({
                "nombre": token.text,
                "cantidad": cantidad_actual
            })
            cantidad_actual = 1  # Reiniciar para el próximo

    return {
        "tipo": tipo,
        "productos": productos
    }
