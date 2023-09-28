import json

from flask import Flask, request
app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    # Aquí es donde procesaremos los argumentos enviados en el cuerpo de la petición.
    # Por ahora, simplemente imprimiremos los argumentos para verificar que todo funciona correctamente.
    print(request)
    print(request.json)
    return 'OK', 200


@app.route('/chatdev', methods=['POST'])
def aidi_create():
    contenido = request.json
    print(contenido)
    print(contenido.content)
    return 'OK', 200


