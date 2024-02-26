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

def agregar_libros(titulo, autor, anio_publicacion):
    add_libros = "INSERT INTO libro (titulo, autor, anio_publicacion, prestado) VALUES (%s, %s, %s, %s)"
    valores = (titulo, autor, anio_publicacion, None)
    cursor.execute(add_libros, valores)



def buscar_libro(buscar):
    obtener = "SELECT * FROM libro WHERE titulo = %s" # %s marcador de posicion, sera reemplazado mas adelante, cuando le pasemos el valor de busqueda
    cursor.execute(obtener, (buscar,))
    result = cursor.fetchone()
    return result

def prestar_libro(libro_a_prestar):
     pass

