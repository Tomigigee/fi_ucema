#!usr/bin/env python 3
import sys, os
#1)Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").

letra = "P"
contador = 0
with open ("archivo1.txt", "r") as archivo:
    for linea in archivo:
        if not linea.startswith(letra):
            contador += 1
        else:
            contador += 0
print(contador)

#2)Escribí un programa que lea un archivo e imprima las primeras n líneas.
n_lineas = 2
with open("archivo2.txt", "r") as archivo:
    for linea in range(n_lineas):
        primeras_lineas = archivo.readline()
        print(primeras_lineas)

#3)Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.
n = 2
lineas = []
with open("archivo3.txt", "r") as archivo:
    lineas = archivo.readlines()
ultimas_lineas = lineas[-n:]

for linea in ultimas_lineas:
    print(linea.strip())

#4)Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.
contador = 0
with open("archivo4.txt", "r") as archivo:
    archivo_leido = archivo.read()
    palabras = archivo_leido.split()
    cantidad_palabras = len(palabras)
    print(cantidad_palabras)


