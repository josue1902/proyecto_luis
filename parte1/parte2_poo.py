class Biblioteca:
    def __init__(self):
        self.biblioteca = {}

        self.libros = {}

    def agregar_libro(self, titulo, autor, anio_publicacion):
        #lista = []
        if titulo in self.libros:
            print("El libro ya se encuentra en la biblioteca")
        else:
            libro_nuevo = {"titulo": titulo, 'autor': autor, 'anio de publicacion': anio_publicacion} 
            self.libros[titulo] = libro_nuevo
            self.biblioteca = self.libros
   
    def mostrar_biblioteca(self):          
        print(self.biblioteca)


    def buscar_libro(self, buscar):
        pass
        









biblioteca1 = Biblioteca()

biblioteca1.agregar_libro("Metas", "brian", 2002)
biblioteca1.agregar_libro("python", "josue", 2022)
biblioteca1.agregar_libro("java", "jorge", 2002)
biblioteca1.agregar_libro("c#", "nicolas", 2003)
biblioteca1.agregar_libro("javascript", "sebastian", 2015)

biblioteca1.mostrar_biblioteca()

biblioteca1.buscar_libro("python")