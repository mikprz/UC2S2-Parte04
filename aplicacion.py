# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 09:51:09 2022

@author: Alumno
"""

import listar
import agregar

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



opcion=input('\nseleccione una opcion: ')

if opcion =='1':
    listar.listarArchivo('nombre.txt','apellido.txt','dni.txt')
elif opcion == "2":
    nuevoDNI = input("Agrega el DNI: ")
    nuevoDNI = "\n" + nuevoDNI
    agregar.agregar("dni.txt",nuevoDNI)
    nuevoNombre = input("Agrega el nombre: ")
    nuevoNombre = "\n" + nuevoNombre
    agregar.agregar("nombre.txt",nuevoNombre)
    nuevoApellido = input("Agrega el apellido: ")
    nuevoApellido = "\n" + nuevoApellido
    agregar.agregar("apellido.txt",nuevoApellido)
    print("\nNueva lista: \n")
    listar.listarArchivo('nombre.txt','apellido.txt','dni.txt')
else:
    exit()


