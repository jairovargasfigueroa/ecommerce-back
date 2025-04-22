import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

import speech_recognition as sr
from pydub import AudioSegment
import tempfile
AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"


@csrf_exempt
def asistente_voz(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    try:
        data = json.loads(request.body)
        texto = data.get('texto', '')
    except Exception as e:
        return JsonResponse({'error': 'JSON inválido', 'detalle': str(e)}, status=400)

    try:
        respuesta = requests.post('http://localhost:8001/interpretar/', json={'texto': texto})
        # respuesta = requests.post('http://fastapi:8001/interpretar/', json={'texto': texto}) con docker
        resultado = respuesta.json()
    except Exception as e:
        return JsonResponse({'error': 'Error al conectar con el microservicio', 'detalle': str(e)}, status=500)

    return JsonResponse(resultado)


@csrf_exempt
def audio_a_texto(request):
    if request.method != 'POST' or 'audio' not in request.FILES:
        return JsonResponse({'error': 'Se requiere un archivo de audio'}, status=400)

    audio_file = request.FILES['audio']

    try:
        # 🔍 Verificar si el ejecutable realmente existe
        import os
        print("🔍 FFmpeg path existe:", os.path.exists(AudioSegment.converter))
        print("👉 Ruta actual de FFmpeg:", AudioSegment.converter)

        # ⚙️ Convertir el archivo a WAV usando pydub
        audio = AudioSegment.from_file(audio_file)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav:
            audio.export(temp_wav.name, format="wav")

            # 🎧 Usar speech_recognition para transcribir
            recognizer = sr.Recognizer()
            with sr.AudioFile(temp_wav.name) as source:
                audio_data = recognizer.record(source)

            texto = recognizer.recognize_google(audio_data, language="es-ES")
            return JsonResponse({'texto': texto})

    except sr.UnknownValueError:
        return JsonResponse({'error': 'No se pudo entender el audio'}, status=422)
    except sr.RequestError as e:
        return JsonResponse({'error': f'Error del servicio de reconocimiento: {e}'}, status=503)
    except Exception as e:
        import traceback
        print("🔧 ERROR COMPLETO EN CONSOLA:")
        traceback.print_exc()
        return JsonResponse({'error': f'Error inesperado: {str(e)}'}, status=500)
