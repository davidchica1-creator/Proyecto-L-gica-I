'''
Autor: David Chica López
Fecha: 03/05/2026
Clase Funcion: Representa una función de cine dentro de una sala.
Atributos: identificador_funcion, identificador_pelicula, fecha, hora_inicio, cant_filas, sillas_por_fila, mapa_sala
'''

import numpy as np
from Pelicula import *


class Funcion:

    '''
    Autor: David Chica López
    Fecha: 2/05/2026
    Método constructor de la clase Funcion
    Entradas: identificador_funcion, identificador_pelicula, fecha, hora_inicio, cant_filas, sillas_por_fila
    Salidas: None
    '''
    
    def __init__(self, identificador_funcion:int, identificador_pelicula:int, identificador_sala:int, fecha:str, hora_inicio:str, cant_filas:int, sillas_por_fila:int):
        self.__identificador_funcion = identificador_funcion
        self.__identificador_pelicula = identificador_pelicula
        self.identificador_sala = identificador_sala
        self.__fecha = fecha
        self.__hora_inicio = hora_inicio
        self.__cant_filas = cant_filas
        self.__sillas_por_fila = sillas_por_fila
        self.__mapa_sala = np.zeros((self.__cant_filas,self.__sillas_por_fila), dtype=int)
        self.__asientos_reservados = 0
    '''
    Autor: David Chica López
    Fecha: 17/05/2026
    Metodos getters de: id_funcion, identificador_pelicula, fecha, hora_inicio
    Entradas: Ninguna
    Salidas: None
    '''

    def get_id_funcion(self) -> int:
        return self.__identificador_funcion

    def get_identificador_pelicula(self) -> int:
        return self.__identificador_pelicula

    def get_fecha(self) -> str:
        return self.__fecha

    def get_hora_inicio(self) -> str:
        return self.__hora_inicio

    '''
    Autor: David Chica López
    Fecha: 17/05/2026
    Metodos setters de: identificador_pelicula, fecha, hora_inicio
    Entradas: nueva_id, nueva_fecha, nueva_hora
    Salidas: None
    '''

    def set_identificador_pelicula(self, nueva_id: int) -> None:
        self.__identificador_pelicula = nueva_id

    def set_fecha(self, nueva_fecha: str) -> None:
        self.__fecha = nueva_fecha

    def set_hora_inicio(self, nueva_hora: str) -> None:
        self.__hora_inicio = nueva_hora

    '''
    Autor: David Chica López
    Fecha: 3/05/2026
    Métodos: mostrar_mapa, muestra el mapa de la sala indicando los asientos disponibles (con un punto) y los ocupados (con una X).
    Entradas: None
    Salidas: None
    '''
    def mostrar_mapa(self)->None:
        print(f"\nMapa de la Funcion")

        for i in range(self.__sillas_por_fila):
            print(i + 1, end = " ")
        print()

        for i in range(self.__cant_filas): 
            
            letra = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
            print(letra[i], end="  ")
            
            for j in range(self.__sillas_por_fila):
                
                if self.__mapa_sala[i, j] == 0:
                    print(".", end=" ")
                else:
                    print("X", end=" ")
            print()

    def get_identificador_funcion(self) -> int:
        return self.__identificador_funcion
        
    def get_mapa_sala(self) -> np.ndarray:
        return self.__mapa_sala
    
    def verificar_disponibilidad(self, asiento_inicial, cant_boletas):
        pass

    def agregar_asientos_reservados(self, cant_boletas) -> None:
        self.__asientos_reservados += cant_boletas
        


    '''
    Autor: David Chica López
    Fecha: 17/05/2026
    Metodo mostar_info: Muestra la informacion de la funcion
    Entradas: Ninguna
    Salidas: str
    '''

    def mostrar_info(self) -> str:
        return f"{self.__identificador_funcion} | {self.nombre_espanol} | {self.__fecha} | {self.__hora_inicio} |"
    
    '''
    Autor: David Chica López
    Fecha: 17/05/2026
    Metodo info_modificar_funcion: Muestra la informacion de la funcion para modificar
    Entradas: Ninguna
    Salidas: str
    '''
    
    def info_modificar_funcion(self) -> str:
        return f"{self.identificador_sala:<10} | {self.__identificador_funcion:<10} | {self.__identificador_pelicula:<20} | {self.__fecha:<15} | {self.__hora_inicio:<15} |"

    def verificar_disponibilidad(self, asiento_inicial, cant_boletas):
        
        if asiento_inicial < 0 or asiento_inicial >= self.__cant_filas * self.__sillas_por_fila:

            return False

