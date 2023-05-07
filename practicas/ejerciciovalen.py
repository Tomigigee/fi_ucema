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
    os.mkdir("Telefonos")
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

