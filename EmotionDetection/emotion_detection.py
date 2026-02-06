import requests
import json

def emotion_detector(text_to_analyze):

    # URL del endpoint de la API
    url = "https://sn-watson-emotion.labs.skills.network/emotion"

    # Payload que se envía a la API
    payload = {"text": text_to_analyze}

    # Llamada al servidor
    response = requests.post(url, json=payload)

    # -------------------------------
    # MANEJO DE ERRORES (TAREA 7)
    # -------------------------------
    # Si el usuario envía texto vacío, la API devuelve status_code = 400
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Si la API falla por otra razón
    if response.status_code != 200:
        return None

    # Procesar respuesta válida
    result = response.json()

    # Extraer emociones
    anger = result["emotionPredictions"][0]["emotion"]["anger"]
    disgust = result["emotionPredictions"][0]["emotion"]["disgust"]
    fear = result["emotionPredictions"][0]["emotion"]["fear"]
    joy = result["emotionPredictions"][0]["emotion"]["joy"]
    sadness = result["emotionPredictions"][0]["emotion"]["sadness"]

    # Determinar emoción dominante
    emotions = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }

    dominant_emotion = max(emotions, key=emotions.get)

    # Devolver diccionario final
    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }