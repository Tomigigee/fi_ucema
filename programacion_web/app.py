from flask import Flask

prendas = [
    {"id":1, "tipo": "pantalon", "talle": 42},
    {"id":2, "tipo": "pantalon", "talle": 56}]
app = Flask(__name__) #Me refiero a la aplicacion por la palabra app.

@app.get("/")
def home():
    return "<p>Te damos la bienvenida a Macowins, </p>"

#Tarea: armar la ruta /prendas que muestre todos los items de prendas