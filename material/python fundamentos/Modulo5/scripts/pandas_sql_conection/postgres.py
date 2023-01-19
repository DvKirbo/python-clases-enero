import pandas as pd
import pyodbc as podbc


def conexion_sql_server(conn_str):
    print("realizando conexion SQL")
    connection = podbc.connect(conn_str)
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


conn_str = (
    "DRIVER={PostgreSQL Unicode};"
    "DATABASE=postgres;"
    "UID=postgres;"
    "PWD=postgres;"
    "SERVER=localhost;"
    "PORT=5432;"
    )

conexion = conexion_sql_server(conn_str)

df = select_to_df('select * from postgres.public.alumno;',conexion)


print(df.head())


print(df.codigo)