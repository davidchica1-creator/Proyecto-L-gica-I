import numpy as np
from funciones_utiles import solicitar_dato, limpiar_pantalla
from Pelicula import*
from Funcion import*

'''
Autor: Juan David Ortiz Diaz  
Fecha: 04/05/2026
Clase Usuario
'''

class Usuario:

    """
    Autor: Salome Garcia Velasquez
    Fecha: 04/05/2026  
    Método constructor de la clase Usuario  
    Entradas: nombre, usuario, tipo_usuario  
    Salidas: None  
    """ 

    def __init__(self,nombre:str, usuario:int, tipo_usuario:int ):
    
   
        self.__nombre = nombre
        self.__usuario = usuario
        self.__contrasena = (f"{self.__usuario}{self.__nombre[0].lower()}*")
        self.__tipo_usuario = tipo_usuario

    '''
    Autor: Salome Garcia Velasquez
    Fecha: 04/05/2026  
    Metodos getter de: nombre, usuario, contrasena, tipo_usuario
    Entradas: Ninguna
    Salidas: cadenas de texto y entero, respectivamente
    '''

    def get_usuario(self)->str:
        return self.__usuario
    
    def get_nombre(self) -> str:
        
        return self.__nombre
    
    def get_contrasena(self)->str:
        return self.__contrasena
    
    def get_tipo_usuario(self) -> int:
        
        return self.__tipo_usuario     
    
    '''
    Autor: Salome Garcia  
    Fecha: 04/05/2026  
    Método menu_admin: Muestra el menú del administrador y permite ejecutar funciones de gestión del sistema.  
    Entradas: sistema
    Retorna: None  
    '''

    def menu_admin(self, sistema) -> None:

        while True:
            encabezado = "|         Bienvenido al menú admin          |"
            separador = "-" * len(encabezado)
            print(f"\n{separador}")
            print(encabezado)
            print(separador)

            opcion = solicitar_dato("Ingresa una de la opciones:\n\n1) Crear clientes\n2) Consultar programacion\n3) Consultar informacion de las peliculas\n4) Gestionar programacion\n5) Crear o modificar pelicula\n6) Consultar porcentaje de ocupacion\n7) Consultar recaudo\n8) Crear salas\n9) Salir\n\n", "numero", 1, 9)
                
            match opcion:            
                case 1:
                    sistema.crear_cliente()
                case 2:
                    sistema.menu_programacion()
                case 3:
                    sistema.mostrar_lista_peliculas()
                case 4:
                    sistema.gestionar_programacion()
                case 5:
                    encabezado = "|         Gestionar peliculas          |"
                    separador = "-" * len(encabezado)
                    print(f"\n{separador}")
                    print(encabezado)
                    print(separador)

                    print("\n\t1) Crear pelicula\n\t2) Modificar estado de pelicula\n\t3) Salir\n")
                    sub_opcion = solicitar_dato("Seleccione una opción: ", "numero", 1, 3)
                    match sub_opcion:


                        case 1:
                            sistema.agregar_pelicula()
                        case 2:
                            if sistema.contador_peliculas == 0:
                                print("No hay películas registradas en el sistema.")
                                continue
                            else:
                                sistema.mostrar_lista_peliculas()
                                numeral_pelicula = solicitar_dato("Ingrese el número de la película a modificar: ", "numero", 1, sistema.contador_peliculas)
                                pelicula_seleccionada = sistema.peliculas[numeral_pelicula - 1]
                                pelicula_seleccionada.cambiar_estado()
                case 8:
                    sistema.menu_crear_sala()

                case 9:
                    break
                        
    '''
    Autor: Juan David Ortiz Diaz  
    Fecha: 04/05/2026  
    Método menu_vendedor: Muestra el menú del vendedor y permite gestionar clientes, consultar información y visualizar mapas de funciones.  
    Entradas: sistema
    Salidas: None  
    '''

    def menu_vendedor(self, sistema) -> None:
    
        while True:
            encabezado = "|         Bienvenido al menú vendedor          |"
            separador = "-" * len(encabezado)
            print(f"\n{separador}")
            print(encabezado)
            print(separador)

            opcion = solicitar_dato("\nIngresa una de la opciones:\n\n1) Crear clientes\n2) Consultar programacion\n3) Consultar info de la peliculas\n4) Reserva boletas\n5) Salir\n", "numero", 1, 5)
            
            if opcion == 5:
                break
                
            match opcion:
                case 1:
                    sistema.crear_cliente()
                
                case 2:
                    sistema.menu_programacion()

                case 3:
                    sistema.mostrar_lista_peliculas_activas()

                case 4:

                    encabezado = "|         Reserva de boletas          |"
                    separador = "-" * len(encabezado)
                    print(f"\n{separador}")
                    print(encabezado)
                    print(separador)

                    sub_opcion = solicitar_dato("\n1. Visualizar mapa\n2. Reservar boleta\nSeleccione: ", "numero", 1, 2)
                    match sub_opcion:
                        case 1:
                            sistema.mostrar_mapa_funcion()

                        case 2:
                            documento = solicitar_dato("Ingrese su número de documento: ", "numero")
                            usuario = sistema.get_usuario_por_documento(documento)
                            
                            salas = sistema.complejo.get_lista_salas()
                            encabezado = f"| {'#':<3} | {'Sala ID':<15} | {'Valor boleta':<20} | {'Filas':<15} | {'Sillas/Fila':<15} |"
                            separador = "-" * len(encabezado)
                            print(f"\n{separador}")
                            print(encabezado)
                            print(separador)
                            for i in range(len(salas)):
                                if salas[i] is not None:
                                    print(f"| {i+1:<3} | {salas[i].mostrar_info()}")       
                            print(separador)
                            
                            identificador_sala = solicitar_dato("Seleccione el ID de la sala: ", "numero")
                            sala = sistema.complejo.get_sala(identificador_sala)
                            programacion = sala.get_programacion()
                            encabezado = f"| {'#':<3} | {'ID función':<10} | {'Fecha':<15} | {'Hora inicio':<15} |"
                            separador = "-" * len(encabezado)
                            print(f"\n{separador}")
                            print(encabezado)
                            print(separador)
                            for i in range(len(programacion)):
                                if programacion[i] is not None:
                                    print(f"| {i+1:<3} | {programacion[i].info_modificar_funcion()}")
                            print(separador)
                            identificador_funcion = solicitar_dato("Ingrese el ID de la función: ", "numero")
                            cant_boletas = solicitar_dato("Ingrese la cantidad de boletas: ", "numero")
                            fila = solicitar_dato("Ingrese la fila: ", "numero")
                            columna_inicial = solicitar_dato("Ingrese la columna inicial: ", "numero")
                            sistema.reservar_boleta(usuario, sala, identificador_funcion, identificador_sala, cant_boletas, fila, columna_inicial)
                                                    

    '''
    Autor: Salome Garcia    
    Fecha: 04/05/2026
    Método menu_cliente: Muestra el menú del cliente y permite consultar información, visualizar mapas de funciones y realizar reservas.
    Parámetros: sistema (objeto sistemaCine)
    Retorna: None
=======
    Autor: Juan David Ortiz Diaz  
    Fecha: 04/05/2026  
    Método menu_cliente: Muestra el menú del cliente y permite consultar programación, ver información de películas y gestionar reservas.  
    Entradas: sistema  
    Salidas: Ninguno    

    '''

    def menu_cliente(self, sistema) -> None:

        while True:
            encabezado = f"|         Bienvenido al menú {self.__nombre}         |"
            separador = "-" * len(encabezado)
            print(f"\n{separador}")
            print(encabezado)
            print(separador)
            opcion = solicitar_dato("\nIngresa una de la opciones:\n\n1.Consultar programacion\n2.Consultar info de la peliculas\n3.Reservar boletas\n4.Salir\n\n", "numero", 1, 4)
            
                
            match opcion:
                case 1:
                    sistema.menu_programacion()
                case 2:
                    sistema.mostrar_lista_peliculas_activas()
 
                case 3:
                    sub_opcion = solicitar_dato("Ingresa una de las opciones:\n1.Visualizar mapa\n2.Reservar boleta\n", "numero", 1, 2)
                    match sub_opcion:
                        case 1:
                            sistema.mostrar_mapa_funcion()
                        case 2:
                            sistema.reservar_boleta(self, sistema.complejo, sistema.peliculas)
                case 4:
                    break