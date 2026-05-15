'''
Autor: David Chica López
Fecha: 04/05/2026
Clase Pelicula: Representa una película que se proyecta en el cine.
Atributos: nombre_espanol, nombre_original, anno_estreno, duracion, genero, pais_origen, calificacion, estado
'''

from funciones_utiles import solicitar_dato

class Pelicula:
    def __init__(self,nombre_espanol:str, nombre_original:str, identificador_pelicula:int, anno_estreno:int, duracion:int, genero:str, pais_origen:str, calificacion:str, estado:bool = True):
        self.__nombre_espanol = nombre_espanol
        self.__nombre_original = nombre_original
        self.__identificador_pelicula = identificador_pelicula
        self.__anno_estreno = anno_estreno
        self.__duracion = duracion
        self.__genero = genero
        self.__pais_origen = pais_origen
        self.__calificacion = calificacion
        self.__estado = estado

    '''
    Método: get_estado, devuelve el estado actual de la película (activa o inactiva), sin parámetros.
    '''
    def get_estado(self) -> bool:
        return self.__estado

    '''
    Método: get_estado, devuelve el estado actual de la película (activa o inactiva), sin parámetros.
    '''

    def cambiar_estado(self, pelicula:int)-> None:
        if self.get_estado():
            self.__estado = False
            print(f"La pelicula {pelicula} ha sido desactivada.")
        else:
            self.__estado = True
            print(f"La pelicula {pelicula} ha sido activada.")

    '''
    Método: get_id, devuelve el identificador único de la película.
    '''
    def get_id(self) -> int:
        return self.__identificador_pelicula

    '''
    Metodo: get_informacion, devuelve una cadena de texto con toda la información de la película. No recibe parámetros.
    '''

    def get_informacion(self) -> str:
        estado_txt = "Activa" if self.__estado else "Inactiva"
        return (f"{self.__nombre_espanol:<20} | {self.__nombre_original:<20} | {self.__anno_estreno:<15} | {self.__duracion:<10} | {self.__genero:<12} | {self.__pais_origen:<15} | {self.__calificacion:<12} | {estado_txt:<10} |")

    def get_duracion(self) -> int:
        return self.__duracion
    