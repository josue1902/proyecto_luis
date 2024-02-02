class Biblioteca:
    def __init__(self):
        self.biblioteca = {}



    def agregar_libro(self, titulo, autor, anio_publicacion):
        lista = []
        if titulo in self.biblioteca:
            print("El libro ya se encuentra en la biblioteca")
        else:
            self.biblioteca = {"titulo": titulo, 'autor': autor, 'anio_publicacion': anio_publicacion}
            lista.append(self.biblioteca)
            print(lista)


            
    def mostrar_biblioteca(self):          
        pass        
        #print(self.lista)

biblioteca1 = Biblioteca()

biblioteca1.agregar_libro("Metas", "brian", 2002)
#biblioteca1.mostrar_biblioteca()
biblioteca1.agregar_libro("python", "josue", 2022)
#biblioteca1.mostrar_biblioteca()