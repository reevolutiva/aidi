from flask import Flask, request

from langchain.prompts import PromptTemplate

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
    body = request.json
    target = body["target"]
    action = body["action"]
    contentido = body["content"]

    print(body)
    
    # Crear un course config
    if target == "course-setting" and action == "create":
         course_setting_generate(contentido)
         print("Crea propt")
        #crearFirstPrompt()

    return 'OK', 200


def course_setting_generate(prompt):
    template = """
          El curso trata sobre {de_que_trata}.
          Los participantes de curso y sus metas son: {participantes_y_metas}.
          Los conocmientos necesarios antes de tomar el curso son: {conocmientos_base}.
          El curso se creare en el idioma: {idioma}.
          La modalidad del curso sera: {modalidad}.

          ¿Optimiza de forma masiva el aprendisaje en la plataforma? {mooc}.
          ¿Optimiza el curso para aprendizaje basado en grupos pequeño? {project_bases}.
          ¿Generar prototipos de tareas para posterior elaboracion? {task_prototype}.

          El curso durara {weeks} semanas.
          El nivel del curso sera {course_level}
          """
    res = PromptTemplate.from_template(template)

    res.format(adjetive="de_que_trata", content=prompt["de_que_trata"])
    res.format(adjetive="participantes_y_metas", content=prompt["participantes_y_metas"])
    res.format(adjetive="conocmientos_base", content=prompt["conocmientos_base"])
    res.format(adjetive="idioma", content=prompt["idioma"])
    res.format(adjetive="mooc", content=prompt["mooc"])
    res.format(adjetive="project_bases", content=prompt["project_bases"])
    res.format(adjetive="task_prototype", content=prompt["task_prototype"])
    res.format(adjetive="weeks", content=prompt["weeks"])
    res.format(adjetive="course_level", content=prompt["course_level"])


    return res