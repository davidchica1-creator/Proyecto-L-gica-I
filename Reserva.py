import numpy as np

class Reserva:
    
    def __init__(self, usuario:int, identificador_funcion:int, cant_boletas:int, asientos:np.ndarray, precio_total:int):
        self.__usuario = usuario
        self.__identificador_funcion = identificador_funcion
        self.__cant_boletas = cant_boletas
        self.__asientos = np.full((cant_boletas,), fill_value=1, dtype=int)
        self.__precio_total = precio_total

    def generar_boleta(self) -> None:
        print("Boleta de Reserva")
        print(f"Usuario: {self.__usuario}")
        print(f"Identificador de Función: {self.__identificador_funcion}")
        print(f"Cantidad de Boletas: {self.__cant_boletas}")
        print(f"Asientos: {self.__asientos}")
        print(f"Precio Total: {self.__precio_total}")
