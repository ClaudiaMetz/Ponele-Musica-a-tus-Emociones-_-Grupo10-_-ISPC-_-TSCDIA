from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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
