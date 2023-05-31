import re

#a) obtener la lista de los substrings delimitados entre '<' y '>' que no incluyan ninguna 'o'.
def entre_piquitos_sin_o(string):
    return re.findall("[<]([^o]*?)[>]", string)
print(entre_piquitos_sin_o("ds<hola>hsb<hhj>sdk<469>nkd")) 

# b) Onomatopopih, que aún no sabe mucho de expresiones regulares,
# nos mandó una función que debería ser capaz de decirnos si un string incluye o no un substring de 3 letras,
# cada una de las cuales debe ser a, b ó c. Esto es, alcanza con incluir, p.ej, 'abc', 'cbc', 'aac', 'ccc'.

# En base a la función que definió respondé:

# ¿Qué error/es tiene? (justificando la respuesta).
# Uno de los errores esta en el patron, el metacaracter {3} solo influye en la c; y tampoco da lugar a que haya match con las 3 letras en otro orden
# Tendria que usar re.search para que la funcion nos diga SI INCLUYE O NO el substring. Con el findall, si la funcion esta escrita correctamente, devolvera la lista de coincidencias. 

# Modificá la función para que cumpla lo requerido correctamente.

def triples(string):
    return re.findall("abc{3}", string)

print(triples("svsslkvabckjsv"))

def triples_corregidos(string):
    return bool(re.search("[a-c]{3}", string))

print(triples_corregidos("svsslkvabckjsv")) #abc
print(triples_corregidos("svsslkvkjabcuhjv"))
print(triples_corregidos("svsslkvkjbbcuhjv"))
print(triples_corregidos("svsslkvkjabuhjv"))
print(triples_corregidos("svssalkvbkjcuhjv"))

# Uno de los errores esta en el patron, el metacaracter {3} solo influye en la c; y tampoco da lugar a que haya match con las 3 letras en otro orden
# Tendria que usar re.search para que la funcion nos diga SI INCLUYE O NO el substring. Con el findall, si la funcion esta escrita correctamente, devolvera la lista de coincidencias. 