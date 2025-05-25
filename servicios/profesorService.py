import requests

'''

Para POST
prof = {"nombre":"Susana",
       "edad": 19,
       "capacidadEstudiantes":50,
       "estado":True}

       
PARA PUT
est = {"idProfesor": 18,
        "nombre":"Milena",
       "edad": 19,
        "capacidadEstudiantes":50,
       "estado":True}
'''

def insertProfesor(profesor):
    res = requests.post("http://educate.runasp.net/api/profesor", json=profesor)
    return res.status_code

def getProfesores():
    res = requests.get("http://educate.runasp.net/api/profesor")
    return res.json()

def getProfesor(id):
    res = requests.get(f"http://educate.runasp.net/api/profesor/{id}")
    return res.json()

def modifyProfesor(id, profesor):
    res = requests.put(f"http://educate.runasp.net/api/profesor/{id}", json=profesor)
    return res.status_code

def unableProfesor(id):
    res = requests.delete(f"http://educate.runasp.net/api/profesor/{id}")
    return res.status_code
