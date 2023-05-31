email --> "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

--> [a-zA-Z0-9._%+-]+ 
    coincide con una o más letras, números o caracteres especiales que se permiten en una dirección de correo electrónico, como puntos (.), guiones (-), porcentajes (%) o signos más (+).
--> @ 
    coincide con el carácter de arroba que separa el nombre de usuario del dominio en una dirección de correo electrónico.
--> [a-zA-Z0-9.-]+ 
    coincide con una o más letras, números, guiones o puntos en el dominio.
--> \. 
    coincide con un punto literal en la dirección de correo electrónico.
--> [a-zA-Z]{2,} 
    coincide con dos o más letras en la parte del dominio de nivel superior (TLD) de la dirección de correo electrónico. Por ejemplo, .com, .org, .edu.

gmail --> "[a-zA-Z0-9._%+-]+@gmail\.com"

