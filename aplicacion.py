# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 09:51:09 2022

@author: Alumno
"""

print("Ingrese sus datos: \n")

bandera = True
contador = 0
while bandera == True and contador < 2:
    
    login = input("Nombre de usuario: ")
    clave = input("Clave: ")

    archivoLogin = open("login.txt","rt",encoding='utf8')
    login2 = archivoLogin.read()

    archivoClave = open("clave.txt","rt",encoding='utf8')
    clave2 = archivoClave.read()

    if login == login2 and clave == clave2:
        print("\n\ntDatos Persona\n")
        print("1. Listar personas\n2. Agregar personas\n3. Salir")
        bandera = False
    else:
        print("Credenciales incorrectas, intente nuevamente\n")
        contador += 1