#1 Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.
import re

def caracteres_permitidos(string):
    return bool(re.search("[a-zA-Z0-9]", string))
print(caracteres_permitidos("manz@"))

#2 Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.
def todos_petmitidos(string):
    return not bool(re.search("[^a-zA-Z0-9]", string))
print(todos_petmitidos("manz@na"))

#3 Creá un programa que verifique las siguientes condiciones:

#si un string dado tiene una h seguida de ninguna o más e.

#si un string dado tiene una h seguida de una o más e.

#si un string dado tiene una h seguida de cero o una e.

#si un string dado tiene una h seguida de dos o tres e.
def encontrar_patron(string): #0 o mas
    patron = "he*"    #uso * ya que es un metacaracter cuantificador que significa 0 o más veces. En este caso es 0 o más veces solo la e ya que afecta solo a lo que tiene a su izquierda
    if re.search(patron, string) is not None:
        return("patron encontrado")
    else:
        return "no se encontro el patron"
    
print(encontrar_patron("a")) #no encuentra
print(encontrar_patron("h")) #encuentra ya que la e era 0 o mas
print(encontrar_patron("he")) #encuentra ya que esta la h y la e

def encontrar_0_o_una(string1): #cero o una
    patron1 = "he?"    #uso ? ya que es un metacaracter cuantificador que significa 0 o 1. En este caso es 0 o más veces solo la e ya que afecta solo a lo que tiene a su izquierda
    if re.search(patron1, string1) is not None:
        return("patron encontrado")
    else:
        return "no se encontro el patron"
print(encontrar_0_o_una("h")) #encuentra

def encontrar_2_o_3(string): #dos o tres
    patron2 = "he{2,3}"
    if re.search(patron2, string) is not None:
        return("patron encontrado")
    else:
        return "no se encontro el patron"
print(encontrar_2_o_3("he")) #no encuentra
print(encontrar_2_o_3("hheeeey")) #encuentra

#4 encuentre una palabra unida a otra con un guion bajo un string
def palabras_unidas(string):
    patron4 = "^[a-z]+_[a-z]+$"
    if re.search(patron4, string) is not None:
        return "Patron encontrado"
    else:
        return "patron no encontrado"
print(palabras_unidas("hola_hola"))

#5)Escribí un programa que diga si un string empieza con un número específico.
def numero_especifico(string):
    patron5 = "^\d$"
    

#6)Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.

#8 Escribi un programa que separe y devuelva los caracteres numericos de un string
def devuelve_numeros(string):
    resultado = re.split("\D+", string)
    for elemento in resultado:
        print(elemento)
devuelve_numeros("hoy hice 3 medialunas con 6 cafes y 2 huevos")

#9 Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
def entre_guiones(string):
    return re.findall(r"-(.*?)-", string) #cuando usamos el ? favorecemos los matrches internos. Si no usamos el ? no encontraría los guiones del medio, sino que solo el primero y el ultimo.
print(entre_guiones("hoy -me fui- pero despues -volvi- moto")) 

#11
 






