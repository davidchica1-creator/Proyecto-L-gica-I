import Reserva
from Usuario import*
from funciones_utiles import solicitar_dato, limpiar_pantalla
from SalasCine import*
from Pelicula import*
from Complejo import Complejo  

'''
Autor: Juan David Ortiz Diaz  
Fecha: 04/05/2026
Clase SistemaCine: Representa un sistema de cine
'''

class SistemaCine:

    '''
    Autor: Juan David Ortiz Diaz  
    Fecha: 04/05/2026  
    Método constructor de la clase SistemaCine  
    Parámetros: Ninguno  
    Salidas: None  
    '''

    def __init__(self):
        self.usuarios:np.ndarray = np.full((100), fill_value = None, dtype = object)
        self.contador_clientes:int =0

        self.peliculas:np.ndarray = np.full((50), fill_value = None, dtype = object)
        self.contador_peliculas:int=0

        self.complejo:Complejo = Complejo()
        self.contador_salas:int = 0

    '''
    Autor: Juan David Ortiz Diaz
    Fecha: 04/05/2026  
    Método crear_cliente: Permite registrar un nuevo cliente en el sistema validando que no exista previamente.  
    Parámetros: Ninguno  
    Salidas: bool (True si se crea correctamente, False si falla)  
    '''

    def crear_cliente(self) -> bool:
        encabezado = "|         Registro de nuevo cliente          |"
        separador = "-" * len(encabezado)
        print(f"\n{separador}")
        print(encabezado)
        print(separador)

        self.__nombre = solicitar_dato("\nIngrese el nombre completo del cliente: ", "texto")
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
    Autor: David Chica López  
    Fecha: 14/05/2026  
    Metodo mostrar_lista_peliculas: Muestra una tabla ordenada con la informacion de las peliculas registradas en el sistema mostrando su informacion de ID, nombre en español
    nombre original, año de estreno, duracion, genero, pais de origen, calificacion y estado.  
    Entradas: Ninguno  
    Salidas: None  
    '''

    def mostrar_lista_peliculas(self) -> None:
        if self.contador_peliculas == 0:
            print("No hay películas registradas en el sistema.")
            return
        
        header = f"| {'#':<3} | {'ID Peli':<10} | {'Nombre en español':<25} | {'Nombre original':<20} | {'Año de estreno':<15} | {'Duración':<10} | {'Género':<12} | {'Pais de origen':<15} | {'Calificación':<12} | {'Estado':<10} |"
        separador = "-" * len(header)
        
        print(f"\n{separador}")
        print(header)
        print(separador)
        
        for i in range(self.contador_peliculas):
            if self.peliculas[i] is not None:
                print(f"| {i+1:<3} | {self.peliculas[i].get_informacion()}")
                print(separador)
        
        entrada = input("\nPresione enter para continuar...")

        if entrada == "":
            pass
    
    '''
    Autor: David Chica López  
    Fecha: 14/05/2026  
    Metodo mostrar_lista_peliculas_activas: Muestra una tabla ordenada con la información de unicamente las pleiculas activas en el sistema mostrando su informacion de ID,
    nombre en español, año de estreno, duración( en minutos ), genero, pais de origen, calificacion y estado ( que unicamente sera activo ).  
    Entradas: Ninguno  
    Salidas: None  
    '''

    def mostrar_lista_peliculas_activas(self) -> None:
        if self.contador_peliculas == 0:
            print("No hay películas registradas en el sistema.")
            return
        
        encabezado = f"| {'#':<3} | {'ID Peli':<10} | {'Nombre en español':<25} | {'Nombre original':<20} | {'Año de estreno':<15} | {'Duracion':<10} | {'Genero':<12} | {'Pais de origen':<15} | {'Calificacion':<12} | {'Estado':<10} |"
        separador = "-" * len(encabezado)
        
        print(f"\n{separador}")
        print(encabezado)
        print(separador)

        numeral_visual = 1
        for i in range(self.contador_peliculas):
            if self.peliculas[i] is not None and self.peliculas[i].get_estado() is True:
                print(f"| {numeral_visual:<3} | {self.peliculas[i].get_informacion()}")
                print(separador)
                numeral_visual += 1
                
        entradad = input("\nPresione enter para continuar...")

        if entradad == "":
            pass



    '''
    Autor: Juan David Ortiz Diaz  
    Fecha: 04/05/2026  
    Método login: Gestiona el inicio de sesión de usuarios (admin, vendedor o cliente) y redirige al menú correspondiente.  
    Entradas: Ninguno  
    Salidas: None  
    '''

    def login(self)->None:
        opcion:int
        user:Usuario
        usuario_ingresado:str
        contrasena:str
        while True:
            limpiar_pantalla()
            encabezado = "|         Bienvenido a que hay para ver!          |"
            separador = "-" * len(encabezado)
            print(f"\n{separador}")
            print(encabezado)
            print(separador)
            
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
                    user = self.usuarios[i]
                    if str(user.get_usuario()) == usuario_ingresado and user.get_contrasena() == contrasena:
                        user.menu_cliente(self)
                        encontrado = True
                        break
                if not encontrado:
                    print("\n ==Error: Usuario no encontrado o contraseña incorrecta==")
                        
    '''
    Autor: Juan David Ortiz Diaz  
    Fecha: 04/05/2026  
    Método menu_crear_sala: Permite registrar una nueva sala de cine solicitando los datos necesarios y validándolos.  
    Entradas: complejo (objeto que gestiona las salas de cine)  
    Salidas: None  
    '''


    def menu_crear_sala(self)->str:

        encabezado = "|         Registro de nueva sala          |"
        separador = "-" * len(encabezado)
        print(f"\n{separador}")
        print(encabezado)
        print(separador)

        if self.contador_salas == 12:
            return "Se ha alcanzado el máximo de salas permitidas por el sistema."
            
        else: 

            while True:
                identificador_sala = solicitar_dato("Ingrese el identificador de la sala (1-12): ", "numero", 1, 12)
                existe = False
                for sala in self.complejo.get_lista_salas():
                    if sala is not None and sala.get_identificador() == identificador_sala:
                        print(f"Error: Ya existe una sala con el identificador {identificador_sala}. Intente con otro.")
                        existe = True
                        break
                
                if not existe:
                    break

            valor_boleta = solicitar_dato("Ingrese el valor de la boleta: ", "numero", 1)

            cant_filas = solicitar_dato("Ingrese cantidad de filas (máximo 26): ", "numero", 1, 26)

            sillas_por_fila = solicitar_dato("Ingrese sillas por fila: ", "numero", 1)

            sala_nueva = SalaCine(identificador_sala, valor_boleta, cant_filas, sillas_por_fila)
            self.contador_salas += 1
            exito = self.complejo.agregar_sala(sala_nueva)
            
            if exito:
                print("\nProceso terminado con éxito.")
            else:
                print("No se pudo realizar el registro.")
    
    '''
    Autor: David Chica lopez
    Fecha: 10/05/2026
    Metodo agregar_pelicula: Permite agregar una pelicula a la lista de peliculas
    Entradas: None
    Salidas: Cadena de texto que confirma que la pelicula fue creada con exito
    '''

    def agregar_pelicula(self)-> str:

        encabezado = "|         Registro de nueva pelicula          |"
        separador = "-" * len(encabezado)
        print(f"\n{separador}")
        print(encabezado)
        print(separador)

        if self.contador_peliculas >= 50:
            
            print("Error: Capacidad máxima de películas alcanzada")

        nombre_espanol = solicitar_dato("Ingrese el nombre en español de la pelicula: ", "texto")
        nombre_original = solicitar_dato("\nIngrese el nombre original de la pelicula: ", "texto")
        
        
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
        
        gen_opc = solicitar_dato("\n---Generos de la pelicula---\n\n1) Drama \n2) Suspenso \n3) Terror \n4) Acción \n5) Comedia \n6) Infantil\n\nIngrese una opcion: ", "numero", 1, 6)
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

        cal_opc = solicitar_dato("\n---Tipos de calificacion de la pelicula---\n\n1) G      (General) \n2) PG     (Se recomienda la compañía de un adulto) \n3) PG-13  (Se recomienda la compañía de un adulto para menores de 13 años) \n4) R      (Prohibida la entrada a menores de 17 años sin compañía de un adulto) \n5) NC-17  (Prohibida la entrada a menores de 18 años sin compañía de un adulto)\n\nIngrese una opcion: ", "numero", 1, 5)
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


    def reservar_boleta(self, usuario,sala, identificador_funcion, identificador_sala, cant_boletas, fila, columna_inicial, precio_total = 0) -> bool:
        
        if usuario is None:
            print("Usuario no encontrado.")
            return False
        
        if sala is None:
            print("Sala no encontrada.")
            return False
        
        if mapa is None:
            print("Función no encontrada.")
            return False
        
        print("\n-------------------------------------------------")
        print("        Vas a realizar una reserva de boletas          ")
        print("-------------------------------------------------\n")
        
        funcion = sala.get_programacion()[identificador_funcion - 1]
        mapa = funcion.get_mapa_sala()
        
        for i in range(cant_boletas):
            asiento_disponible = mapa[fila, columna_inicial + i] 
            if asiento_disponible != 0:
                print("Los asientos seleccionados no están libres, seleccione de nuevo.")
                return False
            
        for i in range(cant_boletas):
            mapa[fila, columna_inicial + i] = 1
            
        funcion.agregar_asientos_reservados(cant_boletas)
        print("Su reserva ha sido guardada con éxito.")
        return True
    
    def get_usuario_por_documento(self, documento):
        for i in range(self.contador_clientes):
            if self.usuarios[i] is not None:
                if self.usuarios[i].get_usuario() == documento:
                    return self.usuarios[i]
        return None

obj:SistemaCine

obj = SistemaCine()

obj.login()

if __name__ == "__main__":
    obj:SistemaCine
    obj = SistemaCine()
    obj.login()

