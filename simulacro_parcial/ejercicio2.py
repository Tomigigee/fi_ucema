import re, sys, os, glob

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

            
    
