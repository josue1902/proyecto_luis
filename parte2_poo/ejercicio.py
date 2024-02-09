# Clases
class Biblioteca:
    def __init__(self):
        self.biblioteca = {}
        self.libros = [] # agregamos los libros
        self.prestar = []   #prestar un libro

    def agregar_libros(self, titulo, autor, anio_publicacion):
        if titulo in self.libros:
            print("El libro ya se encuentra en la biblioteca")
        else:
            libro_ingresado = [titulo, autor, anio_publicacion]
            self.libros.append(libro_ingresado)
            self.biblioteca['Libros'] = self.libros ################


    def buscar_libro(self, libro_a_buscar):
        libro_encontrado = False
        for libro in self.libros:
            if libro_a_buscar == libro[0]:
                libro_encontrado = True
                print(f"Información del libro buscado: {libro}")

                break
        if not libro_encontrado:
            print("No se encuentra el libro en la biblioteca")

    def prestar_libros(self, libro_a_prestar, nombre, fecha):
        libro_encontrado = False
        #prestar = []
        for libro in self.libros:
            if libro_a_prestar == libro[0]:
                info = [libro, nombre, fecha] 
                self.prestar.append(info[0])
                self.libros.remove(libro)
                libro_encontrado = True
                break
        if not libro_encontrado:
            print("El libro no se ha encontrado")

    def devolver_libro(self, libro_a_devolver):
        for libro in self.prestar:
            if libro_a_devolver == libro[0]:
                self.libros.append(libro)
                self.prestar.remove(libro) 
                print(f"Se ha devuelto el libro {libro[0]}")
                break
        else:
            print("No se ha encontrado el libro")

    def mostrar_libros(self):
        print("LIbros no disponibles:", self.prestar)
        print("Libros disponibles:", self.biblioteca)


        
