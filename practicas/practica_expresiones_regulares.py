

#1 Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.
import re

def caracteres_permitidos(string):
    return bool(re.search("[a-zA-Z0-9]", string))
print(caracteres_permitidos("manz@"))

def caracteres_perm(string):
    return bool(re.search("[a-zA-Z0-9]", string))
print(caracteres_perm("hoola"))
#2 Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.
def todo_permitido(string):
    return not bool(re.search("[^a-zA-Z0-9]", string))
print("2", todo_permitido("mana"))

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
    patron4 = "[a-z]+_[a-z]+"
    if re.search(patron4, string) is not None:
        return "Patron encontrado"
    else:
        return "patron no encontrado"
print("4", palabras_unidas("hola_hola"))

#5)Escribí un programa que diga si un string empieza con un número específico.


def numero_especifico():
   numero = 5
   string = "6 son las vidas de un camion"
   patron5 = "^"+ str(numero)+ ".*"
   if re.search(patron5, string):
       return "el string COMIENZ con ese numero "
   else:
       return "el string NO comienza con ese numero"
print(numero_especifico())

#6)Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.

def palabra_en_frase():
    frase = "en casa hay un mapa"
    palabras = ["vida", "mapa", "manzana", "casa"]

    for palabra in palabras:
        if re.search(palabra, frase):
            print(f'La palabra "{palabra}" se encontró en la frase.')
        else:
            print(f'La palabra "{palabra}" NO se encontró en la frase.')
print(palabra_en_frase())



#7)Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.
lista7 = ["un cuento", "manzna", "zapallo"]

def solo_minusculas(lista):
    patron7 = "[a-zA-Z0-9 ]*"
    for string in lista:
        return re.findall(patron7, string) 
            
print(solo_minusculas(lista7))


#8) Escribi un programa que separe y devuelva los caracteres numericos de un string
def devuelve_numeros(string):
    resultado = re.split("\D+", string)
    for elemento in resultado:
        print(elemento)
devuelve_numeros("hoy hice 3 medialunas con 6 cafes y 2 huevos")
def duda(string):
    print (re.search("[0-9].*?[0-9]", string).group())

print(duda("hoy hice 3 medialunas con 6 cafes y 2 huevos"))

#9 Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
def entre_guiones(string):
    return re.findall("-(.*?)-", string) #cuando usamos el ? favorecemos los matrches internos. Si no usamos el ? no encontraría los guiones del medio, sino que solo el primero y el ultimo.
print(entre_guiones("hoy -me fui- pero despues -volvi- moto")) 

#10)Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &.
def delimitado_por(string):
    patron10 = "[^@|&]+[^@|&]?"
    return re.findall(patron10, string)
print(delimitado_por("tomas@franco&alberto&1986"))

#11)Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
lista_strings = ["Práctica Python Pancho", "Práctica C++", "Práctica Portran"]
def empiezan_con_p(lista):
    patron11 = r"P\w* P\w* P\w*" 
    for string in lista:
        if re.search(patron11, string):
            palabras = re.findall(patron11, string)
            print(f"En la cadena '{string}' las palabras que empiezan con P son: {palabras}")
print(empiezan_con_p(lista_strings))

#12)Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).
def separar_ocurrencias(string): 
    return re.sub(r"[ _:]", "|", string)   #usamos re.sub para reemplazar 
print(separar_ocurrencias( "Hola que tal:buen dia"))

#13)Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
def reemplazar_caracteres(string):
    #patron = "\d{0}" #_c_u_a_n_1_2_4_3_t_o_
    patron = "(\d{2})"
    return re.sub(patron, "_", string)

print(reemplazar_caracteres("cuan1243to"))

#14)Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.
def reemplazar_espacios(string):
    patron = "[ ]"
    return re.sub(patron, ";", string)
print(reemplazar_espacios("habia una vez un brujo"))
#15) Realizá un programa que validar si una cuenta de mail está escrita correctamente.
def mail_correcto(string):
    return bool(re.search("^\w+[.-_]?\w*[@][a-z]+[.][a-z]+[.]?[a-z]?$", string ))
print(mail_correcto("Tomigigee@gmail.com")) 
""""
r: significa que cualquier carácter especial contenido en la cadena se interpreta literalmente. (raw string)
 ^: indica el inicio de línea
 [a-zA-Z0-9._%+-]+: representa el nombre del usuario de la dirección de correo electrónico,  el cual debe estar conformado por uno o más caracteres alfanuméricos, puntos, guiones bajos, porcentajes, más y guiones.
 @: se utiliza para separar el nombre del usuario de la dirección de correo electrónico del dominio.
 [a-zA-Z0-9.-]+: especifica el dominio del correo electrónico, puede estar conformado por uno o más caracteres alfanuméricos, puntos y guiones.
 \.: indica que debe haber un punto.
 [a-zA-Z]{2,}: especifica la extensión de la dirección de correo electrónico, la cual debe estar conformada por dos o más caracteres alfabéticos.
""" 


def er(string):
    return re.findall("([a-z]{4})(er)", string)
print(er("llover, comer, barrer "))

def encontrar_nombres(string):
    return re.findall("[A-Z][a-z]\w+", string)
print(encontrar_nombres("Maria y Andres tienen 3 hijos, Juan de 16, Marcela de 10 y Daniel de 5"))


"""
Con [._-] se busca los caracteres . o _ o -. 
Con (._-) busca la secuencia en ese orden
"""