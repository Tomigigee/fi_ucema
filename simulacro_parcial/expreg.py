import re

archivo = open("tiposdesangre.txt", "r")
texto = archivo.read()
archivo.close()

resultado = []
for item in re.findall("(\w+\s\w+)(:\sO\+)", texto):
    resultado.append(item[0])
    print(resultado)  
    

    