'''
Autor: David Chica López
Fecha: 04/05/2026
Clase Pelicula: Representa una película que se proyecta en el cine.
Atributos: nombre_espanol, nombre_original, anno_estreno, duracion, genero, pais_origen, calificacion, estado
'''

from funciones_utiles import solicitar_dato

class Pelicula:

    '''
    Autor: David Chica López
    Fecha: 03/05/2026
    Método constructor de la clase Pelicula
    Entradas: nombre_espanol, nombre_original, identificador_pelicula, anno_estreno, duracion, genero, pais_origen, calificacion, estado
    Salidas: None
    '''

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
    Autor: Salome Garcia Velasquez
    Fecha: 12/05/2026
    Método: get_estado, devuelve el estado actual de la película (activa o inactiva), sin parámetros.
    Entradas: None
    Salidas: False en caso de que la película esté inactiva, True en caso contrario.
    '''
    def get_estado(self) -> bool:
        return self.__estado

    '''
    Autor: David Chica López
    Fecha: 04/05/2026
    Metodo cambiar_estado: Permite cambiar el estado de una pelicula, si esta activa su estado cambia a desactivada y viseversa
    Entradas: Indice de la pelicula a modificar
    Salidas: None
    '''

    def cambiar_estado(self)-> None:
        if self.get_estado():
            self.__estado = False
            print(f"La pelicula '{self.__nombre_espanol}' ha sido desactivada.")
        else:
            self.__estado = True
            print(f"La pelicula '{self.__nombre_espanol}' ha sido activada.")

    '''
    Autor: David Chica López
    Fecha: 04/05/2026
    Método: get_id, devuelve el identificador único de la película.
    Entradas: None
    Salidas: identificador_pelicula
    '''
    def get_id(self) -> int:
        return self.__identificador_pelicula

    '''
    Autor: David Chica López
    Fecha: 04/05/2026
    Metodo: get_informacion, devuelve una cadena de texto con toda la información de la película. No recibe parámetros.
    Entradas: None
    Salidas: Cadena de texto con toda la información de la película.
    '''

    def get_informacion(self) -> str:
        estado_txt = "Activa" if self.__estado else "Inactiva"
        return (f"{self.__identificador_pelicula:<10} | {self.__nombre_espanol:<25} | {self.__nombre_original:<20} | {self.__anno_estreno:<15} | {self.__duracion:<10} | {self.__genero:<12} | {self.__pais_origen:<15} | {self.__calificacion:<12} | {estado_txt:<10} |")
    
    '''
    Autor: David Chica López
    Fecha: 17/05/2026
    Metodo get_duracion: Permite obtener la duracion de la pelicula
    Entradas: None
    Salidas: Duración de la película
    '''

    def get_duracion(self) -> int:
        return self.__duracion
    

    def get_calificacion(self):
        return self.__calificacion

    '''
    Autor: Juan David Ortiz
    Fecha: 19/05/2026
    Metodo get_nombre_espanol: Retorna el nombre en español de la película.
    Entradas: None
    Salidas: str
    '''

    def get_nombre_espanol(self) -> str:
        return self.__nombre_espanol
    
