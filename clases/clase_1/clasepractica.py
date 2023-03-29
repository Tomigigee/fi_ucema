#1 Escribir funciones que permitan obtener el anterior y siguiente de un numero
def anterior(numero):
    return numero-1 
def siguiente(numero):
    return numero+1

print(anterior(5))
print (siguiente(5))
#2)Escribir una funcion que obtenga el doble de un numero
def doble_numero(numero):
    return numero*2
print(doble_numero(10))

#3)Escribir una funcion que obtenga el doble de un numero y el doble del siguiente
def dobleysiguiente(numero):
    return str(doble_numero(anterior(numero))) + " y " + str(doble_numero(siguiente(numero)))
    # return (numero-1)*2 , (numero+1)*2 
print(dobleysiguiente(4))

#4)Escribir una funcion llamada retirardinero que tenga como parametros saldo y el monto a retirar y que devuelva cuanto saldo queda luego de la extracción. Si retira más dinero que lo que tiene en el saldo debe devolver 0(no se puede usar if)
def retirar_dinero(saldo, monto):
    #return str(saldo-montoaretirar) and min(saldo=montoaretirar)
    return max(saldo-monto,0)
print(retirar_dinero(100,10))

#5) Escribir una funcion llamada dia_de_la_semana_favorito que tome como paramtetro un día de la semana y devuelva True si es sabado o false si es cualquier otro
def dia_de_la_semana_favorito(dia):
    return str(dia) == "Sábado" or dia == "sabado"
print(dia_de_la_semana_favorito("sabado"))
print(dia_de_la_semana_favorito("lunes"))

#11)Escribir unafuncion que tome como parametro un string y que, si empieza con la letra "H", nos devuelva la longitud del string
def letrah(palabra):
    if palabra[0]== "H" or palabra[0]=="h":
        return len(palabra)
    else:
        return False
print(letrah("Hipopotamo"))

def letraa(palabra):
    if palabra.startswith("H"):
        return len(palabra)                #ESTO ES OTRA FORMA
    else:
        False
print(letraa("Hipopotanidbd"))


#12)Escribir una funcion que tome como parametro un string y nos diga si el string empieza con buenos o buenas.
def buenos(palabra):
    return palabra.startswith("Buenas") or palabra.startswith("Buenos")
       
print(buenos("Buenas"))

#13)Escribir una función llamada es_multiplo



