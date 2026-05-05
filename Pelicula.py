'''
Autor: David Chica López
Fecha: 04/05/2026
Clase Pelicula: Representa una película que se proyecta en el cine.
Atributos: nombre_espanol, nombre_original, anno_estreno, duracion, genero, pais_origen, calificacion, estado
'''

from funciones_utiles import solicitar_dato

class Pelicula:
    def __init__(self,nombre_espanol:str, nombre_original:str, anno_estreno:int, duracion:int, genero:str, pais_origen:str, calificacion:str, estado:bool = True):
        self.__nombre_espanol = nombre_espanol
        self.__nombre_original = nombre_original
        self.__anno_estreno = anno_estreno
        self.__duracion = duracion
        self.__genero = genero
        self.__pais_origen = pais_origen
        self.__calificacion = calificacion
        self.__estado = estado
    '''
    Metodo: agregar_pelicula, recibe los datos de la película a través de entradas del administrador y los asigna a los atributos correspondientes.
    '''
    def agregar_pelicula(self)-> str:
        print("Hola Administrador, vas a agregar una pelicula, por favor ingrese todos los siguientes datos:\n")

        self.__nombre_espanol = input("Ingrese el nombre en español de la pelicula: \n")
        solicitar_dato(self.__nombre_espanol, "texto")

        self.__nombre_original = input("Ingrese el nombre original de la pelicula: \n")
        solicitar_dato(self.__nombre_original, "texto")

        self.__anno_estreno = input("Ingrese el año de estreno de la pelicula: \n")
        solicitar_dato(self.__anno_estreno, "entero")
        int(self.__anno_estreno)

        self.__duracion = input("Ingrese la duracion (en minutos) de la pelicula: ")
        solicitar_dato(self.__duracion, "entero", 90, 180)
        int(self.__duracion)

        self.__genero = input("Ingrese el genero de la pelicula:\n1) Drama \n2) Suspenso \n3) Terror \n4) Acción \n5) Comedia \n6)Infantil\n")
        solicitar_dato(self.__genero, "entero", 1, 6)
        int(self.__genero)
        match self.__genero:
            case 1:
                self.__genero = "Drama"
            case 2:
                self.__genero = "Suspenso"
            case 3:
                self.__genero = "Terror"
            case 4:
                self.__genero = "Acción"
            case 5:
                self.__genero = "Comedia"
            case 6:
                self.__genero = "Infantil"

        self.__pais_origen = input("Ingrese el pais de origen de la pelicula:\n")
        solicitar_dato(self.__pais_origen, "texto")

        self.__calificacion = input("Ingrese la calificacion de la pelicula: \n1) G (Para todas las edades) \n2) PG (Se recomienda la compañía de un adulto) \n3) PG-13 (No recomendado para menores de 13 años) \n4) R (Restringida, no recomendada para menores de 17 años) \n5) NC-17 (No recomendado para menores de 17 años)\n")
        solicitar_dato(self.__calificacion, "entero", 1, 7)
        int(self.__calificacion)
        match self.__calificacion:
            case 1:
                self.__calificacion = "G"
            case 2:
                self.__calificacion = "PG"
            case 3:
                self.__calificacion = "PG-13"
            case 4:
                self.__calificacion = "R"
            case 5:
                self.__calificacion = "NC-17"

        self.__estado = True

    '''
    Método: get_estado, devuelve el estado actual de la película (activa o inactiva).
    '''
    def get_estado(self) -> bool:
        return self.__estado

    '''
    Metodo: cambiar_estado, recibe como parámetro el nombre de la película y cambia su estado de activa a inactiva o viceversa.
    '''

    def cambiar_estado(self, pelicula:int)-> None:
        if self.get_estado():
            self.__estado = False
            print(f"La pelicula {pelicula} ha sido desactivada.")
        else:
            self.__estado = True
            print(f"La pelicula {pelicula} ha sido activada.")

    '''
    Metodo: get_informacion, devuelve una cadena de texto con toda la información de la película.
    '''

    def get_informacion(self) -> str:
        return f"Nombre en español: {self.__nombre_espanol}\nNombre original: {self.__nombre_original}\nAño de estreno: {self.__anno_estreno}\nDuración: {self.__duracion} minutos\nGénero: {self.__genero}\nPaís de origen: {self.__pais_origen}\nCalificación: {self.__calificacion}\nEstado: {'Activa' if self.__estado else 'Inactiva'}"
    
    def get_duracion(self) -> int:
        return self.__duracion
    