#Aqui voy a trabajar la base de dato carga y extraccion de datos
#Para operar la base de datos debe indicar la password de su base de datos  
import psycopg2


def carga_bd (email, contraceña, sexo):
    try:
        con = psycopg2.connect(host= "localHost",
                    database ="data",
                    user ="postgres",
                    password= "")
        cur=con.cursor()

        comando = """INSERT INTO usuario (email, password, sexo) VALUES (%s, %s, %s)"""
        datos = (email,contraceña, sexo)
        cur.execute(comando,datos)
        con.commit()
        print("Cuenta nueva creada")

    
    
    finally:
        cur.close()
        con.close()


#Comprueva que la el email este en la base de datos
def comprobar_email (correo):
    try:
        con = psycopg2.connect(host= "localHost",
                    database ="data",#la base de dato debe estar creada en pgAdmin4
                    user ="postgres",
                    password= "")#Recuerde que debe ingresar entre las comillas la contraceña de su base de datos
    
        cur=con.cursor()
        
        comando = "SELECT email,password,sexo FROM usuario WHERE email = %s;"
        
        cur.execute(comando,(correo,))
        con.commit()
        datos =cur.fetchall()
        
        datos2 = datos[0]
        

        if datos2[0] == correo:
            return True
    except:
        return False
    finally:
        cur.close()
        con.close()

#Comprueva que la contraceña coincida con la de la base de datos del email ingresado

def comprobar_contraseña(email):
    con = psycopg2.connect(host= "localHost",
                    database ="data",
                    user ="postgres",
                    password= "")
    cur=con.cursor()
    


    try:
        contraseña = input("Ingrese la contraceña ")
        comando = "SELECT email,password,sexo FROM usuario WHERE email = %s;"
        cur.execute(comando,(email,))
        con.commit()
        datos =cur.fetchall()
        datos2= datos[0]
        if datos2 [1] == contraseña:
            return True
        else:
            opcion = input("No es la contraseña correcta, ingrese 1 para intentarlo nuevamente")
            if opcion == "1":

                comprobar_contraseña(email)
            return False
    finally:
        cur.close()
        con.close()
 
        


    
    
    



