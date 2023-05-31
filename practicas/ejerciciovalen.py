import re, os, sys, glob

"""Creá una carpeta llamada “CarpetaParcial” en la que existan 2 archivos .txt que contengan la
siguiente información (los archivo .txt, también tenés que crearlos vos bro):
Contenido del archivo 1:
643262462352362463262+46+423crnewuvpn3t42+3235523+verw+5491142342353532mcw
iromvvwrwrvervwr43v4*3
Contenido del archivo2:
64326246235236bwrbew+54911542263632623r246326vew2+46+423crneevwwuvpnew3tv
ew42+3235523+verw+5491v142342353532mcwiromvvwrwrvervwr43v4*3
Deberás extraer los números de teléfono de CABA (+54911########) y guardarlos en un
archivo nuevo, en una carpeta llamada” Telefonos”, creada dentro de la CarpetaParcial.
Buena suerte!
"""

def ejercicio_valen(archivo_salida):
    os.chdir("carpetaparcial")
    #os.mkdir("Telefonos")
    txt = glob.glob("*.txt")
    for archivo in txt:
        with open(archivo, "r") as file1:
            archivo_leido = file1.read()
            telefonos = re.findall("[+]54911[0-9]{8}", archivo_leido)
        os.chdir("Telefonos")
        with open(archivo_salida, "a") as file2:
            for nro in telefonos:
                file2.write(nro + "\n")
        os.chdir("..") 


print(ejercicio_valen("telefonos.txt"))
#\+54911[0-9]{8}

#2) Buscar en una cadena los siguiente caracteres “&*@” y reemplzarlos por “|”.
def ale(string):
    return re.sub("@|&|[*]", "|", string)
    
print(ale("m@r&d*n@"))


"""3) Buscar en la siguiente secuencia, todos los patrone que comiencen por & y caben por %$
Secuencia:
“vwrevwn35n32o5n32n532jin532&vewkvnemvoseomom&l;mewvemwovew;m*&^6vaevvke
ms;vevm%$vewwv%$ feveve vkwe[31532095llc;ac7777&&&&&f32f45123%$”
"""


#3
def buscar_patron(string):
    return re.findall("&([^&].*?)[%][$]", string)
print(buscar_patron("vwrevwn35n32o5n32n532jin532&vewkvnemvoseomom&l;mewvemwovew;m*&^6vaevvkems;vevm%$vewwv%$ feveve vkwe[31532095llc;ac7777&&&&&f32f45123%$"))


#&[^&]+[^%$]+[$%]

"""#44) En un curso lleno de buenas personas, Tomás Gigena se revela y comienza a hacer desastres.
Tiene una ira inicial la cual puede ir aumentando o disminuyendo. Puede pegarle_al_profe y
esto incrementará su ira en la cantidad de fuerza con que le haya pegado. También es capaz
de dar_el_presente cuando no dijeron su nombre, lo que lo hace enfurece aún más y su ira
aumenta en 20. También sabe responder si esta_en_su_prime, cuando su ira es mayor a 90.
Finalmente, es capaz de matar_compañeros, y esto depende de su ira. Si es máxima
(ira=100), puede matar 10 tipos, si no es másxima, matará siguiendo la proporción.
"""

class Tomas:
    def __init__(self):
        self.ira = 50

    def pegarle_al_profesor(self, fuerza):
        self.ira += fuerza
    
    def dar_el_presente(self):
        self.ira += 20
    



