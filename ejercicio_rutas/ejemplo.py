#!/bin/python3
#Definir un procedimiento que lea los archivos .txt  que estan en la carpeta marzo, y copie la primera linea de cada uno en un archivo dentro de la carepta resultados(que debe estar dentro de news)

import os, glob, sys

def primeras_lineas(path_a_txt, path_resultado, salida):
    os.chdir(path_a_txt)#Nos movemos a marzo
    textos = glob.glob("*.txt")#extraemos los .txt
    primer_linea = []
    for txt in textos:
        with open(txt, "r") as texto:
            primer_linea.append(texto.readline())
    os.chdir("../../")
    os.mkdir(path_resultado)
    #with open("datos/marzo/archivo1.txt")
    os.chdir(path_resultado)
    with open(salida, "a") as final_txt:
        for linea in primer_linea:
            final_txt.write(linea)

primeras_lineas("datos/marzo", "resultado", "salida.txt")

#extraemos los .txt   
#leemos las primeras lineas   
#hacemos carpeta de salida(resultados)
#hacer archivo nuevo (salida.txt)
#poner lineas en archivo nuevo