import sys
import os

#with open("hola.txt", "r") as arch_practica:
    #with open("chau.txt", "w") as arch_practica2:
        #arch_practica2.write(" Hola")

#with open("chau.txt", "r") as arch_practica2:
    #with open("hola.txt", "w") as arch_practica:
        #arch_practica.write(" Chau")

file1 = "hola.txt"
file2 = "chau.txt"

os.rename(file1, "temporal")
os.rename(file2, file1)                 #modificar este script para que pueda cambiar los archivos desde la terminal
os.rename("temporal", file2)