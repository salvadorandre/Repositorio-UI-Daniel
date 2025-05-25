import requests

'''

Para POST
est = {"nombre":"Susana",
       "apellido":"Barrera",
       "promedio":10,
       "edad": 19,
       "grado":"6to",
       "estado":True}

       
PARA PUT
est = {"idEstudiante": 18,
        "nombre":"Milena",
       "apellido":"Barrera",
       "promedio":10,
       "edad": 19,
       "grado":"6to",
       "estado":True}
'''

def insertEstudiante(estudiante):
    res = requests.post("http://educate.runasp.net/api/estudiante", json=estudiante)
    return res.status_code

def getEstudiantes():
    res = requests.get("http://educate.runasp.net/api/estudiante")
    return res.json()

def getEstudianteById(id):
    res = requests.get(f"http://educate.runasp.net/api/estudiante/{id}")
    return res.json()

def modifyEstudiante(id, estudiante):
    res = requests.put(f"http://educate.runasp.net/api/estudiante/{id}", json=estudiante)
    return res.status_code

def unableEstudiante(id):
    res = requests.delete(f"http://educate.runasp.net/api/estudiante/{id}")
    return res.status_code

