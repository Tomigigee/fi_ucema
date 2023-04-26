import re, sys, os, glob

#Si pidiera que nos movieramos a un archivo  habria que usar os.chdir

archivo1 = "C:/Users/fgige/Desktop/fi_ucema/simulacro_parcial/archivo11.txt"
archivo2 = "C:/Users/fgige/Desktop/fi_ucema/simulacro_parcial/archivo22.txt"
archivo3 = "C:/Users/fgige/Desktop/fi_ucema/simulacro_parcial/basededatos.txt"


def copiar_mails(archivo1, archivo2, archivo3):
    with open(archivo1, "r") as file1, open(archivo2, "r") as file2, open(archivo3, "a") as file3:
        archivo_leido = file1.read().split()
        archivo_leido2 = file2.read().split()
        for string in archivo_leido:
            if bool(re.search("^\w+[.-_]?\w*[@][a-z]+[.][a-z]+[.]?[a-z]?$", string)) == True:
                file3.write(string + "\n")
            else:
                pass
                
        for string in archivo_leido2:
            if bool(re.search("^\w+[.-_]?\w*[@][a-z]+[.][a-z]+[.]?[a-z]?$", string)) == True:
                file3.write(string + "\n")
            else:
                pass
print(copiar_mails(archivo1, archivo2, archivo3))

            
def filtrar(archivo):
    lista_txt = glob.glob("*.txt")

    with open(archivo, "a") as arch:
        for archivo in lista_txt:
            with open(archivo, "r") as archivo_secreto:
                texto = archivo_secreto.read()
                lista = re.findall("[\w]+[-_\.]*[\w]+@gmail.com", texto)
                for email in lista:
                    arch.write(email + "\n")
print(filtrar("basededatos.txt"))