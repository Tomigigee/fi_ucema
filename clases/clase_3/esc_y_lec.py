#!/bin/python3
import sys

with open("mi_nombre.txt", "a") as mi_arch:
    mi_arch.write("Tomas Gigena")

with open("mi_nombre.txt", "r") as mi_arch:
    with open("mi_nombre2.txt", "a") as arch:
        arch.write(mi_arch.readline(5))

texto_leido =  open("mi_nombre.txt", "r").read()
texto_para_escribir = texto_leido[0:6]

with open("nuevo_archivo.txt", "a") as miarch:
    miarch.write(texto_para_escribir)

#print(texto_leido[0:6])