import os, glob, re

#De alegige.txt que se encuentra en la carpeta "Prueba" (Carpeta que tienen que crear de antes y meter el txt adentro) extraer las fechas que siguen el siguiente patron numeros/letras/numeros, es decir, las primeras 2. Estas las deben guardar en un txt  nuevo dentro de la carpeta "Prueba". Deben hacer el codigo de tal forma que las fechas se vean de esta forma en el txt nuevo. 

def resta():
    #os.chdir("prueba")
    with open("texto.txt", "r") as file1:
        file_leido = file1.read()
        print(file_leido)
        fechas = re.findall("\d*[/][a-z]*[/]\d*", file_leido)
        
    with open("archivo_nuevo.txt", "a") as file2:
        for fecha in fechas:
            for i in fecha:
                file2.write(i + "\n")

print(resta())