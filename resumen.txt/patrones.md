# Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.
patron = "[a-zA-Z0-9]"

# Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.
r"[^a-zA-Z0-9]"

# Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios)
patron = "^[a-z]+_[a-z]+$"

# Escribí un programa que diga si un string empieza con un número específico.
patron = "^9"

# Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.
patron = "(?!\s)(\W)"

# Escribí un programa que separe y devuelva los caracteres númericos de un string.
patron = "\d"

# Escribí un programa que extraiga los caracteres que estén entre guiones en un string. 
# (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
patron = "-(.*?)-"

# Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &.
patron = "[@|&]+(.*?)[@|&]"

# Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P
# y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
patron = "(P\w*)\s(P\w*)"

# Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|)
patron = "[\s_:]"

# Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
patron = "[\W]{2,}"

# Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
patron = "[\W]{2,}"

# Escribi un patron que recopile los mails de un txt
r"([a-zA-Z0-9.*]+)@(yahoo|hotmail).com\b"

# Escribi un patron que recopile cualquier mail de un txt
"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# comprobar si es un mail en un string dado con inicio y fin de linea
"^\w+[.-]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?$"

# Encontrar telefonos 
patron = "(+5411)([0-9]{8})"

# Obtener la lista de los substrings delimitados entre '<' y '>' que no incluyan ninguna 'o'.
"<([^o].*?)>"

