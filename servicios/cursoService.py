import requests

'''

Para POST
cur = {"nombre":"Susana",
       "estado":True}

       
PARA PUT
cur = {"idCurso": 18,
        "nombre":"Milena",
       "estado":True}
'''

def insertCurso(curso):
    res = requests.post("http://educate.runasp.net/api/curso", json=curso)
    return res.status_code

def getCursos():
    res = requests.get("http://educate.runasp.net/api/curso")
    return res.json()

def getCurso(id):
    res = requests.get(f"http://educate.runasp.net/api/curso/{id}")
    return res.json()

def modifyCurso(id, curso):
    res = requests.put(f"http://educate.runasp.net/api/curso/{id}", json=curso)
    return res.status_code

def unableCurso(id):
    res = requests.delete(f"http://educate.runasp.net/api/curso/{id}")
    return res.status_code
