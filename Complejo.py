import numpy as np
from SalasCine import *

class Complejo:
    def __init__ (self):

        self.__nombre:str = ""
        self.__direccion:str = ""
        self.__lista_salas = np.full((12), fill_value = None, dtype = object)
        self.__cantidad_salas = 0

    def agregar_sala(self, sala: SalaCine) -> bool:
        for i in range(len(self.__lista_salas)):
            if self.__lista_salas[i] is None:
                self.__lista_salas[i] = sala
                self.__cantidad_salas += 1
                print(f"Sala {sala.get_identificador()} agregada al complejo.")
                return True
        print("No se pueden agregar más salas al complejo. Capacidad máxima alcanzada.")
        return False


