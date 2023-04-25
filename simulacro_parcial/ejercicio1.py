# Consigna N*1
# Escribir funciones que, dado un String, permitan:
# a) Obtener la lista de subsecuencias delimitadas por "X e 'Y', que incluyan la subsecuencia 'ab'. Por ejemplo para
# XbaaaYiXababYqXbabbbbaaYaXffeeY, hay que devolver ['abab-, 'babbbaa'.

import re


def obtener_lista(string):
    return re.findall("X([^XY]*ab[^XY]*)+Y", string)
print(obtener_lista("XbaaaYiXababYqXbabbbbaaYaXffeeY"))

#b
def funcionDeExpresiones_Regulares(string1):
    return re.findall("ag(\D.*?)cta", string1)
print(funcionDeExpresiones_Regulares("aabocaggaaactazu4lggaasag24gra1ndecta"))