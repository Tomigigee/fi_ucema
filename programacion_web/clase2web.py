import requests

print(requests.get("https://pokeapi.co/api/v2/pokemon/ditto")) 
respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/ditto") 
datos = respuesta.json()
print(len(datos)) #en cuantas orgs esta el usuario
#print(datos)
print(respuesta.headers)
print("el content type es:", respuesta.headers["Content-Type"])
print("la cantidad de habilidades es:", len(datos["abilities"]))
"""
1)
2) La respuesta que se obtiene es un Respone [200]
3)El content Type es application/json
4) El status code es 200
5) Tiene 2 habilidades 
"""

