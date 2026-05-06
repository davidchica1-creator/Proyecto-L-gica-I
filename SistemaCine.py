from Usuario import*
from funciones_utiles import solicitar_dato
from SalasCine import*
from Pelicula import*

class SistemaCine:
    def __init__(self):
        self.usuarios = np.full((100), fill_value = None, dtype = object)
        self.contador_clientes=0
        self.contador_peliculas=0

    '''
    Autor: Juan David Ortiz Diaz  
    Fecha: 04/05/2026  
    Método crear_cliente: Permite registrar un nuevo cliente en el sistema validando que no exista previamente.  
    Parámetros: Ninguno  
    Retorna: bool (True si se crea correctamente, False si falla)  
    '''
    def crear_cliente(self) -> bool:
    
        self.__nombre = solicitar_dato("Ingrese el nombre completo del cliente: ", "texto")
        self.__usuario = solicitar_dato("Ingrese el usuario (documento) del cliente: ", "numero")
        self.__contrasena = (f"{self.__usuario}{self.__nombre[0].lower()}*")
        
        if self.contador_clientes >= 100 :
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

        print("\nCliente creado con éxito\n")
        print("Las credenciales del nuevo cliente son:\n")
        print("Usuario:", self.__usuario)
        print("Contraseña:", self.__contrasena)

        return True
    
    '''
    Autor: Juan David Ortiz Diaz  
    Fecha: 04/05/2026  
    Método login: Gestiona el inicio de sesión de usuarios (admin, vendedor o cliente) y redirige al menú correspondiente.  
    Parámetros: Ninguno  
    Retorna: None  
    '''
    def login(self)->None:
        opcion:int
        user:Usuario
        usuario_ingresado:str
        contrasena:str
        while True:
            print("\n------------------------------")
            print("Bienvenidos a ¿Qué hay para ver?")
            print("------------------------------")
            opcion = solicitar_dato("1. Ingresar\n2. Salir\nSeleccione una opción: ", "numero", 1, 2)


            if opcion == 2:
                print("Hasta luego")
                break

            usuario_ingresado = input("Ingrese el usuario: ")
            contrasena = input("Ingresa la contrasena: ")

            if usuario_ingresado == "Admin123" and contrasena == "Admin123*":
                user = Usuario("Admin", 123, 1)
                user.menu_admin(self)
            elif usuario_ingresado == "Vendedor123" and contrasena == "Vendedor123*":
                user = Usuario("Vendedor", 1234, 2)
                user.menu_vendedor(self)
            else:
                encontrado = False
                for i in range(self.contador_clientes):
                    cliente = self.usuarios[i]
                    if str(cliente.get_usuario()) == usuario_ingresado and cliente.get_contrasena() == contrasena:
                        cliente.menu_cliente()
                        encontrado = True
                        break
                if not encontrado:
                    print("\n[!] Error: Usuario no encontrado o contraseña incorrecta.")
                        
    '''
    Autor: Juan David Ortiz Diaz  
    Fecha: 04/05/2026  
    Método menu_crear_sala: Permite registrar una nueva sala de cine solicitando los datos necesarios y validándolos.  
    Parámetros: complejo (objeto que gestiona las salas de cine)  
    Retorna: None  
    '''


    def menu_crear_sala(self, complejo):
        print("Registro de Nueva Sala")


        identificador_sala = solicitar_dato("Ingrese el identificador de la sala (1-12): ", "numero", 1, 12)

        valor_boleta = solicitar_dato("Ingrese el valor de la boleta: ", "numero", 1)


        cant_filas = solicitar_dato("Ingrese cantidad de filas: ", "numero", 1)

        sillas_por_fila = solicitar_dato("Ingrese sillas por fila: ", "numero", 1)

        nueva_sala = SalaCine(identificador_sala, valor_boleta, cant_filas, sillas_por_fila)
        
        exito = complejo.agregar_sala(nueva_sala)
        
        if exito:
            print("Proceso terminado con éxito.")
        else:
            print("No se pudo realizar el registro.")

obj:SistemaCine

obj = SistemaCine()

obj.login()