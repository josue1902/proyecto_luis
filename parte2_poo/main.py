from ejercicio import Biblioteca

biblioteca1 = Biblioteca()

biblioteca1.agregar_libros("python", "josue", 2002)
biblioteca1.agregar_libros("java", "sebastian", 2005)
#biblioteca1.buscar_libro("python")
biblioteca1.prestar_libros("python", "josue", "20 de enero")
biblioteca1.devolver_libro("python")
biblioteca1.mostrar_libros()
