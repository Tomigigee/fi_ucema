#1)Escribir un programa que imprima la longitud de un string el cual se lee por teclado.
def longitud(palabra):
    return len(palabra)
print(longitud("boquita"))

##2)Realizar un programa donde se imprima la 5ta y 6ta letra de un string pasado por teclado en mayuscula.
def ultimaletra(palabra):
    if len(palabra) >= 6:
        return palabra[4]+palabra[5]
    else: 
        "la palabra tiene menos de 6 letras"
print(ultimaletra("Maradona"))

#3)Escribir un programa que pregunte el nombre y apellido al usuaeio y lo salude.
def nombreapellido(nombre, apellido):
    return "Hola"+" "+ nombre + " "+ apellido
print(nombreapellido("Tomás", "Gigena"))

#4) Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayusculas
def iniciales(nombre, apellido1, apellido2):
    return nombre[0]+apellido1[0]+apellido2[0]
print(iniciales("Tomas","Gigena","Dall"))

#5)Realice un programa que lea tres numeros ppr teclado y calcule el promedio de ellos.
def numerospromedio(a,b,c):
    return (a+b+c)/3
print(numerospromedio(5,8,5))

