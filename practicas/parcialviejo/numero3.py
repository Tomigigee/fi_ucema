import os, glob, re

# A) En los textos mágicos .log se encuentra escondido el discurso del sombrero seleccionador.

# Usando todo lo que sabes de las bibliotecas os, glob y re construí un procedimiento que:
# i) cree un directorio cuyo nombre se corresponde con el nombre de la casa elegida,
# la cual se esconde en la 4ta linea del archivo texto5.log.

# ii) extraiga las primeras 4 líneas de los archivos .log

# y las almacene en un único archivo llamado selección_del_sombrero.txt,

# que se guarde en la carpeta creada en el punto i).

def sombrero_seleccionador():
    #os.chdir("parcialviejo")
    with open("texto5.log", "r") as casa:
        escondido = casa.readlines()
        #print(escondido)
        nombre_carpeta = escondido[3]
        #print(nombre_carpeta)
        archivo_limpio = re.search("(\w)*", nombre_carpeta).group()
        #print(archivo_limpio)
        os.mkdir(archivo_limpio)
    
    log = glob.glob("*.log")
    todas_las_lineas = []
    for archivo in log:
        with open(archivo, "r") as file1:
            log_leido = file1.readlines()
            contador = 0
            while contador < 4:
                todas_las_lineas.append(log_leido[contador])
                contador += 1      
    os.chdir("Gryffindor")
    with open("seleccion_del_sombrero.txt", "a") as file_salida:
        for linea in todas_las_lineas:
            file_salida.write(linea)
    #os.chdir("../")
print(sombrero_seleccionador())         
    #os.mkdir(re.findall("Gryffindor", log))

