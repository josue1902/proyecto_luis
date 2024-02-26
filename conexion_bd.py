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

"""
def buscar_libro(buscar):
    cursor.execute("SELECT * FROM libro WHERE titulo = buscar") 
"""

resultado = agregar_libros("javascript", "josu", 2020)


#conexion.commit()
cursor.execute("SELECT * FROM libro")
for libro in cursor:
    print(libro)
conexion.close() # utilizado para cerrar la conexion bd, evita posibles problemas de redimiento




"""
import mysql.connector

# Generamos la conexión

cnx = mysql.connector.connect(user='root', database='biblioteca', password='123456', host='localhost')

# Cursor 
cursor = cnx.cursor()


def get_all_books():
    global cnx
    global cursor
    query = ("SELECT * FROM libro")
    # Ejecutamos
    cursor.execute(query)
    # Obtenemos los resultados
    results = cursor.fetchall()
    
    cursor.close()
    cnx.close()
    return results

def get_one_book(id):
    global cnx
    global cursor
    query = ("SELECT * FROM libro WHERE id_libro= %s")
    # Ejecutamos
    cursor.execute(query, (id,))
    # Obtenemos los resultados
    result = cursor.fetchone()
    
    cursor.close()
    cnx.close()
    return result

def insert_book(book):
    global cnx
    global cursor
    query = """INSERT INTO libro 
               (titulo, autor, anio_publicacion, prestado) 
               VALUES (%(titulo)s, %(autor)s, %(anio_publicacion)s, %(prestado)s)"""
    cursor.execute(query, book)
    cnx.commit()
    cursor.close()
    cnx.close()
    print('Se realizó con éxito la insertion')

def update_book(book):
    global cnx
    global cursor
    query = """
            UPDATE libro
            SET titulo = %(titulo)s, autor = %(autor)s, anio_publicacion = %(anio_publicacion)s, prestado = %(prestado)s
            WHERE id_libro = %(id_libro)s;
            """
    cursor.execute(query, book)
    cnx.commit()
    cursor.close()
    cnx.close()

def delete_book(id):
    global cnx
    global cursor
    query = "DELETE FROM libro WHERE id_libro = %s;"
    cursor.execute(query, (id,))
    cnx.commit()
    cursor.close()
    cnx.close()
    print("Se eliminó el libro con éxito")

if _name_ == '_main_':
    # book = get_one_book(52)
    # print(book)
    book = {
        'id_libro': 52,
        'titulo': 'Por el camino de Swann',
        'autor': 'Proust',
        'anio_publicacion': '1999',
        'prestado': True
    }
    # update_book(book)
    # insert_book(book)
    # delete_book(52)
    book = get_one_book(52)
    print(book)

"""