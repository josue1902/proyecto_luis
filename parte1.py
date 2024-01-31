# 30/1/24

print("""
    Elige una opcion
    1) anadir libro
    2) Buscar libro
    3) Prestar libro
    4) Devolver libro
    5) Listar libros


""")


biblioteca = []

prestado = []
#opcion = int(input("Ingesa una opcion: "))
while True:
    opcion = int(input("Ingesa una opcion: "))

    if opcion == 1:
        titulo = input("Ingrese el titulo del libro ('salir para salir): ")
        #if opcion == "salir":
            #break

        autor = input("Ingresa el autor del libro: ")
        anio_publicacion = int(input("Ingresa el año de publicacion: "))

        libro_ingresado = [titulo, autor, anio_publicacion]
        biblioteca.append(libro_ingresado)


    elif opcion == 2:
        titulo_libro = input("Ingresa el titulo del libro: ")
        for libro in biblioteca:
            if titulo in libro[0]:
                print("Datos del libro solicitado: ",libro)
            else:
                print("No se ha encontrado el libro")

    elif opcion == 3:
        nombre = input("Ingresa tu nombre: ")
        fecha = input("Ingresa la fecha: ")
        #prestado = [nombre, fecha]

        libro_nombre = input("Ingresa el titulo del libro que quieres pedir prestado: ")

        libro_encontrado = None
        for libro  in biblioteca:
            if titulo in libro[0]:
                libro_encontrado = libro
                break

        if libro_encontrado:
            prestado = [nombre, fecha, libro_encontrado]
            biblioteca.remove(libro_encontrado)
            print("Se ha prestado el libro a", prestado )

        else:
            print(f"El libro {libro_nombre} no esta disponible")

    elif opcion == 4:
        nombre_devolver = input("Ingresa tu nombre para devolver el libro: ")
        for libro in prestado:
            if titulo in prestado[0]:
                prestado.remove(prestado)

        print(f"El libro {prestado[0]} se ha devuelto")


    elif opcion == 5:
        print(biblioteca)
        




# Errores encontrados en el momento
# 1 cuando buscamos un libro, nos sale varios mensajes que no se ha enontrado, despues que si
# 2 cuando usamos la opcion de prestar un libro, se presta el libro pero no es ese, se presta otro libro, por ejemplo, pedimos el de python y nos presta el de java
        

