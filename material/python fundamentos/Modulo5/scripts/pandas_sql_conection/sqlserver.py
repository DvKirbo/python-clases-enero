import pandas as pd
import pyodbc as podbc


def conexion_sql_server(driver,server,database,username,password):
    print("realizando conexion SQL")
    connection = podbc.connect('DRIVER='+driver+
                                ';SERVER='+server+
                                ';DATABASE='+database+
                                ';UID='+username+
                                ';PWD='+ password)
    print("exito!!")
    return connection


def select_to_df(sql_query,connection):
    #conectando a la base de datos
    try:
        #pasanod info a df
        df = pd.read_sql(sql_query, connection)
    except Exception as e:
        print(e)
    
    #cerrando conexion
    connection.close()
    return df
    
driver='{SQL Server Native Client 11.0}'
server='localhost'
database='db_python'
username='gdelgadr'
password='gdelgadr'

conexion = conexion_sql_server(driver,server,database,username,password)

df = select_to_df('select * from datos',conexion)

print(df.head)