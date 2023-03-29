#!/bin/python3
import os, sys

def main():
   print("hola")

usuario = sys.argv[1]#sys.arg toma los argumentos que le pasamos al script por consola; [1] significa que siempre voy a tomar el primero


def saludador(nombre):
    return "Hola" + " " + str(nombre)

if __name__ == "__main__":
    print(saludador(usuario))

