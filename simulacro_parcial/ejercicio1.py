# Consigna N*1
# Escribir funciones que, dado un String, permitan:
# a) Obtener la lista de subsecuencias delimitadas por "X e 'Y', que incluyan la subsecuencia 'ab'. Por ejemplo para
# XbaaaYiXababYqXbabbbbaaYaXffeeY, hay que devolver ['abab-, 'babbbaa'.

import re


def obtener_lista(string):
    return re.findall("X([^XY]*ab[^XY]*)+Y", string)
print(obtener_lista("XbaaaYiXababYqXbabbbbaaYaXffeeY"))

def entre(string):
    return re.findall("X(.*?ab.*?)Y", string)          #el enunciado estaba mal, no tenia que devolver abab y babbbaa
print(entre("XbaaaYiXababYqXbabbbbaaYaXffeeY"))

#EL ? lo usamos para que haga la busqueda interna
#.* : Cualquier caracter una o mas veces

#Usamos Findall ya que nos pide que nos devuelva una lista y eso es lo que hace findall.



#b
def funcion_de_expresiones_regulares(string1):
    return re.findall("ag([^\d]*)cta", string1)
print(funcion_de_expresiones_regulares("aabocaggaaactazu4lggaasag24gra1ndecta"))

#En el nombre de la funcion faltaban los snake case que separen las palabras. Ademas, las palabras deben estar todas en mayuscula o todas en minuscula.
#El nombre de la funcion esta mal ya que no tiene que dec;arar que es una funcion y ademas tiene que ser descriptiva de lo que hace. 
#El error que tira es AttributeError: module re has no function findal.
