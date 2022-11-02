import os

def agregar(nombre,contenido):
    archivo = open(nombre,"at")
    archivo.write(contenido)
    archivo.close()