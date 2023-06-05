import requests, json
"""
a) ¿Cuál es el dominio al que estamos consultando? 
El dominio que estamos consultando es https://pokeapi.co

b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué Content-Type? Obtené la información correspondiente al campo "forms".
 El status code es 200 (que quiere decir que esta todo bien). El Content-Type es application/json

c) Averigüá cuántos Pokemones almacena la API.
Almacena 20 pokemons.

d) ¿Cómo esperás que sea la URL para obtener las habilidades de los Pokemons (abilities)? ¿y cómo será la url para obtener la información sobre la habilidad 2?
Se esperaria que sea https://pokeapi.co/v2/abilities
Para obtener la habilidad 2 https://pokeapi.co/v2/abilities/2

f) Guardar los datos correspondientes a Pikachu y Sylveon en un archivo de nombre "ficha_tecnica_pokemon.txt".

g) Describí la arquitectura cliente-servidor y los roles de cada parte
"""


print(requests.get("https://pokeapi.co/api/v2/pokemon/pikachu"))
pikachu = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
print("el status code es", pikachu.status_code)
pokemons = requests.get("https://pokeapi.co/api/v2/pokemon") #c
datos_pokemons = pokemons.json() #c
headers = pikachu.headers
headers_pokemon = pokemons.json() #c
datos = pikachu.json()
#print(datos)
print(pikachu.json().keys()) #veo todas las llaves a las que puedo acceder
print(headers["Content-Type"]) #b, content type
print(pikachu.json()["forms"]) #b, forms. COMO ES UN DICCIONARIO TENGO QUE PONERLO ASI, SI FUERA UNA LISTA LO PONDRIA CON [0]
#print(headers_pokemon["results"])
#print(len(headers_pokemon["results"])) # c 
print(pokemons.json()["count"]) #obtenemos la cantidad de pokemons
#print(len(datos_pokemons))

#E
sylveon = requests.get("https://pokeapi.co/api/v2/pokemon/sylveon")

#str(pikachu.json()) Esto es otra forma de hacerlo
with open("ficha_tecnica_pokemon.txt", "wb") as ficha:
    ficha.write(pikachu.content)
    ficha.write(b"\n")
    ficha.write(sylveon.content)
    

"""a) ¿Cuál es el dominio al que estamos consultando?
 https://jsonplaceholder.typicode.com

b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué Content-Type? 
El status code es 200.
El content type es application/json

c) Agregar un contenido cuyo userId es 11 y su id es 2 con un nuevo título e indicando que está completo (completed).


d) En la arquitectura cliente-servidor ¿Qué características tiene el cliente?"""

print(requests.get("https://jsonplaceholder.typicode.com/todos")) #Nos da el status code
respuesta = requests.get("https://jsonplaceholder.typicode.com/todos")
datos = respuesta.json()
print(datos)
headers = respuesta.headers
print(headers["Content-Type"])
print(type(respuesta.json())) #Nos dice que el json es una lista
print(len(respuesta.json()))

#C
print(respuesta.json()[5])
data = {"userId": 11, "id": 2, "title": "quis ut nam facilits", "completed": True}
headers = {"Content-Type": "application/json; charset=utf-8"}

a = requests.post("https://jsonplaceholder.typicode.com/todos", data = json.dumps(data), headers = headers )

print(a.json())