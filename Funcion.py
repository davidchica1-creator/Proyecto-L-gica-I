import numpy as np

class Funcion:
    def __init__(self, identificador_funcion:int, identificador_pelicula:str, fecha:str, hora_inicio:int, cant_filas:int, sillas_por_fila:int):
        self.__identificador_funcion = identificador_funcion
        self.__identificador_pelicula = identificador_pelicula
        self.__fecha = fecha
        self.__hora_inicio = hora_inicio
        self.__cant_filas = cant_filas
        self.__sillas_por_fila = sillas_por_fila
        self.__mapa_sala = np.zeros((self.__cant_filas,self.__sillas_por_fila), dtype=int)

    def mostrar_mapa(self)->None:
        print(f"\nMapa de la Funcion")

        for i in range(self.__sillas_por_fila):
            print(i + 1, end = " ")
        print()

        for i in range(self.__filas):
            
            letra = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
            print(letra[i], end="  ")
            
            for j in range(self.__sillas_por_fila):
                
                if self.__mapa_sala[i, j] == 0:
                    print(".", end=" ")
                else:
                    print("X", end=" ")
            print()

    def verificar_disponibilidad(self, asiento_inicial,):
        pass