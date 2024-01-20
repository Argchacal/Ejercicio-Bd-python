from operar_bd import *

def cuenta_nueva():# Esto se debe mejorar para que compruebe si el mail ya esta registrado
    
    email = input("Ingrese el correo electronico ")
    contraceña = input("Ingrese la contraceña ")
    sexo = input("Ingrese la Sexo ")
    carga_bd (email, contraceña, sexo)

def mostrar_estadisticas(email, contraceña):
    comprobar_contraceña (email, contraceña)

#main

opcion = int(input ("Introdusca 1: Crear Cuenta Nueva \n2: Usuario existente \n3: Exit \n "))



if opcion == 1:
    cuenta_nueva()

if opcion == 2:
    email = input("Ingrese el correo electronico ")
    if comprobar_email (email):
        contraceña = input("Ingrese la contraceña ")
        comprobar_contraceña(email, contraceña)
        #     mostrar_estadisticas()

elif opcion == 3:
    print ("Exit")