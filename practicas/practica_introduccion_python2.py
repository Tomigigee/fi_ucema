
#1)Definir un procedimiento que tome como parámetro una lista, verifique si tiene el elemento "control" y le agregue el string "revisado" y le quite el elemento "control".
lista = ["control", "agua"]

def chequear(lista):
    if "control" in lista:
        return lista.append("revisado") and lista.remove("control")
print(chequear(lista))
#2)Definir un procedimiento que tome una lista como parámetro y elimine el primer elemento de la lista. Hacer las verificaciones que sean necesarias.
lista2 = ["hola", "como", "estas"]
def eliminar_primero(lista):
    lista.pop(0)
    return lista
print(eliminar_primero(lista2))
#nueva_lista = eliminar_primero(lista2)
#print(nueva_lista)
#3)Definir una función que dada una lista y un elemento devuelva la posición de este elemento en la lista.
def posicion_elemento(lista, elemento):
    return lista.index(elemento)
lista3 = [1, 2, 3, 4, 5]
elemento = 3
print(posicion_elemento(lista3, elemento))

 
#4)Definir un procedimiento que tome como parámetros dos listas y un elemento, en la que se debe eliminar el elemento de una lista y agregarlo a la otra. Realizar dos versiones del , usando un método distinto para eliminar el elemento en cada versión. ¿Qué problema/s tiene este procedimiento?
def cambiar_elemento(lista1, lista2, elemento):
    lista1.remove(elemento), lista2.append(elemento)
    return lista1, lista2
lista4 = [1, 2, 3, 4]
lista0 = [5, 6, 7, 8]
elemento_4 =  4
print(cambiar_elemento(lista4, lista0, elemento_4))

listaa = [1, 2, 3, 4]
listab = [5, 6, 7, 8]
elemento_a =  4
def mover_elemento(lista1, lista2, elemento):      #OTRO METODO
    indice = lista1.index(elemento)
    lista2 += [lista1.pop(indice)]
    return listaa, listab
print(mover_elemento(listaa, listab, elemento_a))
#5)Escribir una función que tome como parámetro una lista de enteros y devuelva una lista con valores booleanos que indique si cada elemento es par o impar. Por ejemplo, para la lista [2, 45, 108, 12, 7], la función debería retornar [True, False, True, True, False]. Utilizar la función realizada en la práctica anterior.
lista5= [1,2, 4,7, 8,9,10,12]
def par_impar(lista):
    return [x % 2 == 0 for x in lista]    
print(par_impar(lista5))
 
#6)Escribir una función que lea un string y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).
string6 = "Boca"
def cantidad_caracteres(string):
    diccionario = {}
    for caracter in string:
        if caracter in diccionario:            #Lo intente pero me parecio imposible asi que le pedi a chatGPT que lo haga :(
            diccionario[caracter] += 1
        else:
            diccionario[caracter] = 1 
    return diccionario 
print(cantidad_caracteres(string6))
 
#7)Modificá la función anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0.
string7 = "Maradona"
def contar_todo(string):
    diccionario = { }
    for caracter in string:
        if caracter in diccionario:            #Tambien se lo pedi a chat gpt pero no funciona el codigo
            diccionario[caracter] += 1
        else:
            diccionario[caracter] = 1 
    for caracter in sorted(set(string)):
        if caracter not in diccionario:
            diccionario[caracter] = 0
    return diccionario
 
resultado = contar_todo(string7)
print(resultado)
 
#8)Definir una función que dada una palabra, nos diga si el palíndromo o no.
def palindromo(palabra):
    palabra_invertida = palabra [::-1]         #Tambien se lo pedi a chat gpt :((((
    return palabra == palabra_invertida
print(palindromo("neuquen"))

 
#9)Definir una función llamada productoria que toma como parámetro una lista de números y los multiplica a todos.
lista9 = (2, 4, 3, 6)
def multiplicador(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado
print(multiplicador(lista9))

#10)Creá un programa para gestionar datos de los socios de un club, el cual permita: 
#Cargar la información de los socios en un diccionario, al cual poder acceder por número de socio. Los datos que se deben almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al dia (s/n). El programa debe iniciar con los datos de los socios fundadores ya cargados, los cuales son:

#Socio número 1, Florencia Ocampo, ingresó el 14/09/2001, cuota al día

#Socio número 2, David Estévez, ingresó el 14/09/2001, cuota al día

#Socio número 3, Sofía Cáceres, ingresó el 14/09/2001, cuota al día

#Informar la cantidad de socios que tiene el club.

#Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas.

#Modificar la fecha de ingreso de todos los socios ingresados el 21/10/2017, indicando que en realidad ingresaron el 22/10/2017.

#Solicitar el nombre y apellido d eun socio y darlo de baja (eliminarlo del listado).

#Imprimir el listado de socios completos.

#Definir las funciones y/o procedimientos que creas necesarios.