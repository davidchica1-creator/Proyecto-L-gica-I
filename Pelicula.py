from funciones_utiles import solicitar_dato

class Pelicula:
    def __init__(self,nombre_espanol:str, nombre_original:str, anno_estreno:int, duracion:int, genero:str, pais_origen:str, calificacion:str, estado:bool):
        self.__nombre_espanol = nombre_espanol
        self.__nombre_original = nombre_original
        self.__anno_estreno = anno_estreno
        self.__duracion = duracion
        self.__genero = genero
        self.__pais_origen = pais_origen
        self.__calificacion = calificacion
        self.__estado = estado

    def agregar_pelicula(self)-> str:
        print("Hola Administrador, vas a agregar una pelicula, por favor ingrese todos los siguientes datos:\n")
        self.__nombre_espanol = input("Ingrese el nombre en español de la pelicula: \n")
        solicitar_dato(self.__nombre_espanol, "texto")

        self.__nombre_original = input("Ingrese el nombre original de la pelicula: \n")

        self.__anno_estreno = int(input("Ingrese el año de estreno de la pelicula: \n"))

        self.__duracion = int(input("Ingrese la duracion (en minutos) de la pelicula: "))

        self.__genero = int(input("Ingrese el genero de la pelicula:\n1) Drama \n2) Suspenso \n3) Terror \n4) Acción \n5) Comedia \n6)Infantil\n"))

        self.__pais_origen = input("Ingrese el pais de origen de la pelicula:\n")

        self.__calificacion = int(input("Ingrese la calificacion de la pelicula: \n"))

        self.__estado = int(input("Ingrese el estado:\n1) Activo \n2) Inactivo"))