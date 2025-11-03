class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def presentarse(self):
        print(f"\nHola, soy {self.nombre}, interpreto música {self.genero} y mi popularidad es {self.popularidad}/100.")

    def actuar(self):
        print("El artista se prepara para su actuación...")

    def despedirse(self):
        print(f"{self.nombre} agradece al público y se despide con una sonrisa.")



class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def actuar(self):
        print(f"{self.nombre} canta su éxito '{self.cancion_mas_popular}' con gran energía.")



class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo

    def actuar(self):
        print(f"El DJ {self.nombre} mezcla temas de estilo {self.estilo}, haciendo vibrar al público.")



class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes

    def actuar(self):
        print(f"La banda {self.nombre} con {self.integrantes} integrantes toca un poderoso solo de guitarra.")



def iniciar_festival(lista_artistas):
    print("\nComienza el Festival Musical")
    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("Fin de la actuación\n")
    print("El festival ha terminado con gran éxito.")
