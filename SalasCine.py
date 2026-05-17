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
        self.__programacion = np.full((12), fill_value = None, dtype = object)
        self.__contador_funciones = 0

    
    def get_identificador(self):
        return self.__identificador_sala

    def get_cant_filas(self):
        return self.__cant_filas

    def get_sillas_por_fila(self):
        return self.__sillas_por_fila

    def agregar_funcion(self, funcion:Funcion)-> bool:
        if self.__contador_funciones >= 12:
            print(f"Error: La sala {self.__identificador_sala} ya tiene el máximo de funciones (12).")
            return False
        
        for i in range(len(self.__programacion)):
            if self.__programacion[i] is None:
                self.__programacion[i] = funcion
                self.__contador_funciones += 1
                print("Función agregada con éxito a la sala.")
                return True
        return False
    

    def eliminar_funcion(self, identificador_funcion:int):
        pass

    def calcular_porcentaje_ocupacion(self):
        pass