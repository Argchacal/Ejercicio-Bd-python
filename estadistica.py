
# Crea un grafico Torta

def mostrar_estadisticas():
    import psycopg2
    import pandas as pd
    import matplotlib.pyplot as plt

    con = psycopg2.connect(host= "localHost",
                        database ="data",#la base de dato debe estar creada en pgAdmin4
                        user ="postgres",
                        password= "")#Recuerde que debe ingresar entre las comillas la contraceña de su base de datos
    

    sql = pd.read_sql_query("SELECT * FROM usuario", con)
    df = pd.DataFrame(sql, columns=["email", "password", "sexo"])

    df.groupby("sexo").size()
    
    conteo_variable=df["sexo"].value_counts()
    etiquetas=df["sexo"].unique()
    colores=["green","pink","red"]
    fig, ax=plt.subplots(figsize=(10,5))
    plt.pie(conteo_variable,labels=etiquetas, 
            autopct="%0.2f %%", 
            colors=colores)
    ax.set_title("Porcentaje por clase \n", fontsize=15, fontweight="bold")
    plt.rcParams.update({'font.size': 12, 'font.weight' : 'bold'}) 
    plt.show()

 