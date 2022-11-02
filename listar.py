
import os


def listarArchivo(nombre,apellido,dni):
    archivo=open(nombre,'r')
    archivo_1=open(apellido,'r')
    archivo_2=open(dni,'r')
    #archivo=open(nombre,"rt",encoding='utf8')

    #print(archivo.readline())
    #num=len(archivo)

    print("Nombre\t\t\tApellido\t\t\tDNI")
    print("______\t\t\t________\t\t\t___")
    for x in range(20):
        
        print(archivo.readline().rstrip("\n"),"\t\t\t",archivo_1.readline().rstrip("\n"),"\t\t\t",archivo_2.readline().rstrip("\n"))

    #datos_archivo=archivo.read()
    #print(datos_archivo)