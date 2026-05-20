'''
Autor: David Chica López
Fecha: 04/05/2026
Clase Complejo: Representa un complejo de cines que contiene varias salas de cine.
Atributos: nombre, direccion, lista_salas, cantidad_salas
'''

import numpy as np
from SalasCine import *
from funciones_utiles import solicitar_dato, validar_formato, horas_minutos, limpiar_pantalla
from Funcion import *




class Complejo:

    '''
    Autor: David Chica López
    Fecha: 04/05/2026
    Método constructor de la clase Complejo
    Entradas: None
    Salidas: None
    '''

    def __init__ (self):

        self.__nombre:str = ""
        self.__direccion:str = ""
        self.__lista_salas = np.full((12), fill_value = None, dtype = object)
        self.__cantidad_salas = 0


    '''
    Autor: David Chica López
    Fecha: 04/05/2026
    Métodos: agregar_sala, recibe como parámetro un objeto SalaCine y lo agrega a la lista de salas del complejo. 
    Devuelve True si se agregó correctamente, o False si no se pudo agregar ( en caso de que el complejo ya tenga 12 salas)
    y al agregar una sala, se incrementa el contador de cantidad_salas.
    '''

    def agregar_sala(self, sala: SalaCine) -> bool:
        for i in range(len(self.__lista_salas)):
            if self.__lista_salas[i] is None:
                self.__lista_salas[i] = sala
                self.__cantidad_salas += 1
                print(f"\nSala {sala.get_identificador()} agregada al complejo.")
                return True
        print("No se pueden agregar más salas al complejo. Capacidad máxima alcanzada.")
        return False
    
    '''
    Autor: David Chica López
    Fecha: 17/05/2026
    Metodo get_lista_salas: Retorna la lista de salas del complejo.
    Entradas: None
    Salidas: lista_salas
    '''
    
    def get_lista_salas(self):
        return self.__lista_salas
    
    '''
    Autor: David Chica López
    Fecha: 17/05/2026
    Método crear_funcion: Permite crear una funcion en una sala seleccionada. Verifica que existan salas y peliculas registradas.
    Entradas: sistema_cine, sala_seleccionada
    Salidas: None
    '''
    
    def crear_funcion(self, sistema_cine, sala_seleccionada: SalaCine) -> None:
    
            '''
            En caso de querer modificar una funcion se verifica que la cantidad de funciones para esa sala no supere el limite de 5
            '''

            if sala_seleccionada.get_cant_funciones() >= 5:
                print("La sala ya tiene el máximo de funciones permitidas.")
                return
            elif sistema_cine.contador_peliculas == 0:
                print("No hay películas registradas en el sistema.")
                return
                
            encabezado = "|         Registro de nueva función          |"
            separador = "-" * len(encabezado)   

            print(f"\n{separador}")
            print(encabezado)
            print(separador)
            
            while True:
                identificador_funcion = solicitar_dato("Ingrese el identificador de la función: ", "numero")
                
                existe = False
                for funcion in sala_seleccionada.get_programacion():
                    if funcion is not None and funcion.get_id_funcion() == identificador_funcion:
                        print(f"Error: Ya existe una función con el ID {identificador_funcion} en esta sala.")
                        existe = True
                        break
                
                if not existe:
                    break
            
            '''
            Se muestran las peliculas disponibles para agendar funciones y se le pide el ID de la pelicula a agendar
            '''

            print("\nPelículas disponibles:")
            sistema_cine.mostrar_lista_peliculas_activas()
        
            identificador_pelicula = -1
            while True:

                '''
                Se le pide el ID al administrador de la pelicula a agendar y se verifica que sea de una pelicula que exista y que ademnas sea de la lista de 
                peliculas activas que se muestran
                '''
                id_buscado = solicitar_dato("\nIngrese el ID de la película para la función: ", "numero")
                peli_encontrada = None
                for i in range(sistema_cine.contador_peliculas):
                    p = sistema_cine.peliculas[i]
                
                    if p is not None and p.get_id() == id_buscado and p.get_estado():
                        peli_encontrada = p
                        break
                
                if peli_encontrada:
                    identificador_pelicula = peli_encontrada.get_id()
                    break
                else:
                    print(f"Error: El ID {id_buscado} no corresponde a ninguna película de la lista de disponibles.")

            fecha = solicitar_dato("\nIngrese la fecha de la función (DD/MM/AAAA): ", "fecha")

            hora_inicio = solicitar_dato("\nIngrese la hora de inicio (HH:MM): ", "hora")

            '''
            Se valida que la nueva funcion no se cruce con ninguna otra funcion. 
            Se agregan 15 minutos de margen para limpieza de la sala.
            '''
            duracion_peli_nueva = peli_encontrada.get_duracion()
            minutos_inicio_peli_nueva = horas_minutos(hora_inicio)
            minutos_fin_peli_nueva = minutos_inicio_peli_nueva + duracion_peli_nueva + 15
            
            cruce_de_horario = False
            for funcion_actual in sala_seleccionada.get_programacion():
                if funcion_actual is not None and funcion_actual.get_fecha() == fecha:
                    
                    peli_ya_programada = None
                    for peli in sistema_cine.peliculas:
                        if peli is not None and peli.get_id() == funcion_actual.get_identificador_pelicula():
                            peli_ya_programada = peli
                            break
                    
                    if peli_ya_programada is not None:
                        minutos_inicio_existente = horas_minutos(funcion_actual.get_hora_inicio())
                        minutos_fin_existente = minutos_inicio_existente + peli_ya_programada.get_duracion() + 15
                        
                        if minutos_inicio_peli_nueva < minutos_fin_existente and minutos_inicio_existente < minutos_fin_peli_nueva:
                            cruce_de_horario = True
                            break
            
            if cruce_de_horario == True:
                print("\nError: La función coincide con el horario de otra película ya programada en esta sala.")
                return
            

            cant_filas = sala_seleccionada.get_cant_filas()

            sillas_por_fila = sala_seleccionada.get_sillas_por_fila()

            nueva_funcion = Funcion(identificador_funcion, identificador_pelicula, sala_seleccionada.get_identificador(), fecha, hora_inicio, cant_filas, sillas_por_fila)
            
            if sala_seleccionada.agregar_funcion(nueva_funcion):
                print(f"Función creada y agregada a la sala {sala_seleccionada.get_identificador()}")
            else:
                print("No se pudo crear la función.")

    '''
    Autor: David Chica López
    Fecha: 17/05/2026
    Metodo modificar_funcion: Permite modificar una funcion en una sala seleccionada. Verifica primeramente que la sala tenga al menos una funcion.
    Entradas: sistema_cine, sala_seleccionada
    Salidas: None

    '''

    def modificar_funcion(self, sistema_cine, sala_seleccionada: SalaCine) -> None:
        if sala_seleccionada.get_cant_funciones() == 0:
            print("No hay funciones programadas en esta sala.")
            return

        encabezado = "|         Modificar función          |"
        separador = "-" * len(encabezado)
        print(f"\n{separador}")
        print(encabezado)
        print(separador)   

        header_tabla = f"| {'#':<3} | {'ID sala':<10} | {'ID función':<10} | {'Nombre pelicula':<20} | {'Fecha':<15} | {'Hora inicio':<15} |"
        sep_tabla = "-" * len(header_tabla)
        
        print(f"\n{sep_tabla}")
        print(header_tabla)
        print(sep_tabla)
        
        for i in range(len(sala_seleccionada.get_programacion())):
            if sala_seleccionada.get_programacion()[i] is not None:
                print(f"| {i+1:<3} {sala_seleccionada.get_programacion()[i].info_modificar_funcion()}")
        print(sep_tabla)

        funcion_a_modificar = None
        while True:
            funcion_seleccionada = solicitar_dato("Ingrese el ID de la función que desea modificar: ", "numero")
            for func in sala_seleccionada.get_programacion():
                if func is not None and func.get_id_funcion() == funcion_seleccionada:
                    funcion_a_modificar = func
                    break
            
            if funcion_a_modificar:
                print(f"Vas a modificar la función con el ID {funcion_seleccionada}")
                break
            else:
                print(f"Error: No existe una función con el ID {funcion_seleccionada} en esta sala.")
                return

        print("\nPelículas disponibles:")
        sistema_cine.mostrar_lista_peliculas_activas()
        
        identificador_pelicula = -1
        peli_encontrada = None
        while True:
            id_buscado = solicitar_dato("\nIngrese el nuevo ID de la película: ", "numero")
            for i in range(sistema_cine.contador_peliculas):
                p = sistema_cine.peliculas[i]
                if p is not None and p.get_id() == id_buscado and p.get_estado():
                    peli_encontrada = p
                    break

            if peli_encontrada:
                identificador_pelicula = peli_encontrada.get_id()
                break
            else:
                print("Error: El ID ingresado no es válido o no está en la lista de películas activas.")

        fecha = solicitar_dato("Ingrese la nueva fecha de la función (DD/MM/AAAA): ", "fecha")
        hora_inicio = solicitar_dato("Ingrese la nueva hora de inicio (HH:MM): ", "hora")

   
        duracion_peli_nueva = peli_encontrada.get_duracion()
        minutos_inicio_peli_nueva = horas_minutos(hora_inicio)
        minutos_fin_peli_nueva = minutos_inicio_peli_nueva + duracion_peli_nueva
        minutos_fin_peli_nueva = minutos_inicio_peli_nueva + duracion_peli_nueva + 15
        
        cruce_de_horario = False
        for funcion_actual in sala_seleccionada.get_programacion():
            if funcion_actual is not None and funcion_actual.get_id_funcion() != funcion_seleccionada and funcion_actual.get_fecha() == fecha:
                peli_ya_programada = None
                for peli in sistema_cine.peliculas:
                    if peli is not None and peli.get_id() == funcion_actual.get_identificador_pelicula():
                        peli_ya_programada = peli
                        break
                
                    minutos_inicio_existente = horas_minutos(funcion_actual.get_hora_inicio())
                    minutos_fin_existente = minutos_inicio_existente + peli_ya_programada.get_duracion() + 15
                    
                    if minutos_inicio_peli_nueva < minutos_fin_existente and minutos_inicio_existente < minutos_fin_peli_nueva:
                        cruce_de_horario = True
                        break
        
        if cruce_de_horario == True:
            print("\nError: El nuevo horario se cruza con una función existente.")
            return

        funcion_a_modificar.set_identificador_pelicula(identificador_pelicula)
        funcion_a_modificar.set_fecha(fecha)
        funcion_a_modificar.set_hora_inicio(hora_inicio)
        print(f"Función con ID {funcion_seleccionada} modificada exitosamente.")

    '''
    Autor: David Chica López
    Fecha: 17/05/2026
    Metodo eliminar_funcion_de_sala: Permite eliminar una funcion de una sala seleccionada. verifica primero que la sala tenga al menos una funcion.
    Entradas: sala_seleccionada
    Salidas: None
    '''
    
    def eliminar_funcion_de_sala(self, sala_seleccionada:SalaCine) -> None:
        if sala_seleccionada.get_cant_funciones() == 0:
            print("No hay funciones programadas en esta sala.")
            return

        print("\n|         Eliminar función          |")
        header = f"| {'#':<3} | {'ID sala':<10} | {'ID función':<10} | {'Nombre pelicula':<20} | {'Fecha':<15} | {'Hora inicio':<15} |"
        separador = "-" * len(header)
        print(f"{separador}\n{header}\n{separador}")
        
        for i in range(len(sala_seleccionada.get_programacion())):
            if sala_seleccionada.get_programacion()[i] is not None:
                print(f"| {i+1:<3} | {sala_seleccionada.get_programacion()[i].info_modificar_funcion()}")
        print(separador)

        funcion_seleccionada = solicitar_dato("Ingrese el ID de la función que desea eliminar: ", "numero")
        existe = False
        for func in sala_seleccionada.get_programacion():
            if func is not None and func.get_id_funcion() == funcion_seleccionada:
                existe = True
                break
        
        if not existe:
            print(f"Error: No existe una función con el ID {funcion_seleccionada} en esta sala.")
            return
            
        eliminar = solicitar_dato(f"¿Está seguro de querer eliminar la función con el ID {funcion_seleccionada}? (si/no): ", "si_no")
        if eliminar == "si":
            sala_seleccionada.eliminar_funcion(funcion_seleccionada)

    '''
    Autor: David Chica López
    Fecha: 17/05/2026
    Metodo renovar_programacion_de_sala: Permite renovar la programación de una sala seleccionada eliminando las funciones existentes en esa sala.
    Entradas: sala_seleccionada
    Salidas: None
    '''
    
    def renovar_programacion_de_sala(self, sala_seleccionada:SalaCine) -> None:

        if sala_seleccionada.get_cant_funciones() == 0:
            print("No hay funciones programadas en esta sala.")
            return

        encabezado = "|         Renovar programación          |"
        separador = "-" * len(encabezado)
        print(f"\n{separador}")
        print(encabezado)
        print(separador)
        
        print(f"\nUsted va a renovar la programación de la sala con el ID {sala_seleccionada.get_identificador()}, esto eliminará las funciones ya existentes.\n")

        renovar_programacion = solicitar_dato("¿Está seguro de querer renovar la programación? (si/no): ", "si_no")
        if renovar_programacion == "si":

            sala_seleccionada.renovar_programacion(sala_seleccionada.get_identificador())



    '''
    Autor: David Chica López
    Fecha: 16/05/2026
    Metodo gestionar_progrmacion: Recibe de parametro un objeto del SistemaCine, no retorna nada.

    '''

    def gestionar_programacion(self, sistema_cine) -> None:

        '''
        Primeramente verifica que hayan salas y peliculas para agendar funciones
        '''
        
        if self.__cantidad_salas == 0 or sistema_cine.contador_peliculas == 0:
            print("No hay salas registradas para programar funciones o no hay películas registradas.")
            return
        
        limpiar_pantalla()
        encabezado = "|         Registro de nueva funcion          |"
        separador = "-" * len(encabezado)
        print(f"\n{separador}")
        print(encabezado)
        print(separador)

        '''
        Muestra una lista de las salas disponibles para agendar funciones
        '''

        print("\nSalas disponibles")
        encabezado = f"| {'#':<3} | {'Sala ID':<15} | {'Valor boleta':<20} | {'Filas':<15} | {'Sillas/Fila':<15} |"
        separador = "-" * len(encabezado)
        
        print(f"\n{separador}")
        print(encabezado)
        print(separador)
        
        for i in range(len(self.__lista_salas)):
            if self.__lista_salas[i] is not None:
                print(f"| {i+1:<3} | {self.__lista_salas[i].mostrar_info()}")
        print(separador)

        '''
        Se pide al administrador la sala que quiere gestionar sus funciones
        '''

        idx_sala = solicitar_dato("\nSeleccione una sala para gestionar su programación: ", "numero", 1, self.__cantidad_salas) - 1
        sala_seleccionada = self.__lista_salas[idx_sala]

        print(f"\nID de la sala seleccionada: {sala_seleccionada.get_identificador()}")

        '''
        Se muestran las distintas opciones para administrar las funciones de la sala seleccionada
        '''
              
        print("\n\n\t1) Crear función\n\t2) Modificar función\n\t3) Eliminar función\n\t4) Renovar programación\n\t5) Salir\n")
        opcion = solicitar_dato("Seleccione una opción: ", "numero", 1, 5)

        match opcion:
            case 1:
                self.crear_funcion(sistema_cine, sala_seleccionada)
            case 2:
                self.modificar_funcion(sistema_cine, sala_seleccionada)
            case 3:
                self.eliminar_funcion_de_sala(sala_seleccionada)
            case 4:
                self.renovar_programacion_de_sala(sala_seleccionada)
            case 5:
                return
