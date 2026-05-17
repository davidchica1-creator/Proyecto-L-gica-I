'''
Autor: David Chica López
Fecha: 04/05/2026
Clase Complejo: Representa un complejo de cines que contiene varias salas de cine.
Atributos: nombre, direccion, lista_salas, cantidad_salas
'''

import numpy as np
from SalasCine import *
from funciones_utiles import solicitar_dato

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
    
    def gestionar_programacion(self):
        print("-------------------------------")
        print("|   Gestión de Programación    |")
        print("-------------------------------")
        
        if self.__cantidad_salas == 0:
            print("No hay salas registradas para programar funciones.")
            return

        print("\nSalas disponibles:")
        for i in range(len(self.__lista_salas)):
            if self.__lista_salas[i] is not None:
                print(f"{i+1}) Sala {self.__lista_salas[i].get_identificador()}")

        idx_sala = solicitar_dato("Seleccione una sala: ", "numero", 1, self.__cantidad_salas) - 1
        sala_seleccionada = self.__lista_salas[idx_sala]

        print("\n1) Crear función\n2) Modificar función\n3) Eliminar función\n4) Renovar programación\n5) Salir\n")
        opcion = solicitar_dato("Seleccione una opción: ", "numero", 1, 5)

        match opcion:
            case 1:
                print("\nCreación de función:")
                identificador_funcion = solicitar_dato("Ingrese el identificador de la función: ", "numero")
                identificador_pelicula = solicitar_dato("Ingrese el identificador de la película: ", "texto")
                fecha = solicitar_dato("Ingrese la fecha de la función (DD/MM/AAAA): ", "fecha")
                hora_inicio = solicitar_dato("Ingrese la hora de inicio (HH:MM): ", "hora")
                cant_filas = sala_seleccionada.get_cant_filas()
                sillas_por_fila = sala_seleccionada.get_sillas_por_fila()

                nueva_funcion = Funcion(identificador_funcion, identificador_pelicula, fecha, hora_inicio, cant_filas, sillas_por_fila)
                
                if sala_seleccionada.agregar_funcion(nueva_funcion):
                    print(f"Función creada y agregada a la sala {sala_seleccionada.get_identificador()}")
                else:
                    print("No se pudo crear la función.")
            case 2:
                print("\nModificación de función:")
                
            case 5:
                return
