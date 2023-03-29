print("hola")
import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
re.search(patron, texto).group()
print(re.findall(patron, texto))

patron2 = "ipsum(.*)amet" #En (.*) el punto quiere decir que puede ser cualquier caracter y el asterisco para indicar que puede haber 0 o mas de esos caracteres
print(re.search(patron2, texto).group()) #usando solo group() se incluye lo que esta entre las dos palabras pero incluyendolas
print(re.search(patron2, texto).group(1)) #Usando group(1) no se incluyen las dos palabras.

texto3 = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron3 = "ipsum(.*?)sit"
print(re.findall(patron3, texto3))

saludo = "Hola mundo"
print(len(saludo)) #Nos dice la cantidad de caracteres 
print(saludo.upper()) #Todo mayuscula
print(saludo.lower()) #Todo minuscula
print(saludo.count('o')) #Cuenta cuantas letras, palabras hay de lo que seleccionamos entre parentesis
print(saludo.replace('o','a')) #Reemplaza
print(saludo.lower().upper()) #Si combinamos termina siendo todo mayuscula ya que fue la ultima que se puso
print(saludo.replace("mundo", "terricolas"))
print(saludo)
