from flask import Flask, request
from langchain import PromptTemplate
import os

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    # Aquí es donde procesaremos los argumentos enviados en el cuerpo de la petición.
    # Por ahora, simplemente imprimiremos los argumentos para verificar que todo funciona correctamente.
 
    body = request.json

    res = course_setting_generate(body)

    task = f"{res}"

    comand = create_prompt_chat_dev( "chatDevCore.py" , "ReevolutivaResumen" , {"name":"DesingInstrutional","task":task}) 
    
    print(comand)

    #os.system(comand)
    
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


def create_prompt_chat_dev( core , config , body ):

    res = ""

    for name, value in body.items():
        res = res + f'--{name} "{value}" '
    
    response = f'python {core} --config "{config}" {res}'

    return response


def course_setting_generate(prompt):
    template = "El curso trata sobre {de_que_trata}. Los participantes de curso y sus metas son: {participantes_y_metas}. Los conocmientos necesarios antes de tomar el curso son: {conocmientos_base}. El curso se creare en el idioma: {idioma}. La modalidad del curso sera: {curso_modalidad}. ¿Optimiza de forma masiva el aprendisaje en la plataforma? {mooc}. ¿Optimiza el curso para aprendizaje basado en grupos pequeño? {project_based}. ¿Generar prototipos de tareas para posterior elaboracion? {task_prototypes}. El curso durara {weeks} semanas. El nivel del curso sera {course_level}"
    res = PromptTemplate.from_template(template)

    for key in prompt:
         prompt[key] = prompt[key].replace('\n', '\\n')

    formatted_prompt = res.format( de_que_trata=prompt["de_que_trata"],
                                   participantes_y_metas=prompt["participantes_y_metas"],
                                   conocmientos_base=prompt["conocmientos_base"],
                                   curso_modalidad=prompt["curso_modalidad"],
                                   idioma=prompt["idioma"],
                                   mooc=prompt["mooc"],
                                   project_based=prompt["project_based"],
                                   task_prototypes=prompt["task_prototypes"],
                                   weeks=prompt["weeks"],
                                   course_level=prompt["course_level"])
   
    return formatted_prompt



