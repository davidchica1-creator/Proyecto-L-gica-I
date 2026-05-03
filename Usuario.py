class Usuario:
    
    def __init__(self,nombre:str, usuario:int, contrasena:str, tipo_usuario:int ):
        self.__nombre = nombre
        self.__usuario = usuario
        self.__contrasena = contrasena
        self.__tipo_usuario = tipo_usuario

    def get_nombre(self) -> str:

        return self.__nombre
    
    def get_tipo_usuario(self) -> int:

        return self.__tipo_usuario

    
    
