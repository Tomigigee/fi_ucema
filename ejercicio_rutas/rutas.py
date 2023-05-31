import os, sys

print(os.getcwd()) #directorio en el que estamos trabajando
os.chdir("../")
print(os.getcwd())
print(os.listdir())
#os.mkdir("nuevo directorio")
os.chdir("nuevo directorio")
print(os.getcwd())


sys.exit() #terminar la ejecucion de un programa
