'''
Autor: David Chica López
Fecha: 04/05/2026
Clase Reserva: Representa una reserva de boletas para una función de cine.
Atributos: usuario, identificador_funcion, identificador_sala, cant_boletas, asientos, precio_total
'''


import numpy as np

class Reserva:
    
    def __init__(self, usuario:int, identificador_funcion:int, identificador_sala:int, cant_boletas:int, asientos:np.ndarray, precio_total:int):
        self.__usuario = usuario
        self.__identificador_funcion = identificador_funcion
        self.__identificador_sala = identificador_sala
        self.__cant_boletas = cant_boletas
        self.__asientos = np.full((cant_boletas,), fill_value=1, dtype=int)
        self.__precio_total = precio_total

    '''
    Metodo: generar_boleta, muestra la información de la reserva, incluyendo el usuario, el identificador de la función, 
    la cantidad de boletas, los asientos reservados y el precio total.
    Parámetros: No recibe parámetros.
    Retorna: None
    '''

    def generar_boleta(self) -> None:
        print("Boleta de Reserva")
        print(f"Usuario: {self.__usuario}")
        print(f"Identificador de Función: {self.__identificador_funcion}")
        print(f"Cantidad de Boletas: {self.__cant_boletas}")
        print(f"Asientos: {self.__asientos}")
        print(f"Precio Total: {self.__precio_total}")
