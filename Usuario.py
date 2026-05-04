import numpy as np
from funciones_utiles import solicitar_dato

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
        self.usuarios = np.full((100), fill_value = None, dtype = object) #arreglo de 100 espacios donde inicia cada casilla en None
        self.contUsuario = 0 #se inicializa el contador en 0
      
        
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


    
    def crear_cliente(self) -> bool:
        """
    El método crear clientes permite pedir los datos al usuario y guardarlos en el arreglo
    teniendo en cuenta que el arreglo no esté lleno y el cliente no tenga una cuenta existente
    
    No recibe parámetros y retorna un booleano que indica si se pudo crear o no el cliente.
"""
        self.__nombre = solicitar_dato("Ingrese el nombre completo del cliente: ")
        self.__usuario = int(solicitar_dato("Ingrese el usuario (documento) del cliente: "))
        self.__contrasena = (f"{self.__usuario}{self.__nombre[0].lower()}*") #se actualiza la contraseña
           
        if self.contUsuario >= 100 : #evita que se creen mas usuarios de los permitidos
            print ("Se ha alcanzado el máximo de usuarios permitidos por el sistema.")
            return False
            
        for i in range(self.contUsuario): #ciclo para comparar los datos existentes en el arreglo
            dato = self.usuarios[i].split(",") #split para separar varios datos en str de una casilla por comas
                
            if dato[1] == str(self.__usuario):
                print("El usuario ya tiene una cuenta.")
                return False
            
        #guardar cliente    
        self.usuarios[self.contUsuario] = (f"{self.__nombre}, {str(self.__usuario)}, {self.__contrasena}, {str(3)}")
            
        self.contUsuario += 1
        
        #Muestra mensaje con la info de la cliente creado en el sistema.
        print(f"El cliente se ha creado con éxito. Información de la cuenta:\n {self.usuarios[self.contUsuario - 1]}")
        return True            
"""
   Autor: Salomé García Velásquez
   Fecha: 04/05/26
   """