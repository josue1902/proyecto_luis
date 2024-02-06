from ejercicio import Biblioteca

biblioteca1 = Biblioteca()

biblioteca1.agregar_libros("python", "josue", 2002)
biblioteca1.agregar_libros("java", "sebastiaan", 2023)
#biblioteca1.buscar_libro("python")
biblioteca1.prestar_libro("josue", "20 de enero", "java")
biblioteca1.devolver_libro("java")
biblioteca1.mostrar_libros()
