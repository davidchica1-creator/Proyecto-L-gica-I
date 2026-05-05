from Usuario import*
from funciones_utiles import*
class sistemaCine:
    def __init__(self):
        self.usuarios = np.full((100), fill_value = None, dtype = object)
        self.contador_clientes=0
        self.contador_peliculas=0


    def crear_cliente(self) -> bool:
    
        self.__nombre = input("Ingrese el nombre completo del cliente: ")
        self.__usuario = int(input("Ingrese el usuario (documento) del cliente: "))
        self.__contrasena = (f"{self.__usuario}{self.__nombre[0].lower()}*")
        
        if self.contUsuario >= 100 :
            print ("Se ha alcanzado el máximo de usuarios permitidos por el sistema.")
            return False
        
        for i in range(self.contador_clientes):
            if self.usuarios[i] is not None:
                if self.usuarios[i].get_usuario() == self.__usuario:
                    print("El usuario ya existe")
                    return False

        
        nuevo = Usuario(self.__nombre,self.__usuario, 3)

        self.usuarios[self.contador_clientes] = nuevo
        self.contador_clientes += 1

        print("Cliente creado con éxito")
        print("Usuario:", self.__usuario)
        print("Contraseña:", self.__contrasena)

        return True
    
    def login(self)->None:
        opcion:int
        user:Usuario
        usuario_ingresado:str
        contrasena:str
        print("Bienvenidos a ¿Qué hay para ver?")
        opcion=(input("Ingresa una de las opciones:\n1.Ingresar.\n2.Salir\n"))
        #solicitar_dato(opcion,"numero",1,2)
        opcion=int(opcion)
        match opcion:
            case 1:
                usuario_ingresado=input("Ingrese el usuario: ")
                contrasena=input("Ingresa la contrasena: ")
                if usuario_ingresado=="Admin123" and contrasena=="Admin123*":
                    user=Usuario("Admin",123,1)
                    user.menu_admin(self)
                elif usuario_ingresado=="Vendedor123" and contrasena=="Vendedor123*":
                    user=Usuario("Vendedor",1234,2)
                    user.menu_vendedor(self)
                else:
                    for i in range(self.contador_clientes):
                        cliente=self.usuarios[i]
                        if cliente.get_usuario()==usuario_ingresado and cliente.get_contrasena()==contrasena:
                            cliente.menu_cliente()
                    print("Usuario no encontrado")

            case 2:
                print("Hasta luego")
                        


quehay:sistemaCine
quehay=sistemaCine()
quehay.login()

        

