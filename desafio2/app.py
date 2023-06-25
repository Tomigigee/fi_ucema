from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder='static')

productos = {
    1: {"name": "shampoo solido", "Stock": 5, "precio_unitario": 300},
    2: {"name": "crema de manos","Stock": 6, "precio_unitario": 600}
}


@app.get("/") #Le asociamos una ruta a app
def home(): #Es el metodo que me permite mostrar los datos que estan asociados a la pagina( en este caso ninguno)
    return render_template("home.html")  

@app.get("/productos/")
def get_all_products():
    return render_template("productos.html", productos=productos.items())

@app.get("/productos/<int:id>")
def get_producto(id): 
    if id in productos:
        producto = productos[id]
        return render_template('producto.html', id=id, producto=producto)
    else:
        return ("no hay producto", 404)

