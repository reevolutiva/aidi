from flask import Flask, request

import os

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    # Aquí es donde procesaremos los argumentos enviados en el cuerpo de la petición.
    # Por ahora, simplemente imprimiremos los argumentos para verificar que todo funciona correctamente.
 
    body = request.json

    comand = create_prompt_chat_dev( "chatDevCore.py" , body) 

    print(comand)
   
    #comando = f'python chatDevCore.py  --task "{task}" --name "{name}"'

    #print(comando)

    #os.system(comando)
    
    return 'OK', 200


@app.route('/chatdev', methods=['POST'])
def aidi_create():
    body = request.json
    target = body["target"]
    action = body["action"]
    contentido = body["content"]

    #print(body)
    
    # Crear un course config
    if target == "course-setting" and action == "create":
        ##res = course_setting_generate(contentido)
        print(res)
        #crearFirstPrompt()

    return 'OK', 200


def create_prompt_chat_dev( core , body):

    res = ""

    for name, value in body.items():
        res = res + f"--{name} '{value}' "
    
    response = f"python {core} {res}"

    return response
