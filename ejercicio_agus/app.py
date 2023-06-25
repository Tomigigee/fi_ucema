from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

prendas = {
    100: {"name": "Remera talle m", "price": 50},
    150: {"name": "Remera talle s", "price": 40}
}


#Primer endpoint de la app:
@app.get("/") #decorador, generamos el /home (pagina principal)
def home(): 
    return render_template("home.html") #renderiza ese html y lo va a buscar a la carpeta template
#<p> etiqueta de html que se usa para poner texto en una pág web

@app.get("/prendas/")
def get_all_prendas():
    return render_template("prendas.html", prendas=prendas.items())

@app.get("/prendas/<int:id>")
def get_prenda(id): 
    if id in prendas:
        prenda=prendas[id]
        return render_template('prenda.html', id=id, prenda=prenda)
    else:
        return ('no hay prenda', 404)
    

@app.get("/ventas/<int:id>")
def get_ventas(id):
    return {"foo":1}

@app.route('/success/')
def success():
    return render_template("success.html")

@app.route('/prendas/new/' , methods=('GET', 'POST'))
def create_prenda():
    if request.method == 'POST':
        valor_input = request.form.get("name").split(',')
        prendas[int(valor_input[0])] = {"name":valor_input[1], "price": valor_input[2]}
    else:
        return render_template('new_prendas.html')
    


#como dominio vamos a usar un puerto/ip
#Para ver el front hacemos ctrl + click en el link (todo esto en la terminal)
#ctrl + C = salimos de python3 -m flask run 