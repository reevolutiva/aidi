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


from your_module import crearFirstPrompt  # Asegúrate de que esta ruta de importación sea correcta

@app.route('/chatdev', methods=['POST'])
def aidi_create():
    body = request.json
    target = body["target"]
    action = body["action"]
    contentido = body["content"]

    print(body)
    
    if target == "course-setting" and action == "create":
        crearFirstPrompt()

    return 'OK', 200
    


    return 'OK', 200


