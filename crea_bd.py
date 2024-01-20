
"""Base de dato creada en pgAdmin4 """

import psycopg2

#Este espacio lo cree para que puedan crear su tabla en PgAdmin4  marcelo

# hosts = input ("Introdusca el host " )
# databas = input ("Introdusca su nombre de database ") 
# usuario = input ("Introdusca su usuario ")
# contraceña = input ("Introdusca su usuario ")
# con = psycopg2.connect(host= hosts,
#                     database =databas,
#                     user =usuario,
#                     password= contraceña)
con = psycopg2.connect(host= "localHost",
                    database ="data",
                    user ="postgres",
                    password= "Bartousai2020")
cur= cur = con.cursor()



comando = """CREATE TABLE IF NOT EXISTS usuario (id serial PRIMARY KEY, 
    email VARCHAR(50),
    password VARCHAR(50),
    sexo VARCHAR(8))"""

cur.execute(comando)
con.commit()
cur.close()
con.close()
