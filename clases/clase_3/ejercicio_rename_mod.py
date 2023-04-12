#Modificar el script para que tome el nombre de los archivos dsede la terminal
import os


archivo1 = "hola2.txt"
archivo2 = "chau2.txt"

if not os.path.exists(archivo1):
    print(f"El archivo {archivo1} no existe")
    exit(1)

if not os.path.exists(archivo2):
    print(f"El archivo {archivo2} no existe")
    exit(1)

os.rename(archivo1, "temporal")
os.rename(archivo2, archivo1)                 #modificar este script para que pueda cambiar los archivos desde la terminal
os.rename("temporal", archivo2)


