
"""Base de dato creada en pgAdmin4 """

import psycopg2

#Este espacio lo cree para que puedan crear su tabla en PgAdmin4 la base de dato llamada Data


contraseña = input ("Introdusca su usuario de su BD")

con = psycopg2.connect(host= "localHost",
                    database ="data",#la base de dato debe estar creada en pgAdmin4
                    user ="postgres",
                    password= contraseña)
cur = con.cursor()


#Crea la base de dato tenga en  cuenta que sexo pueden ser Hombre, Mujer y No binario
comando = """CREATE TABLE IF NOT EXISTS usuario (id serial PRIMARY KEY, 
    email VARCHAR(50),
    password VARCHAR(50),
    sexo VARCHAR(10))"""

cur.execute(comando)
con.commit()
cur.close()
con.close()



