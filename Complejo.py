'''
Autor: David Chica López
Fecha: 04/05/2026
Clase Complejo: Representa un complejo de cines que contiene varias salas de cine.
Atributos: nombre, direccion, lista_salas, cantidad_salas
'''

import numpy as np
from SalasCine import *

class Complejo:
    def __init__ (self):

        self.__nombre:str = ""
        self.__direccion:str = ""
        self.__lista_salas = np.full((12), fill_value = None, dtype = object)
        self.__cantidad_salas = 0

        '''
        Métodos: agregar_sala, recibe como parámetro un objeto SalaCine y lo agrega a la lista de salas del complejo. 
        Devuelve True si se agregó correctamente, o False si no se pudo agregar (por ejemplo, si el complejo ya tiene 12 salas)
        y al agregar una sala, se incrementa el contador de cantidad_salas.
        '''
    def agregar_sala(self, sala: SalaCine) -> bool:
        for i in range(len(self.__lista_salas)):
            if self.__lista_salas[i] is None:
                self.__lista_salas[i] = sala
                self.__cantidad_salas += 1
                print(f"Sala {sala.get_identificador()} agregada al complejo.")
                return True
        print("No se pueden agregar más salas al complejo. Capacidad máxima alcanzada.")
        return False


