import requests

'''

Para POST
asig = {"estudianteId": 1,
       "profesorCursoId": 1,
       "estado": True}

       
PARA PUT
asig = {"idAsignacion":1,
        "estudianteId": 1,
       "profesorCursoId": 1,
       "estado": True}
'''

def insertAsignacion(asignacion):
    res = requests.post("http://educate.runasp.net/api/asignacion", json=asignacion)
    return res.status_code

def getAsignaciones():
    res = requests.get("http://educate.runasp.net/api/asignacion")
    return res.json()

def getAsignacion(id):
    res = requests.get(f"http://educate.runasp.net/api/asignacion/{id}")
    return res.json()

def modifyAsignacion(id, asignacion):
    res = requests.put(f"http://educate.runasp.net/api/asignacion/{id}", json=asignacion)
    return res.status_code

def unableAsignacion(id):
    res = requests.delete(f"http://educate.runasp.net/api/asignacion/{id}")
    return res.status_code

asig = {"estudianteId":2, "profesorCursoId": 1, "estado":True}


