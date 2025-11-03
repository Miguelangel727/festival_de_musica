from musica.Festival import Cantante,DJ,Banda,iniciar_festival
def main():
    lista_artistas = []

    print("Bienvenido al simulador del Festival Musical")
    n = int(input("¿Cuántos artistas se presentarán? "))

    for i in range(n):
        print(f"\n--- Artista #{i+1} ---")
        tipo = input("Tipo de artista (Cantante / DJ / Banda): ").strip().capitalize()
        nombre = input("Nombre del artista: ")
        genero = input("Género musical: ")
        popularidad = int(input("Popularidad (1-100): "))

        if tipo == "Cantante":
            cancion = input("Canción más popular: ")
            artista = Cantante(nombre, genero, popularidad, cancion)

        elif tipo == "Dj":
            estilo = input("Estilo del DJ: ")
            artista == DJ(nombre, genero, popularidad, estilo)

        elif tipo == "Banda":
            integrantes = int(input("Número de integrantes: "))
            artista = Banda(nombre, genero, popularidad, integrantes)

        else:
            print("Tipo no válido, se omitirá este artista.")
            continue

        lista_artistas.append(artista)

    iniciar_festival(lista_artistas)


if __name__ == "__main__":
    main()
