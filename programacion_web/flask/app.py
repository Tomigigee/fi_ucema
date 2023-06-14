from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

prendas = {
    100: {"name": "Remera talle m", "price": 50},
    150: {"name": "Remera talle s", "price": 40}
}

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/prendas/")
def get_all_prendas():
    return render_template("prendas.html", prendas=prendas.items())

@app.get("/prendas/<int:id>")
def get_prenda(id):
    if id in prendas:
        prenda = prendas[id]
        return render_template('prenda.html', id=id, prenda=prenda)
    else:
        return ("no hay prenda", 404)

@app.get("/ventas/<int:id>")
def get_venta(id):
    return {"foo":1}

"""from flask import Flask, render_template
import requests
from markupsafe import escape 
prendas = [
    {"id":1, "tipo": "pantalon", "talle": 42},
    {"id":2, "tipo": "pantalon", "talle": 56}]

app = Flask(__name__) #Me refiero a la aplicacion por la palabra app. Instanciamos app

@app.get("/") #Le asociamos una ruta a app
def home(): #Es el metodo que me permite mostrar los datos que estan asociados a la pagina( en este caso ninguno)
    return render_template("home.html") #si no funciona habria que poner el path a home.html
    #return "<p>Te damos la bienvenida a Macowins, </p>"

@app.get("/prendas/")
def get_all_prendas():
    return render_template("prendas.html", prendas=prendas.items())

@app.get("/prendas/<int:id>")
def get_prenda(id):
    if id in prendas:
        prenda = prendas[id]
        return render_template('prenda.html', id=id, prenda=prenda)
    else:
        return ("no hay prenda", 404)

@app.get("/ventas/<int:id>")
def get_venta(id):
    return {"foo":1}

#Tarea: armar la ruta /prendas que muestre todos los items de prendas

@app.get("/prendas") # El @ es un decorador.
def mostrar_prendas():
    muestra = ""
    for prenda in prendas:
        muestra += f"Prenda {prenda['id']}: Tipo {prenda['tipo']}, Talle {prenda['talle']}<br>"
    return muestra
"""
#a = requests.get("https://<Flask 'app'>")"""

"""@app.get("/prendas") #con /prendas puedo usar un get para buscar las prendas o un post para agregar una prenda nueva. Todo lo que no sea mapeable como recurso no hay que usarlo si queremos hacer una API rest.
#con <id> puedo usar: Get para traer solo una prenda de id. Patch para modificar esa prenda.
def get_all_prendas():
    return f"<p>Mostrando todas las prendas</p>"
    """
"""
@app.get("/prendas/<id>")
def get_prenda(id): #saca el id desde la url
    return f"<p>Mostrando la prenda {escape(id)}</p>
"""