from Usuario import*
from funciones_utiles import solicitar_dato
from SalasCine import*
from Pelicula import*
from Complejo import Complejo  

class SistemaCine:
    def __init__(self):
        self.usuarios = np.full((100), fill_value = None, dtype = object)
        self.contador_clientes=0
        self.peliculas = np.full((50), fill_value = None, dtype = object)
        self.contador_peliculas=0
        self.complejo = Complejo()

    '''
    Autor: Juan David Ortiz Diaz  f
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
    

    def mostrar_lista_peliculas(self) -> None:
        if self.contador_peliculas == 0:
            print("No hay películas registradas en el sistema.")
            return
        
        header = f"| {'#':<3} | {'Nombre en español':<20} | {'Nombre original':<20} | {'Año de estreno':<15} | {'Duración':<10} | {'Género':<12} | {'Pais de origen':<15} | {'Calificación':<12} | {'Estado':<10} |"
        separador = "-" * len(header)
        
        print(f"\n{separador}")
        print(header)
        print(separador)
        
        for i in range(self.contador_peliculas):
            if self.peliculas[i] is not None:
                print(f"| {i+1:<3} | {self.peliculas[i].get_informacion()}")
                print(separador)
        
        input("\nPresione enter para continuar...")

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
            print("\n--------------------------------------------")
            print("|     Bienvenido a ¿Qué hay para ver?     |")
            print("--------------------------------------------\n")
            opcion = solicitar_dato("1. Ingresar\n2. Salir\n\nSeleccione una opción: ", "numero", 1, 2)


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
                    print("\n! Error: Usuario no encontrado o contraseña incorrecta.")
                        
    '''
    Autor: Juan David Ortiz Diaz  
    Fecha: 04/05/2026  
    Método menu_crear_sala: Permite registrar una nueva sala de cine solicitando los datos necesarios y validándolos.  
    Parámetros: complejo (objeto que gestiona las salas de cine)  
    Retorna: None  
    '''


    def menu_crear_sala(self):

        print("Registro de Nueva Sala")


        identificador_sala = solicitar_dato("Ingrese el identificador de la sala (1-12): ", "numero", 1, 12)

        valor_boleta = solicitar_dato("Ingrese el valor de la boleta: ", "numero", 1)

        cant_filas = solicitar_dato("Ingrese cantidad de filas: ", "numero", 1)

        sillas_por_fila = solicitar_dato("Ingrese sillas por fila: ", "numero", 1)

        sala_nueva = SalaCine(identificador_sala, valor_boleta, cant_filas, sillas_por_fila)
        
        exito = self.complejo.agregar_sala(sala_nueva)
        
        if exito:
            print("Proceso terminado con éxito.")
        else:
            print("No se pudo realizar el registro.")
            
    '''
    Metodo: agregar_pelicula, recibe los datos de la película a través de entradas del administrador y los asigna a los atributos correspondientes.
    '''
    def agregar_pelicula(self)-> bool:
        
        print("Hola Administrador, vas a agregar una pelicula, por favor ingrese todos los siguientes datos:\n")

        if self.contador_peliculas >= 50:
            print("Error: Capacidad máxima de películas alcanzada.")
            return False

        nombre_espanol = solicitar_dato("Ingrese el nombre en español de la pelicula: ", "texto")
        nombre_original = solicitar_dato("\nIngrese el nombre original de la pelicula: ", "texto")
        
        # Bucle para 
        while True:
            identificador_pelicula = solicitar_dato("\nIngrese el identificador de la pelicula: ", "numero")
            existe = False
            for i in range(self.contador_peliculas):
                if self.peliculas[i] is not None:
                    if self.peliculas[i].get_id() == identificador_pelicula:
                        print("Error: Ya existe una película con ese identificador. Intente con otro.")
                        existe = True
                        break
            
            if not existe:
                break

        anno_estreno = solicitar_dato("\nIngrese el año de estreno de la pelicula: ", "numero")
        duracion = solicitar_dato("\nIngrese la duracion (en minutos) de la pelicula: ", "numero", 90, 180)
        
        gen_opc = solicitar_dato("\nIngrese el genero de la pelicula:\n1) Drama \n2) Suspenso \n3) Terror \n4) Acción \n5) Comedia \n6) Infantil\n", "numero", 1, 6)
        match gen_opc:
            case 1:
                genero = "Drama"
            case 2:
                genero = "Suspenso"
            case 3:
                genero = "Terror"
            case 4:
                genero = "Acción"
            case 5:
                genero = "Comedia"
            case 6:
                genero = "Infantil"

        pais_origen = solicitar_dato("\nIngrese el pais de origen de la pelicula: ", "texto")

        cal_opc = solicitar_dato("\nIngrese la calificacion de la pelicula: \n1) G (General) \n2) PG (Se recomienda la compañía de un adulto) \n3) PG-13 (Se recomienda la compañía de un adulto para menores de 13 años) \n4) R (Prohibida la entrada a menores de 17 años sin compañía de un adulto) \n5) NC-17 (Prohibida la entrada a menores de 18 años sin compañía de un adulto)\n", "numero", 1, 5)
        match cal_opc:
            case 1:
                calificacion = "G"
            case 2:
                calificacion = "PG"
            case 3:
                calificacion = "PG-13"
            case 4:
                calificacion = "R"
            case 5:
                calificacion = "NC-17"


        nueva_pelicula = Pelicula(nombre_espanol, nombre_original, identificador_pelicula, anno_estreno, duracion, genero, pais_origen, calificacion)
        
        self.peliculas[self.contador_peliculas] = nueva_pelicula
        self.contador_peliculas += 1

        print(f"\nPelícula '{nombre_espanol}' agregada exitosamente.")
        return True

obj:SistemaCine

obj = SistemaCine()

obj.login()