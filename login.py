from operar_bd import *
from estadistica import *

def cuenta_nueva():# Esto se debe mejorar para que compruebe si el mail ya esta registrado
   
    email = input("Ingrese el correo electronico ")
    if comprobar_email (email):
        print("Correo electronico existente")
        cuenta_nueva()
      
    else:
        contraceña = input("Ingrese la contraceña ")
        sexo = input("Ingrese la Sexo ")
        carga_bd(email, contraceña,sexo)

def  usuario_apto():
    correo = input("Ingrese el correo electronico ")
    if comprobar_email (correo):
        print ("correo aceptado")
        if comprobar_contraseña(correo):
            print ("Usuario aceptado") 
            return True                    
           
        else:
            return False

#main
opcion = int(input ("Introdusca 1: Crear Cuenta Nueva \n2: Usuario existente \n3: Exit \n "))
if opcion == 1:
    cuenta_nueva()
elif opcion == 2:
            if usuario_apto():     
                mostrar_estadisticas()
            
else:
    print ("Exit")