'''
Autor: David Chica López
Fecha: 03/06/2026
Clase SalaCine: Representa una sala de cine dentro de un complejo.
Atributos: identificador_sala, valor_boleta, cant_filas, sillas_por_fila, tamanio, programacion
'''

from Funcion import *
import numpy as np

class SalaCine:

    '''
    Autor: David Chica López
    Fecha: 03/05/2026
    Método constructor de la clase SalaCine
    Entradas: identificador_sala, valor_boleta, cant_filas, sillas_por_fila
    Salidas: None
    '''

    def __init__(self, identificador_sala:int, valor_boleta:int, cant_filas:int, sillas_por_fila:int):
        self.__identificador_sala = identificador_sala
        self.__valor_boleta = valor_boleta
        self.__cant_filas = cant_filas
        self.__sillas_por_fila = sillas_por_fila
        self.__tamanio = self.__cant_filas * self.__sillas_por_fila
        self.__programacion = np.full((5), fill_value = None, dtype = object)
        self.__contador_funciones = 0

    
    '''
    Autor: David Chica López
    Fecha: 03/05/2026
    Métodos getter de identificador_sala, cant_filas, sillas_por_fila, programacion
    Entradas: Ninguna    
    '''
    def get_identificador(self) -> int:
        return self.__identificador_sala

    def get_cant_filas(self) -> int:
        return self.__cant_filas

    def get_sillas_por_fila(self) -> int:
        return self.__sillas_por_fila

    def get_cant_funciones(self) -> int:
        return self.__contador_funciones
    
    '''
    Autor: David Chica López
    Fecha: 17/05/2026
    Métodos setter de cant_funciones
    Entradas: cant_funciones
    Salidas: None
    '''

    def set_cant_funciones(self, cant_funciones:int) -> None:
        self.__contador_funciones = cant_funciones


    def get_programacion(self):
        return self.__programacion
    
    '''
    Autor: David Chica López
    Fecha: 3/05/2026
    Metodo agregar_funcion: Permite agregar una funcion a una sala de cine. Verifica que no sobrepase el limite de 5 funciones por sala
    Entradas: funcion
    Salidas: True si se pudo agregar, False si no se pudo agregar
    '''

    def agregar_funcion(self, funcion:Funcion)-> bool:
        if self.__contador_funciones >= 5:
            print(f"Error: La sala {self.__identificador_sala} ya tiene el máximo de funciones (5).")
            return False
        
        for i in range(len(self.__programacion)):
            if self.__programacion[i] is None:
                self.__programacion[i] = funcion
                self.__contador_funciones += 1
                print("Función agregada con éxito a la sala.")
                return True
        return False

    '''
    Autor: David Chica López
    Fecha: 17/05/2026
    Metodo mostrar_info: Muestra la informacion de la sala
    Entradas: Ninguna
    Salidas: None
    '''
    
    def mostrar_info(self) -> None:
        return (f"{self.get_identificador():<15} | {self.__valor_boleta:<20} | {self.__cant_filas:<15} | {self.__sillas_por_fila:<15} |")
    
    '''
    Autor: David Chica López
    Fecha: 17/05/2026
    Metodo eliminar_funcion: Permite eliminar una funcion de una sala de cine.
    Entradas: identificador_funcion
    Salidas: None
    '''

    def eliminar_funcion(self, identificador_funcion:int) -> None:
        for i in range(len(self.__programacion)):
            if self.__programacion[i] is not None and self.__programacion[i].get_id_funcion() == identificador_funcion:
                self.__programacion[i] = None
                self.__contador_funciones -= 1
                print(f"Función con el ID {identificador_funcion} eliminada de la sala {self.__identificador_sala}")    

    '''
    Autor: David Chica López
    Fecha: 17/05/2026
    Metodo renovar_programacion: Permite renovar la programación de una sala de cine.
    Entradas: identificador_sala
    Salidas: None
    '''

    def renovar_programacion(self, identificador_sala:int) -> None:
        for i in range(len(self.__programacion)):
            if self.__programacion[i] is not None:
                id_funcion_eliminada = self.__programacion[i].get_id_funcion()
                self.__programacion[i] = None
                print(f"Función con el ID {id_funcion_eliminada} eliminada de la sala {self.__identificador_sala}")
        self.__contador_funciones = 0