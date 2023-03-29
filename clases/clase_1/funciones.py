#Esta es la estructura de una función
# def funcion(argumento):
  #  Operación sobre el argumento
   # return aquí va el resultado quiero devolver
def doble(numero):
    resultado = numero * 2
    return resultado
print(doble(5)) 

def dividir(a, b):
    return a // b
print(dividir(8,2))

def es_par(numero):
    return numero % 2 == 0
print(es_par(8))

def mail(nombre, dominio):
    return nombre + "@"+ dominio + ".com"
print(mail("tomigigee", "gmail"))

def mate(numero):
    return numero * 30 - 1000
print(mate(20))

def vaquita(precio, comensales): 
    return precio // comensales 
print(vaquita(9800, 16))

def cantidad_agua(numero):
    if numero * 30 <= 1000:
        return numero * 30 
    else:
        return "vas a necesitar más de un termo"
print(cantidad_agua(500))


pedido = {"Ana": "no veggie", "Paul": "veganas", "Luz": "vegetarianas"}
pedido["Ana"]
pedido.keys()
lista_comensales = pedido.keys() 
def empanadas_por_gusto():
    for i in lista_comensales:
        print(pedido[i])
print(empanadas_por_gusto())
  