import re
texto1 = "hola como andas como estas "
patron = "como"
print(re.search(patron, texto1)) #Busca el primero que aparece 
print(texto1[5:9])

print(re.match(patron, texto1)) #Busca al incicio del texto1

print(re.findall(patron, texto1)) #Genera una lista con todas las apariciones 

print(re.search(patron, texto1).group()) 

texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron1 = "ipsum(.*)sit" #todo lo que hay entre ipsum y sit
print(re.search(patron1, texto), "\n")
print(re.search(patron1, texto).group())
print(re.search(patron1, texto).group(1)) #elimina ipsum y sit, no incluye lo que yo busqué
