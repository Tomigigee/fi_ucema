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

#6) Escribir una función que determine si una longitud de onda de una radio está dentro o fuera del rango de recepción de una antena. La longitud de onda mínima que recibe la antena es 223.0 y la máxima es 586.8 (no se puede usar if).
def longitud_radio(numero):
    return 223.0 <= numero <= 586.8
print(longitud_radio(200))

#7) Reescribir la función del punto anterior considerando, además, que la longitud de onda no puede ser 314.5 porque ya está ocupada por otra radio (no se puede usar if).
def longitud_radio2(numero):
    return 223.0 <= numero <= 586.8 and numero != 314.5
print(longitud_radio2(314.5))

#8) Escribir una función llamada tiene_descuento que tome como parámetro una edad y devuelva True en caso de que la edad sea menor o igual a 12 o mayor o igual a 60. En caso contrario tiene que devolver False (no se puede usar if).
def tiene_descuento(edad):
    return edad <= 12 or edad>=60
print(tiene_descuento(10))


#10) Escribir una función que reciba un nombre y un apellido y devuelva un saludo de bienvenida para esa persona.
def nombre_apellido(nombre, apellido):
    return "Hola"+" "+ nombre + " "+ apellido + ", bienvenido al Himalaya. Helado?"
print(nombre_apellido("Tomás", "Gigena"))

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

#13)Escribir una función llamada es_multiplo que reciba dos números y diga si el segundo es múltiplo del primero
def es_multiplo(n1, n2):
    return (n2%n1) == 0
print(es_multiplo(2, 5))

#14)Escribir una función que nos diga si un número es par, impar o cero.
def par_impar(numero):
    if numero % 2 == 0 and numero != 0:
        return "es par"
    elif numero == 0:
        return "es cero"
    else:
        return "es impar"
print(par_impar(4))

#15)Escribir una función que tome como parámetro una frase y nos diga cuántas "a" (o "A") hay en la frase, utilizando for.
#frase = "hola como estas"
 #def cuantas_a():   #no me salio
 #   for i in frase:



#16) Escribir una función que tome como valor una cantidad de dinero y nos diga por cuántos meses podemos subsistir con ese dinero, tomando en cuenta que se gastan 60000 pesos por mes.
def dinero(cantidad):
   return "puedes subsistir "+ str(cantidad // 60000 ) +" meses"
print(dinero(220000))