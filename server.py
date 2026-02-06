from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)   # ← ESTA LÍNEA DEBE IR ANTES DE CUALQUIER @app.route

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    text_to_analyze = request.form["textToAnalyze"]
    result = emotion_detector(text_to_analyze)

    # Manejo seguro cuando la API falla

    # -------------------------------
    # Si la función devuelve None o dominant_emotion es None → entrada inválida

    if result is None or result.get("dominant_emotion") is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    response_text = (
        f"Para la declaración dada, la respuesta del sistema es "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} y 'sadness': {sadness}. "
        f"La emoción dominante es {dominant}."
    )

    return response_text

if __name__ == "__main__":
    app.run(host="localhost", port=5000)