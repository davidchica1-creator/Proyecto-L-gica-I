import numpy as np
from Pelicula import*
from Funcion import*
from funciones_utiles import*



class Usuario:
    
    def __init__(self,nombre:str, usuario:int, tipo_usuario:int ):
        self.__nombre = nombre
        self.__usuario = usuario
        self.__contrasena = (f"{self.__usuario}{self.__nombre[0].lower()}*") 
        self.__tipo_usuario = tipo_usuario

        
    def get_usuario(self)->str:
        return self.__usuario
    
    def get_nombre(self) -> str:

        return self.__nombre
    
    def get_tipo_usuario(self) -> int:

        return self.__tipo_usuario
    
    def get_contrasena(self)->str:
        return self.__contrasena
         
    

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
  
        