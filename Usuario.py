import numpy as np

class Usuario:
    
    def __init__(self,nombre:str, usuario:int, tipo_usuario:int ):
        self.__nombre = nombre
        self.__usuario = usuario
        self.__contrasena = (f"{self.__usuario}{self.__nombre[0].lower()}*") 
        self.__tipo_usuario = tipo_usuario
        self.usuarios = np.full((100), fill_value = None, dtype = object)
        self.contUsuario = 0
        
        
    def get_nombre(self) -> str:

        return self.__nombre
    
    def get_tipo_usuario(self) -> int:

        return self.__tipo_usuario
    
    
    def crear_cliente(self) -> bool:
        
            self.__nombre = input("Ingrese el nombre completo del cliente: ")
            self.__usuario = int(input("Ingrese el usuario (documento) del cliente: "))
            self.__contrasena = (f"{self.__usuario}{self.__nombre[0].lower()}*")
           
            if self.contUsuario >= 100 :
                print ("Se ha alcanzado el máximo de usuarios permitidos por el sistema.")
                return False
            
            for i in range(self.contUsuario):
                dato = self.usuarios[i].split(",")
                
                if dato[1] == str(self.__usuario):
                    print("El usuario ya tiene una cuenta.")
                    return False
                
            self.usuarios[self.contUsuario] = (f"{self.__nombre}, {str(self.__usuario)}, {self.__contrasena}, {str(3)}")
            
            self.contUsuario += 1
            
            print(f"El cliente se ha creado con éxito. Información de la cuenta:\n {self.usuarios[self.contUsuario]}")
            return True            