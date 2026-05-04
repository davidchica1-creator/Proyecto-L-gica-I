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
    
    def crear_cliente(self, nombre: str, usuario: int) -> bool:
        
            self.__nombre = input("Ingrese el nombre completo del cliente: ")
            self.__usuario = int(input("Ingrese el usuario (documento) del cliente: "))
            self.__contrasena = (f"{self.__usuario}{self.__nombre[0].lower()}*") 
            lista_usuarios = open("usuarios.txt" , "r")

            for linea in lista_usuarios:
                dato = linea.strip().split(",")

                if dato[1] == str(self.__usuario):
                    print("El usuario ya tiene una cuenta existente.")
                    return False
                
                else:
                    lista_usuarios = open("usuarios.txt" , "a")
                    lista_usuarios.write(f"{self.__nombre}, {self.__usuario}, {self.__contrasena}, 3\n")
                    lista_usuarios.close()
                    print("El cliente se ha creado con éxito.")
                    return True
                    