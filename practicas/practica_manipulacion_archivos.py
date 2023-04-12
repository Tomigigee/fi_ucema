#!/bin/python3
import sys, os

#1)Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").
letra_inicio = "P"
contador = 0
with open("archivo1.txt", "r") as archivo:
    for linea in archivo:
        #linea = linea.strip() # Eliminar el salto de línea al final de la línea ##opcional
        if not linea.startswith(letra_inicio):
            contador += 1  
print("El archivo {} tiene {} líneas que no comienzan con la letra {}.".format("archivo1.txt", contador, letra_inicio))


#2)Escribí un programa que lea un archivo e imprima las primeras n líneas.
cantidad_lineas = 5
with open("archivo2.txt", "r") as archivo:
    for linea in range(cantidad_lineas):
        linea = archivo.readline()
        print(linea)

#3)Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.
n = 3
lineas = [] #archivo donde almacenare las lineas
with open("archivo3.txt", "r") as archivo:
    lineas = archivo.readlines() #utilizo readlines para que lea todas las lineas
ultimas_lineas = lineas[-n:]

print("Las últimas", n, "líneas del archivo son:")
for linea in ultimas_lineas:
    print(linea.strip()) #uso strip para eliminar caracteres de salto de linea o espacio en blanco al final de la linea

#4)Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.
cantidad = 0
with open("archivo4.txt", "r") as archivo:
    contenido = archivo.read() #lee todo el contenido del archivi
    palabras = contenido.split() #uso split para dividir el contenido en palabras
    cantidad_palabras = len(palabras) #utilizo len para obtener la cantidad de palabras que hay
    
print("El archivo tiene {} palabras".format(cantidad_palabras))

 
#5)Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.
letra = "p"
with open("archivo5.txt", "r") as archivo:
    contenido_archivo5 = archivo.read()
    letras_reemplazado = contenido_archivo5.replace(letra, "m")

with open("archivo5,5.txt", "a") as arch:
    arch.write(letras_reemplazado)
 
#6)Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

with open("archivo6.txt", "r") as archivo:
    contenido = archivo.read()
contenido_sin_salto = contenido.replace("\n", "")

with open("archivo_sin_salto.txt", "w") as archivo_sin_salto:
    archivo_sin_salto.write(contenido_sin_salto)

#7)Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.
def longest_word(archivo):
    max_long = 0
    palabra = ""
    with open(archivo, "r") as f:
        word_list = f.read().split()
        for word in word_list:
            if len(word) > max_long :
                max_long = len(word)
                palabra = word
    print("la palabra mas larga es", palabra, "con", max_long, "caracteres")
longest_word("archivo1.txt") 

#8)Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.
with open("archivo8.txt", "r") as archivo1:
    archivo1_leido = archivo1.read()
with open("archivob.txt", "r") as archivo2:
    archivo2_leido = archivo2.read()
with open("archivo8leido.txt", "a") as archivo_final:
    archivo_final.write(archivo1_leido)
    archivo_final.write(archivo2_leido)

#def join_files(file1,file2,file3):
 #   with open(file1, "r") as f1, open(file2, "r") as f2, open(file3, "a") as f3:    #otraa forma
  #      f3.write(f1.read() + f2.read())
#join_files("documento", "documento2", "documento3")

#9)Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.
palabra = "hola"
with open("archivo9.txt", "r") as archivo:
    arch_leido = archivo.read()
    palabras99 = arch_leido.split()
    cantidad_palabras = len(palabras99)
    veces_palabra = arch_leido.count(palabra)
    frecuencia = (veces_palabra) / cantidad_palabras

print(frecuencia)

#10)Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.
ruta_carpeta1 = "C:/Users/fgige/Desktop/fi_ucema/practicas/carpeta 1" 
ruta_resultado = os.path.join(ruta_carpeta1, "resultado")       ## Definimos la ruta de la carpeta Carpeta1 y la carpeta Resultado
ruta_archivo_resultado = os.path.join(ruta_resultado, "resultado.txt")  # Definimos la ruta del archivo donde se van a concatenar los archivos .txt

archivo_resultado = open(ruta_archivo_resultado, "a") # Abrimos el archivo en modo "a" para añadir contenido al final del archivo si existe

for archivo in os.listdir(ruta_carpeta1): #recorremos todos los archivos de la carpeta
    if archivo.endswith(".txt"): #comprobamos que el archivo termine en txt
        ruta_archivo = os.path.join(ruta_carpeta1, archivo)
        archivo_txt = open(ruta_archivo, "r")

        contenido = archivo_txt.read()
        archivo_resultado.write(contenido)


