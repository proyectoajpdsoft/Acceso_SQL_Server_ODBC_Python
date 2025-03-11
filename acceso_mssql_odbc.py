import pyodbc

# Definimos los datos de conexión (usuario y contraseña)
USUARIO = "sa"
CONTRASENA = "MiContraseña"
ORIGEN_DATOS = "mssql"

# Definimos el string de conexión ODBC en base a los datos de conexión anteriores
strConexionODBC = f"DSN={ORIGEN_DATOS};UID={USUARIO};PWD={CONTRASENA}"

# Conectamos con el servidor de SQL Server mediante ODBC
conexion = conn = pyodbc.connect(strConexionODBC) 
cursor = conexion.cursor()

# Ejecutamos una consulta SQL de ejemplo que nos 
# devolverá el nombre de la base de datos a la que estamos conectados
sql = "select DB_NAME() as BD;"
cursor.execute(sql)
# Obtenemos el primer registro devuelto por la consulta SQL
# Y mostramos el campo "BD"
registro = cursor.fetchone()
if registro:
   print(f"{registro.BD}")
   
# Otro ejemplo, donde obtenemos y mostramos todos los registros de una tabla
# En este caso listamos los ficheros que componen la base de datos SQL Server
# de la tabla "sys.database_files"
sql = "select file_id, name, physical_name from sys.database_files order by file_id;"
cursor.execute(sql)
# Obtenemos todos los registros de la consulta SQL
# Y mostramos el campo "BD" de cada registro obtenido
registros = cursor.fetchall()
for registro in registros:
    print(f"{registro.file_id} | {registro.name} | {registro.physical_name}")
    
# Cerramos la conexión con el servidor SQL Server
cursor.close
conexion.close