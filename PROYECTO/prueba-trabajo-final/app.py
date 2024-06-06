from flask import Flask, render_template, request, jsonify
import cv2
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)
app.debug = False

# Cargar el clasificador de rostros pre-entrenado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Función para detectar emociones en una imagen
def detectar_emociones(imagen):
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Detectar rostros en la imagen
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Iterar sobre cada rostro detectado
    for (x, y, w, h) in faces:
        # Extraer la región de interés (ROI) que contiene el rostro
        roi_gray = gray[y:y+h, x:x+w]

        # Realizar la predicción de la emoción en la región de interés
        emocion = predecir_emocion(roi_gray)  # Suponiendo que tienes una función para predecir la emoción

        # Imprimir la emoción detectada en la consola
        print("Emoción detectada:", emocion)

        # Dibujar un rectángulo alrededor del rostro y mostrar la emoción detectada en la imagen
        cv2.rectangle(imagen, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(imagen, emocion, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Mostrar la imagen con los rostros y las emociones detectadas
    cv2.imshow('Emociones detectadas', imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Función para predecir la emoción en una región de interés (ROI)
def predecir_emocion(roi_gray):
    # Aquí deberías incluir la lógica para predecir la emoción en la ROI
    # Puedes utilizar tu modelo pre-entrenado u otro enfoque de detección de emociones
    # Retorna la emoción detectada como una cadena (por ejemplo: "feliz", "triste", "enojado", etc.)
    # Por ahora, simplemente retornamos una cadena genérica para fines de ejemplo
    return "Emoción desconocida"

# Función para obtener recomendaciones de música basadas en la emoción detectada
def obtener_recomendaciones(emocion):
    # Configurar las credenciales de la API de Spotify
    client_id = ''
    client_secret = ''

    # Configurar el cliente de autenticación
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Parámetros de la solicitud de recomendaciones
    parametros = {
        "seed_genres": "pop",  # Género de música para basar las recomendaciones
        "target_valence": 0.8,  # Valencia objetivo (emoción positiva)
        "limit": 5  # Número máximo de canciones recomendadas
    }

    try:
        # Obtener las recomendaciones de música
        recomendaciones = sp.recommendations(**parametros)
        print("Recomendaciones de Spotify:", recomendaciones)
    except spotipy.exceptions.SpotifyException as e:
        print("Error al obtener recomendaciones:", e)
        recomendaciones = None

    return recomendaciones

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar_imagen', methods=['POST'])
def procesar_imagen():
    # Aquí debes agregar la lógica para procesar la imagen, detectar emociones y obtener recomendaciones de música
    # El código que ya tienes en tu archivo app.py puede ir aquí

    # Ejemplo de datos de emociones y recomendaciones
    emociones_html = "<p>Emociones detectadas: Feliz, Triste</p>"
    recomendaciones_html = "<p>Canciones recomendadas: Song 1, Song 2, Song 3</p>"

    return jsonify({'emociones_html': emociones_html, 'recomendaciones_html': recomendaciones_html})

if __name__ == '__main__':
    app.run(debug=True)
