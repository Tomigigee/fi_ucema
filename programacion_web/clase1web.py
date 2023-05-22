import requests

respuesta = requests.get("https://api.github.com/users/ajvelezrueda/orgs") 
datos = respuesta.json()
print(len(datos)) #en cuantas orgs esta el usuario

print(respuesta.headers)