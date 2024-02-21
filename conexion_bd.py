import mysql.connector
conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "biblioteca"


)

if conexion.is_connected():
    print("Conexion a la base de datos")
else:
    print("No te has conectado a la base de datos")


cursor = conexion.cursor()


titulo = "python"
autor = "josue"
anio_publicacion = 2003
#prestado = 0

sql = "INSERT INTO libro (titulo, autor, anio_publicacion, prestado) VALUES (%s, %s, %s, %s)"

valores = (titulo, autor, anio_publicacion)

cursor.execute(sql, valores)

conexion.commit()

conexion.close() # este objeto nos permite interactuar con la bd mediante le ejecucion de comandos sql.
