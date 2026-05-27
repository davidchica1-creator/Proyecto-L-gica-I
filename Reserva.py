'''
Autor: David Chica López
Fecha: 04/05/2026
Clase Reserva: Representa una reserva de boletas para una función de cine.
Atributos: usuario, identificador_funcion, identificador_sala, cant_boletas, asientos, precio_total
'''


import numpy as np
from datetime import datetime

class Reserva:
    
    def __init__(self, usuario:int, identificador_funcion:int, identificador_sala:int, cant_boletas:int, asientos:np.ndarray, precio_total:int):
        self.__usuario = usuario
        self.__identificador_funcion = identificador_funcion
        self.__identificador_sala = identificador_sala
        self.__cant_boletas = cant_boletas
        if asientos is not None:
            self.__asientos = asientos
        else:
            self.__asientos = np.full((cant_boletas,), fill_value=1, dtype=int)
        self.__precio_total = precio_total
        self.__fecha_venta = datetime.now().strftime("%d/%m/%Y")
        self.__hora_venta = datetime.now().strftime("%H:%M")

    '''
    Metodo: generar_boleta, muestra la información de la reserva, incluyendo el usuario, el identificador de la función, 
    la cantidad de boletas, los asientos reservados y el precio total.
    Parámetros: No recibe parámetros.
    Retorna: None
    '''
    def get_cant_boletas(self) -> int:
        return self.__cant_boletas
    
    def get_asientos(self) -> np.ndarray:
        return self.__asientos
    
    def get_usuario(self) -> int:
        return self.__usuario
    
    def get_id_funcion(self) -> int:
        return self.__identificador_funcion

    def get_precio_total(self) -> int:
        return self.__precio_total
    
    def get_fecha_venta(self) -> str:
        return self.__fecha_venta
    
    def get_hora_venta(self) -> str:
        return self.__hora_venta
    
    def get_sala(self) -> int:
        return self.__identificador_sala

    
