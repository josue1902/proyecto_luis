import mysql.connector
import datetime
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

def agregar_libros(titulo, autor, anio_publicacion, prestado):
    add_libros = "INSERT INTO libro (titulo, autor, anio_publicacion, prestado) VALUES (%s, %s, %s, %s)"
    valores = (titulo, autor, anio_publicacion, False)
    cursor.execute(add_libros, valores)
    conexion.commit()



def buscar_libro(buscar):
    obtener = "SELECT * FROM libro WHERE titulo = %s" # %s marcador de posicion, sera reemplazado mas adelante, cuando le pasemos el valor de busqueda
    cursor.execute(obtener, (buscar,))
    result = cursor.fetchone()
    return result

def prestar_libro(conexion,libros, id_usuario, fecha):
    for libro in libros:
        condicion = ("SELECT * FROM libro WHERE id_libro = %s AND prestado = FALSE")
        cursor.execute(condicion,(libro,))
        resultado = cursor.fetchone()
        print(resultado)
        if resultado:
            query = "INSERT INTO prestado (id_libro, id_usuario, fecha) VALUES (%s, %s, %s)"
            valores = (libro, id_usuario, fecha)
            cursor.execute(query, valores)
            update = ("UPDATE libro SET prestado = TRUE WHERE id_libro = %s")
            cursor.execute(update,(libro,))
            print(f"El libro {libro} se presto")
        else:
            print("El libro no existe o ya fue prestado")
    conexion.commit()
    cursor.close()

#agregar = agregar_libros("java", "mateo", 2002, False)

"""def borrar_tabla():
    borrar = ("DELETE FROM libro")
    cursor.execute(borrar)
    conexion.commit()


borrar = borrar_tabla()"""

libros = [8] # libros a prestar

resultado = prestar_libro(conexion, libros,1, datetime.datetime.now())