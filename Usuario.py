import numpy as np
from funciones_utiles import solicitar_dato
from Pelicula import*
from Funcion import*

class Usuario:
    """
    Esta clase sirve para manejar los usuarios del sistema, guardar y crear clientes nuevos.
    
    """
    
    def __init__(self,nombre:str, usuario:int, tipo_usuario:int ):
    
        """
    Método constructor con los datos del usuario, se inicializa el arreglo de los clientes y el contador 
    Los parametros son nombre (string del nombre completo), usuario(número de documento)
    y tipo de usuario (1 para admin, 2 para vendedor, 3 para cliente), la contraseña la automatiza 
    el sistema.
    El método no retorna nada.
    """ 
        self.__nombre = nombre
        self.__usuario = usuario
        self.__contrasena = (f"{self.__usuario}{self.__nombre[0].lower()}*") #secuencia armada por el sistema para creación de contraseña
        self.__tipo_usuario = tipo_usuario

        
    def get_usuario(self)->str:
        return self.__usuario
    
    def get_nombre(self) -> str:
        
        """
    Getter que devuelve el nombre del usuario, no recibe parámetros y retorna un string
    """
        return self.__nombre
    
   
    def get_tipo_usuario(self) -> int:
        
        """
    Getter que devuelve el tipo de usuario, no recibe parámetros y retorna un entero
    """
        return self.__tipo_usuario
    
    def get_contrasena(self)->str:
        return self.__contrasena
         
    
    '''
Autor: Juan David Ortiz Diaz  
Fecha: 04/05/2026  
Método menu_admin: Muestra el menú del administrador y permite ejecutar funciones de gestión del sistema.  
Parámetros: sistema (objeto sistemaCine)  
Retorna: None  
'''

    def menu_admin(self, sistema)->None:
        opcion:int
        print("Bienvenido Admin:\n")
        opcion=int(input("Ingresa una de la opciones:\n1.Crear clientes\n2.Consultar programacion\n3.Consultar info de la pelicula\n4.Gestionar programacion\n5.Crear o modificar pelicula\n6.Consultar porcentaje de ocupacion\n7.Consultar recaudo\n8.Crear salas\n9.Salir\n"))
        match opcion:            
            case 1:
                sistema.crear_cliente()
            case 5:
                pelicula:Pelicula
                pelicula=Pelicula()
                pelicula.agregar_pelicula()
            
    
    '''
Autor: Juan David Ortiz Diaz  
Fecha: 04/05/2026  
Método menu_vendedor: Muestra el menú del vendedor y permite gestionar clientes, consultar información y visualizar mapas de funciones.  
Parámetros: sistema (objeto sistemaCine)  
Retorna: None  
'''
    def menu_vendedor(self, sistema)->None:
        mapa:Funcion
        mapa=Funcion()
        opcion=(input("Ingresa una de la opciones:\n1.Crear clientes\n2.Consultar programacion\n3.Consultar info de la pelicula\n4.Reserva boletas\n5.Salir\n"))
        solicitar_dato(opcion,"numero",1,5)
        opcion=int(opcion)
        match opcion:
            case 1:
                sistema.crear_cliente()
            case 3:
                opcion=input("Ingresa una de las opciones:\n1.Visualizar mapa\n2.Reservar boleta")
                solicitar_dato(opcion,"numero",1,2)
                opcion=int(opcion)
                match opcion:
                    case 1:
                        id_funcion=int(input("ingresa el identificador de la funcion: "))
                        id_pelicula=input("Ingresa el identificador de la pelicula: ")
                        fecha=input("Ingresa la fecha, asi (DD//MM//AA): ")
                        hora_inicio=int(input("Ingresa la hora de inicio, (HH:DD)"))
                        num_filas=int(input("Ingresa el numero de filas: "))
                        num_columnas=int(input("Ingresa el numero de columnas"))
                        mapa:Funcion
                        mapa=Funcion(id_funcion,id_pelicula,fecha,hora_inicio,num_filas,num_columnas)
                        mapa.mostrar_mapa()
                    case 2:
                        print("Aun no se ha implementado")

            case 5:
                print("Hasta luego")

    '''
Autor: Juan David Ortiz Diaz  
Fecha: 04/05/2026  
Método menu_cliente: Muestra el menú del cliente y permite consultar programación, ver información de películas y gestionar reservas.  
Parámetros: Ninguno  
Retorna: None  
'''

    def menu_cliente(self)->None:
        opcion=(input("Ingresa una de la opciones:\n1.Consultar programacion\n2.Consultar info de la pelicula\n3.Reservar boletas\n4.Salir"))
        solicitar_dato(opcion,"numero",1,2)
        opcion=int(opcion)
        match opcion:
            case 1:
                print("Consultar programacion (no implementado)")                        
            case 2:
                opcion=int(input("Ingresa una de las opciones:\n1.Visualizar mapa\n2.Reservar boleta"))
                solicitar_dato(opcion,"numero",1,2)
                match opcion:
                    case 1:
                        id_funcion=int(input("ingresa el identificador de la funcion: "))
                        id_pelicula=input("Ingresa el identificador de la pelicula: ")
                        fecha=input("Ingresa la fecha, asi (DD//MM//AA): ")
                        hora_inicio=(input("Ingresa la hora de inicio, (HH:DD)"))
                        num_filas=int(input("Ingresa el numero de filas: "))
                        num_columnas=int(input("Ingresa el numero de columnas"))
                        mapa:Funcion
                        mapa=Funcion(id_funcion,id_pelicula,fecha,hora_inicio,num_filas,num_columnas)
                        mapa.mostrar_mapa()
                    case 2:
                        print("Aun no se ha implementado")