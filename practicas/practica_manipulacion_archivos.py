#!/bin/python3
import sys, os, re, glob

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
cantidad_lineas = 2
def leer_imprimir(archivo):
    with open(archivo, "r") as archivo:
        for linea in range(cantidad_lineas):
            lineas = archivo.readline()
            print(lineas)
print(leer_imprimir("archivo2.txt"))

""""
cantidad_lineas = 5
with open("archivo2.txt", "r") as archivo:
    for linea in range(cantidad_lineas):
        linea = archivo.readline()
        print(linea)"""

#3)Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.
n = 4
lineas = []
def leer_guardar(archivo):
    with open(archivo, "r") as archivo:
        lineas = archivo.readlines()
    ultimas_lineas = lineas[-n:]
    for linea in ultimas_lineas:
        print(linea) #uso strip para eliminar caracteres de salto de linea o espacio en blanco al final de la linea
print(leer_guardar("archivo3.txt"))
        
n = 3
lineas = [] #archivo donde almacenare las lineas
with open("archivo3.txt", "r") as archivo:
    lineas = archivo.readlines() #utilizo readlines para que lea todas las lineas
    ultimas_lineas = lineas[-n:]

print("Las últimas", n, "líneas del archivo son:")
for linea in ultimas_lineas:
    print(linea.strip()) #uso strip para eliminar caracteres de salto de linea o espacio en blanco al final de la linea

#4)Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

def leer_y_contar(archivo):
    contador = 0
    with open(archivo, "r") as file1:
        archivo_leido = file1.read().split()
        cantidad_palabras = len(archivo_leido)
        print(cantidad_palabras)
print( leer_y_contar("archivo4.txt"))


with open("archivo4.txt", "r") as archivo:
    contenido = archivo.read() #lee todo el contenido del archivi
    palabras = contenido.split() #uso split para dividir el contenido en palabras
    cantidad_palabras = len(palabras) #utilizo len para obtener la cantidad de palabras que hay
    
print("El archivo tiene {} palabras".format(cantidad_palabras))

 
#5)Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

def rremplazar(archivo_entrada, archivo_salida, letra):
    with open(archivo_entrada, "r") as file1:
        archivo_leido = file1.read()
        archivo_reemplezado = archivo_leido.replace(letra, "\n" + letra )
    with open(archivo_salida, "a") as file2:
        file2.write(archivo_reemplezado)
print(rremplazar("archivo5.txt", "archivo5,5.txt", "p"))

def reemplazo(archivo_lectura, archivo_escritura, letra):
    with open(archivo_lectura, "r") as file1, open(archivo_escritura, "a") as file2:
        archivo_leido = file1.read()
        archivo_separado = archivo_leido.replace(letra,"\n" + letra)
        file2.write(archivo_separado)
#print(reemplazo("archivo5.txt", "archivo5,5.txt", "p"))

"""def reemplazar(entrada, salida, letra):
    with open(entrada, 'r') as file, open(salida, 'w') as file2:
        for line in file:
            file2.write(line.replace(letra, '\n' + letra)) 
print(reemplazar("archivo5.txt", "archivo5,5.txt", "p"))
     #Reemplazo y lo escribo en el nuevo archivo
    # reemplazar('sin_saltos.txt', 'texto_prueba.txt','n')"""

#6)Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

def eliminar_salto_de_linea(archivo_entrada, archivo_salida):
    with open (archivo_entrada, "r") as file1:
        archivo_leido = file1.read()
        contenido_sin_salto = archivo_leido.replace("\n", "")
    with open(archivo_salida, "a") as file2:
        file2.write(contenido_sin_salto)
print(eliminar_salto_de_linea("archivo6.txt", "archivo6,5.txt"))

def eliminar_saltos_de_linea(archivo):
    with open(archivo, "r") as arch:
        contenido = arch.read()
        contenido_sin_salto = contenido.replace("\n", "")

    with open("archivo_sin_salto.txt", "w") as archivo_sin_salto:
        archivo_sin_salto.write(contenido_sin_salto)
 
print("6", eliminar_saltos_de_linea("archivo6.txt"))
#7)Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.
def palabra_larga(archivo):
    longitud = 0
    word = ""
    with open(archivo, "r") as file1:
        archivo_leido = file1.read().split()
        for palabra in archivo_leido:
            if len(palabra) > longitud:
                longitud = len(palabra)
                word = palabra
    print("la palabra mas larga es", word,"con", longitud, "letras")
print(palabra_larga("archivo1.txt"))

def longest_word(archivo):
    max_long = 0
    palabra = ""
    with open(archivo, "r") as arch:
        lista_palabras = arch.read().split()
        for word in lista_palabras:
            if len(word) > max_long :
                max_long = len(word)
                palabra = word
    print("la palabra mas larga es", palabra, "con", max_long, "caracteres")
    longest_word("archivo1.txt") 

#8)Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

def guardar_contenido(archivo_entrada1, archivo_entrada2, archivo_salida):
    with open(archivo_entrada1, "r") as file1, open(archivo_entrada2, "r") as file2:
        archivo_leido = file1.read() + file2.read()
    with open(archivo_salida, "a") as file3:
        file3.write(archivo_leido)
print(guardar_contenido("archivo8.txt", "archivo8,5.txt", "archivo8leido.txt"))

def dos_documentos(archivo, archivo2, archivocontenido):
    with open(archivo, "r") as file1, open(archivo2, "r") as file2, open(archivocontenido, "a") as file3:
        archivo1leido= file1.read()
        archivo2leido = file2.read()
        file3.write(archivo1leido)
        file3.write(archivo2leido)
#print(dos_documentos("archivo8.txt", "archivob.txt", "archivo8leido.txt"))

"""with open("archivo8.txt", "r") as archivo1:
    archivo1_leido = archivo1.read()
with open("archivob.txt", "r") as archivo2:
    archivo2_leido = archivo2.read()
with open("archivo8leido.txt", "a") as archivo_final:
    archivo_final.write(archivo1_leido)
    archivo_final.write(archivo2_leido)"""

#def join_files(file1,file2,file3):
 #   with open(file1, "r") as f1, open(file2, "r") as f2, open(file3, "a") as f3:    #otraa forma
  #      f3.write(f1.read() + f2.read())
#join_files("documento", "documento2", "documento3")

#9)Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.
def frecuencia(archivo_entrada, palabra):
    with open(archivo_entrada, "r") as file1:
        archivo_leido_separado = file1.read().split()
        cantidad_palabras = len(archivo_leido_separado)
        veces_palabra = archivo_leido_separado.count(palabra)
        frecuencia = veces_palabra / cantidad_palabras
        print(frecuencia)
print(frecuencia("archivo9.txt", "hola"))

def frecuencia_de_todas(archivo_entrada0):
    with open(archivo_entrada0, "r") as file1:
        palabras = file1.read().split()
        total = len(palabras)
        for palabra in palabras:
            veces = palabras.count(palabra)
            frecuencia = (veces / total) * 100
            print("la palabra "+ str(palabra) + " aparece "+ str(veces) + " veces" + "es decir, un "+ str(frecuencia)+ " % del total")
        print(palabras)
print(frecuencia_de_todas("archivo9.txt"))

#10)Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.

def leer_carpeta(archivo_salida):
    os.chdir("carpeta1")
    os.mkdir("resultadoo")
    txt = glob.glob("*.txt")
    for archivo in txt:
        with open(archivo, "r") as file1:
            archivo_leido = file1.read()
        os.chdir("resultadoo")
        with open(archivo_salida, "a") as file2:
            file2.write(archivo_leido)
        os.chdir("../")
#print(leer_carpeta("archivo_salida.txt")) 

"""def carpeta(archivo_salida, archivo_mails):
    os.chdir("carpeta1")
    os.mkdir("resultadoo")
    txt = glob.glob("*.txt")
    for archivo in txt:
        with open(archivo, "r") as file1:
            texto_leido = file1.read()
            #texto = re.findall("mis[.*]+justo", texto_leido)
        os.chdir("resultadoo")
        with open(archivo_salida, "a") as salida:
            salida.write(texto_leido + "\n")
        os.chdir("../")
    mails = re.findall("[a-z]+[_-.]?[0-9]*[a-z]*[@][a-z]+[.][a-z]+[.]?[a-z]{2,3}", archivo_salida)
    with open(archivo_mails, "a") as mails:
        for mail in mails:
            mails.write(mail + "\n")
    
carpeta("archivo_nuevo", "archivo_mails")
"""

# vamos a hacer un programa que nos perimta abrir un archivo, leerlo y separar todos los mails validos y guardarlos
# en un nuevo archivo  
def encontrar_mails(archivo, archivo_salida):
    with open(archivo, "r") as file:
        texto_leido = file.read()
    pattern = r"[a-z0-9]+[._-]?[a-z0-9]*[@][a-z]+[.][a-z]+[.]?[a-z]*"
    mails = re.findall(pattern, texto_leido)
    print (mails)
    with open (archivo_salida, "w") as file2:
        for mail in mails:
            file2.write(mail + "\n")


""""ruta_carpeta1 = "C:/Users/fgige/Desktop/fi_ucema/practicas/carpeta1" 
ruta_resultado = os.path.join(ruta_carpeta1, "resultado")       ## Definimos la ruta de la carpeta Carpeta1 y la carpeta Resultado
ruta_archivo_resultado = os.path.join(ruta_resultado, "resultado.txt")  # Definimos la ruta del archivo donde se van a concatenar los archivos .txt

archivo_resultado = open(ruta_archivo_resultado, "a") # Abrimos el archivo en modo "a" para añadir contenido al final del archivo si existe

for archivo in os.listdir(ruta_carpeta1): #recorremos todos los archivos de la carpeta
    if archivo.endswith(".txt"): #comprobamos que el archivo termine en txt
        ruta_archivo = os.path.join(ruta_carpeta1, archivo)
        archivo_txt = open(ruta_archivo, "r")

        contenido = archivo_txt.read()
        archivo_resultado.write(contenido)"""


def reemplazar(entrada, salida, letra):
    with open(salida, "a") as archivo1:
        with open(entrada, "r") as archivo2:
            texto = archivo2.read()
            texto2 = texto.replace(letra, letra + "\n")
            archivo1.write(texto2)
        
def numero_valido(archivo):
    #os.chdir("telefonos.txt")
    with open(archivo, "r")  as file1:
        telefonos_leido = file1.read()
        for linea in telefonos_leido:
            re.findall(r"(+5411)([0-9]{8})", linea)

print(numero_valido("telefonos.txt"))


"""Creá una carpeta llamada “CarpetaParcial” en la que existan 2 archivos .txt que contengan la
siguiente información (los archivo .txt, también tenés que crearlos vos bro):
Contenido del archivo 1:
643262462352362463262+46+423crnewuvpn3t42+3235523+verw+5491142342353532mcw
iromvvwrwrvervwr43v4*3
Contenido del archivo2:
64326246235236bwrbew+54911542263632623r246326vew2+46+423crneevwwuvpnew3tv
ew42+3235523+verw+5491v142342353532mcwiromvvwrwrvervwr43v4*3
Deberás extraer los números de teléfono de CABA (+54911########) y guardarlos en un
archivo nuevo, en una carpeta llamada” Telefonos”, creada dentro de la CarpetaParcial.
Buena suerte!
"""

def ejercicio_valen():
    os.chdir("carpetaparcial")
    os.mkdir("Telefonos")

print(ejercicio_valen())