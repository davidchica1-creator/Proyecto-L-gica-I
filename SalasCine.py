'''
Autor: David Chica López
Fecha: 03/06/2026
Clase SalaCine: Representa una sala de cine dentro de un complejo.
Atributos: identificador_sala, valor_boleta, cant_filas, sillas_por_fila, tamanio, programacion
'''

from Funcion import *
import numpy as np

class SalaCine:

    def __init__(self, identificador_sala:int, valor_boleta:int, cant_filas:int, sillas_por_fila:int):
        self.__identificador_sala = identificador_sala
        self.__valor_boleta = valor_boleta
        self.__cant_filas = cant_filas
        self.__sillas_por_fila = sillas_por_fila
        self.__tamanio = self.__cant_filas * self.__sillas_por_fila
        self.__programacion = np.full((5), fill_value = None, dtype = object)

    def get_programacion(self):
        return self.__programacion
    
    def get_identificador(self):
        return self.__identificador_sala
    
    def get_valor_boleta(self):
        return self.__valor_boleta

    def mostrar_info(self):
        return (f"{self.__identificador_sala:<15} | {self.__valor_boleta:<20} | {self.__cant_filas:<15} | {self.__sillas_por_fila:<15} |")
     
    
    def agregar_funcion(self, funcion:Funcion)-> bool:
    
        for i in range(len(self.__programacion)):
            if self.__programacion[i] is None:
                self.__programacion[i] = funcion
                return True
        return False

    def eliminar_funcion(self, identificador_funcion:int):
        pass

    def calcular_porcentaje_ocupacion(self):
        pass