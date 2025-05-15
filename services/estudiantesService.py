import requests

baseURL = "http://educate.runasp.net/api/estudiante"

def getEstudiantes():
    return requests.get(baseURL).json()

def createEstudiante(estudiante):
    res = requests.post(baseURL, json=estudiante)
    print(res.status_code)

def updateEstudiante(estId, estudiante):
    res = requests.put(f"{baseURL}/{estId}", json=estudiante)
    print(res.status_code)

def inhabilitarEstudiante(estId, estudiante):
    return requests.put(f"{baseURL}/{estId}", json=estudiante).json()
    
def insertarDatos(tabla):
    datos = getEstudiantes()
    
    for dato in datos:
       tabla.insert("", "end", values=(dato["idEstudiante"], 
                                       dato["nombre"], 
                                       dato["apellido"], 
                                       dato["promedio"], 
                                       dato["edad"], 
                                       dato["grado"], 
                                       dato["estado"], 
                                       dato["asignacion"]))
                    
