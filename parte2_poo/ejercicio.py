class Biblioteca:
    def __init__(self):
        self.biblioteca = {}
        self.libros = {}
        self.libros_prestados = {}
    def agregar_libros(self, titulo, autor, anio_publicacion):
        if titulo in self.libros:
            print("El libro ya se encuentra en la biblioteca")
        else:
            libro_nuevo = {"Titulo" : titulo, "Autor" : autor, "anio publicacion" : anio_publicacion}
            self.libros[titulo] = libro_nuevo
            self.biblioteca = self.libros

    def mostrar_libros(self):
        print(self.biblioteca)


    def buscar_libro(self, nombre_libro):
        libro_encontrado = False
        for libro in self.libros:
            if nombre_libro == libro:
                libro_encontrado = True
                break
        if libro_encontrado:
            print(f"Información del libro buscado: {self.libros[nombre_libro]}")
        else:
            print("El libro que estas buscando, no se encuentra")

    def prestar_libro(self, nombre, fecha, libro_prestar):
        #libros_prestados = {}
        libro_encontra = None
        for libro in self.biblioteca:
            if libro_prestar in libro:
                libro_encontra = libro

                break
        if libro_encontra:
            libros_prestados = libro
            del self.biblioteca[libros_prestados]

            print(f"El libro {libros_prestados} fue prestado a {nombre} en la fecha {fecha}")
        else:
            print("No se encontro el libro")


    def devolver_libro(self, libro_a_devolver):
        for libro, info in self.libros_prestados.items():
            if libro_a_devolver == info["Titulo"]:
                self.biblioteca[libro] = info
                del self.libros_prestados[libro]
                break