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
        titulo = input("Ingrese el titulo del libro: ")
        #if opcion == "salir":
            #break

        autor = input("Ingresa el autor del libro: ")
        anio_publicacion = int(input("Ingresa el año de publicacion: "))
        estado = True

        libro_ingresado = [titulo, autor, anio_publicacion]
        biblioteca.append(libro_ingresado)


    elif opcion == 2:
        titulo_libro = input("Ingresa el titulo del libro: ")
        libro_encontrado = False

        for libro in biblioteca:
            if titulo_libro in libro[0]:
                print("Datos del libro solicitado: ",libro)
                libro_encontrado = True
                break
        if not libro_encontrado:
            print("No se ha encontrado el libro")

    elif opcion == 3:
        nombre = input("Ingresa tu nombre: ")
        fecha = input("Ingresa la fecha: ")
        #prestado = [nombre, fecha]

        libro_nombre = input("Ingresa el titulo del libro que quieres pedir prestado: ")

        libro_encontrado = False
        for libro  in biblioteca:
            if libro_nombre in libro[0]:
                libro_encontrado = libro
                break

        if libro_encontrado:
            prestado = [nombre, fecha, libro_encontrado]
            biblioteca.remove(libro_encontrado)
            print(f"Se ha prestado el libro {libro_nombre} a {nombre} en la fecha {fecha}")


        else:
            print(f"El libro {libro_nombre} no esta disponible")

    elif opcion == 4:
        nombre_devolver = input("Ingresa tu nombre para devolver el libro: ")
        for libro in prestado:
            if titulo in prestado[0]:
                prestado.remove(prestado)

        print(f"El libro {prestado} se ha devuelto")


    elif opcion == 5:
        for libro in biblioteca:
            
            print("Los libros disponibles de la biblioteca son:", libro)




# falta la opcion 5 terminar
        

#si el libro esta en la lista biblioteca, significa que el libro esta disponible