import requests

print(requests.get("https://pokeapi.co/api/v2/pokemon/ditto")) 
respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/ditto") 
print(respuesta.json())
datos = respuesta.json()
print(len(datos)) #en cuantas orgs esta el usuario
#print(datos)
print(respuesta.headers)
print(datos.keys())

print("el content type es:", respuesta.headers["Content-Type"])
print(respuesta.status_code)
print("la cantidad de habilidades es:", len(datos["abilities"]))
"""
1) Protocolo: https://
Dominio: pokeapi.co (https://______/----)
Recursos: https://______/-----) ---: son las cosas que puedo consultar en la base de datos.
2) La respuesta que se obtiene es un Respone [200]
3)El content Type es application/json
4) El status code es 200
5) Tiene 2 habilidades 
"""

#Para que una api sea rest debe 
#http solo soporta TEXTO
#El numero que le sigue al recurso (si es que hay) es el ID, y es basicamente el numero de la fila.

r = requests.get("https://macowins-server.herokuapp.com/prendas?tipo=pantalon")
# ? y = (query params) son las claves que le paso a la api en la url para filtrar la busqueda.
# ?: Busca
# =: igualdad
#Tambien se pueden concatenar filtrados usando &.
a = requests.get("https://macowins-server.herokuapp.com/prendas?talle=40&tipo=pantalon")
#Delete: borra un item seleccionado.
#Post: se escriben datos desde 0.
#Patch: se sobreescriben datos.
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data =  { "tipo": "chomba", "talle": "XS" }
b = requests.post('https://macowins-server.herokuapp.com/prendas', data=json.dumps(data), headers=headers)

"""
Para cada url de una api rest hay verbos asociados.
GET /ventas/: consultar todos (listar)
DELETE /ventas/: borrar todos
POST /ventas/: crear uno
POST /ventas/1 crear uno con ID (QMP no lo soporta)
GET /ventas/1: consultar uno
PUT /ventas/1: modificar uno
DELETE /ventas/1: eliminar uno
"""