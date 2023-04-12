import re

patron = "hola"
texto = "hola chau hola mañana"

if re.search(patron, texto) is not None:
    print("no aparece")
else:
    print("aparece")


