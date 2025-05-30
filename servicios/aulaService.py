import requests

'''

Para POST
profCur = {"profesorId": 1,
       "cursoId": 1,
       "estado": True}

       
PARA PUT
profCur = {"idProfesorCurso": 18,
        "profesorId":1,
        "cursoId":1,
       "estado":True}
'''

def insertAula(profCurso):
    res = requests.post("http://educate.runasp.net/api/asignacionprofesor", json=profCurso)
    return res.status_code

def getAulas():
    res = requests.get("http://educate.runasp.net/api/asignacionprofesor")
    return res.json()

def getAula(id):
    res = requests.get(f"http://educate.runasp.net/api/asignacionprofesor/{id}")
    return res.json()

def getTotalAula(id):
    id_real = id
    res = requests.get(f"http://educate.runasp.net/api/ViewAula?activo=true")   
    for curso in res.json():
        if curso["idAula"] == id_real:
            return curso["totalEstudiantes"]


def modifyAula(id, profCurso):
    res = requests.put(f"http://educate.runasp.net/api/asignacionprofesor/{id}", json=profCurso)
    return res.status_code

def unableAula(id):
    res = requests.delete(f"http://educate.runasp.net/api/asignacionprofesor/{id}")
    return res.status_code
