import pyodbc
import asyncio
loop = asyncio.get_event_loop()



async def queryDDL(query):

    server = 'OSCAR-DESKTOP\SQLEXPRESS'
    database = 'ss2_practica1'
    trusted_connection = 'yes'
    dns = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}"
     
    try:
        # Configura la cadena de conexión a tu servidor SQL Server
        conexion = pyodbc.connect(dns)

        # Crea un objeto cursor para ejecutar consultas
        cursor = conexion.cursor()

        # Ejecuta la consulta SQL
        cursor.execute(query)

        # Recupera los resultados (si la consulta es SELECT)
       
        if query.upper().startswith("\nSELECT"):
            resultados = cursor.fetchall()
            return resultados
        else:
            # Si la consulta no es SELECT, confirma los cambios en la base de datos
            conexion.commit()
            return "Consulta ejecutada con éxito."

    except Exception as e:
        # Captura cualquier error y muestra un mensaje de error
        return f"Error al ejecutar la consulta: {str(e)}"
    finally:
        # Cierra la conexión
        conexion.close()

def runQuery(query):
    return loop.run_until_complete( queryDDL(query))

