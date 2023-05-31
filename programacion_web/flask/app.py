from flask import Flask, render_template
import requests
from markupsafe import escape 
prendas = [
    {"id":1, "tipo": "pantalon", "talle": 42},
    {"id":2, "tipo": "pantalon", "talle": 56}]

app = Flask(__name__) #Me refiero a la aplicacion por la palabra app. Instanciamos app

@app.get("/") #Le asociamos una ruta a app
def home(): #Es el metodo que me permite mostrar los datos que estan asociados a la pagina( en este caso ninguno)
    return render_template("home.html")
    #return "<p>Te damos la bienvenida a Macowins, </p>"

#Tarea: armar la ruta /prendas que muestre todos los items de prendas
"""@app.get("/prendas") # El @ es un decorador.
def mostrar_prendas():
    muestra = ""
    for prenda in prendas:
        muestra += f"Prenda {prenda['id']}: Tipo {prenda['tipo']}, Talle {prenda['talle']}<br>"
    return muestra
#a = requests.get("https://<Flask 'app'>")"""

"""@app.get("/prendas") #con /prendas puedo usar un get para buscar las prendas o un post para agregar una prenda nueva. Todo lo que no sea mapeable como recurso no hay que usarlo si queremos hacer una API rest.
#con <id> puedo usar: Get para traer solo una prenda de id. Patch para modificar esa prenda.
def get_all_prendas():
    return f"<p>Mostrando todas las prendas</p>"
    """

@app.get("/prendas/<id>")
def get_prenda(id): #saca el id desde la url
    return f"<p>Mostrando la prenda {escape(id)}</p>"