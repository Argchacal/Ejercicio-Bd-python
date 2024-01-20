#Aqui voy a trabajar la base de dato carga y extraccion de datos

import psycopg2


con = psycopg2.connect(host= "localHost",
                    database ="data",
                    user ="postgres",
                    password= "Bartousai2020")
cur=con.cursor()

def comprobar_contraceña(email, contraceña):
    pass


def carga_bd (email, contraceña, sexo):


    comando = """INSERT INTO usuario (email, password, sexo) VALUES (%s, %s, %s)"""
    datos = (email,contraceña, sexo)
    cur.execute(comando,datos)
    con.commit()
    
    print("Cuenta nueva creada")
    cur.close()
    con.close()

def comprobar_email (correo):
    try:
        comando = "SELECT email,password,sexo FROM usuario WHERE email = %s;"
        
        cur.execute(comando,(correo,))
        con.commit()
        datos =cur.fetchall()
        
        datos2 = datos[0]
        if datos2[0] == correo:
            print("email comprobado", datos2[0])
            
            return True
    except:
        print( correo, "No se encuentra en la base de datos")
        cur.close()
        con.close()
        return False
 


def comprobar_contraceña(email, contraceña):
    print ("email", email, "contraceña", contraceña)
    try:
        comando = "SELECT email,password,sexo FROM usuario WHERE email = %s;"
        
        cur.execute(comando,(email,))
        con.commit()


        datos =cur.fetchall()
        cur.close()
        con.close()
        datos2= datos[0]
        print ("datos", datos2)
        if datos2 [1] == contraceña:
            print ("Usuario aceptado")

        else:
            print ("No es la contraceña correcta")
    except:
        print( "es Incorrecta la contraceña")
        cur.close()
        con.close()


    print("opa q paso aqui")
 




    
    
    



