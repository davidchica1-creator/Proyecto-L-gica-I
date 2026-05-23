import Reserva
from datetime import datetime, timedelta
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
    Metodo mostrar_lista_peliculas_activas: Muestra una tabla ordenada con la información de unicamente las peliculas activas en el sistema mostrando su informacion de ID,
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

    # ══════════════════════════════════════════════════════════════════
    # HELPER ─ Construye y muestra la tabla de programación semanal
    # Recibe una lista de tuplas (funcion, sala_id, etiqueta_extra)
    # etiqueta_extra permite forzar texto adicional en la celda, 
    # por ejemplo la sala cuando se filtra por película.
    # ══════════════════════════════════════════════════════════════════

    '''
    Autor: Juan David Ortiz / David Chica López
    Fecha: 23/05/2026
    Metodo _construir_tabla_programacion: Helper interno que genera y
    muestra la tabla semanal de franjas horarias dado un iterable de
    funciones. Permite filtrar por sala o película reutilizando lógica.
    Entradas: funciones_con_sala -> lista de tuplas (Funcion, sala_id)
              titulo             -> encabezado que se imprime sobre la tabla
    Salidas:  None
    '''

    def _construir_tabla_programacion(self, funciones_con_sala: list, titulo: str) -> None:

        # 1. Recolectar fechas únicas de las funciones recibidas
        fechas = np.array([], dtype=object)
        for funcion, sala_id in funciones_con_sala:
            fecha = funcion.get_fecha()
            if fecha not in fechas:
                fechas = np.append(fechas, fecha)

        if len(fechas) == 0:
            print("\nNo hay funciones programadas")
            input("\nEnter para continuar...")
            return

        # 2. Fecha más cercana y construcción de la semana
        fecha_menor = datetime.strptime(fechas[0], "%d/%m/%Y")
        for f in fechas:
            fecha_actual = datetime.strptime(f, "%d/%m/%Y")
            if fecha_actual < fecha_menor:
                fecha_menor = fecha_actual

        inicio_semana = fecha_menor - timedelta(days=fecha_menor.weekday())
        fechas_str = np.empty(7, dtype=object)
        for i in range(7):
            dia = inicio_semana + timedelta(days=i)
            fechas_str[i] = dia.strftime("%d/%m/%Y")

        dias_es = np.array(
            ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
            dtype=object
        )

        # 3. Crear franjas de 2 horas entre 08:00 y 00:00
        franjas = np.empty((8, 3), dtype=object)
        fila_idx = 0
        for h in range(8, 24, 2):
            franjas[fila_idx][0] = h * 60
            franjas[fila_idx][1] = (h + 2) * 60
            franjas[fila_idx][2] = f"{h:02d}:00-{(h+2)%24:02d}:00"
            fila_idx += 1

        # 4. Rellenar tabla: cada celda puede acumular varias funciones
        tabla = np.full((8, 7), "", dtype=object)

        for funcion, sala_id in funciones_con_sala:
            fecha_func = funcion.get_fecha()
            hora_func  = funcion.get_hora_inicio()

            if fecha_func not in fechas_str:
                continue

            dia_idx = 0
            for i in range(7):
                if fechas_str[i] == fecha_func:
                    dia_idx = i

            partes = hora_func.split(":")
            minutos_total = int(partes[0]) * 60 + int(partes[1])

            nombre_peli = "SIN NOMBRE"
            for p in self.peliculas:
                if p is not None and p.get_id() == funcion.get_identificador_pelicula():
                    nombre_peli = p.get_nombre_espanol()[:12]

            texto_celda = "S" + str(sala_id) + " " + nombre_peli + " " + hora_func

            for i in range(8):
                if franjas[i][0] <= minutos_total < franjas[i][1]:
                    if tabla[i][dia_idx] == "":
                        tabla[i][dia_idx] = texto_celda
                    else:
                        tabla[i][dia_idx] += "\n" + texto_celda

        # 5. Calcular ancho dinámico de columna según contenido acumulado
        ancho_franja = 12
        ancho_dia    = 23

        for i in range(8):
            for j in range(7):
                if tabla[i][j]:
                    # Cada sub-entrada separada por \n cuenta por separado
                    for entrada in tabla[i][j].split("\n"):
                        if len(entrada) + 2 > ancho_dia:
                            ancho_dia = len(entrada) + 2

        separador = "+" + "-" * ancho_franja
        for _ in range(7):
            separador += "+" + "-" * ancho_dia
        separador += "+"

        # 6. Imprimir tabla
        print(f"\n{titulo}")
        print(separador)

        encabezado = "|" + "FRANJA".center(ancho_franja)
        for i in range(7):
            encabezado += "|" + dias_es[i].center(ancho_dia)
        encabezado += "|"
        print(encabezado)
        print(separador)

        for i in range(8):
            # Dividir cada celda en sus sub-líneas para imprimirlas en filas separadas
            sub_lineas = []
            for j in range(7):
                if tabla[i][j]:
                    sub_lineas.append(tabla[i][j].split("\n"))
                else:
                    sub_lineas.append([""])

            max_sub = 0

            for s in sub_lineas:

                longitud = len(s)

            if longitud > max_sub:

                max_sub = longitud

            for k in range(max_sub):
                if k == 0:
                    fila_txt = "|" + franjas[i][2].center(ancho_franja)
                else:
                    fila_txt = "|" + "".center(ancho_franja)

                for j in range(7):
                    if k < len(sub_lineas[j]):
                        celda = sub_lineas[j][k]
                    else:
                        celda = ""
                    fila_txt += "|" + celda[:ancho_dia].ljust(ancho_dia)
                fila_txt += "|"
                print(fila_txt)

            print(separador)

        input("\nPresione Enter para continuar...")

    # ══════════════════════════════════════════════════════════════════
    # MENÚ DE PROGRAMACIÓN ─ Submenú con 3 opciones
    # ══════════════════════════════════════════════════════════════════

    '''
    Autor: Juan David Ortiz / David Chica López
    Fecha: 23/05/2026
    Metodo menu_programacion: Muestra un submenú para consultar la
    programación general, por sala o por película. Se llama desde los
    menús de admin, vendedor y cliente.
    Entradas: None
    Salidas:  None
    '''

    def menu_programacion(self) -> None:
        while True:
            encabezado = "|         Consultar programación          |"
            separador  = "-" * len(encabezado)
            print(f"\n{separador}")
            print(encabezado)
            print(separador)
            opcion = solicitar_dato(
                "\n1) Programación general\n2) Programación por sala\n3) Programación por película\n4) Volver\n\nSeleccione: ",
                "numero", 1, 4
            )
            if opcion == 4:
                break
            elif opcion == 1:
                self.mostrar_programacion_general()
            elif opcion == 2:
                self.mostrar_programacion_por_sala()
            elif opcion == 3:
                self.mostrar_programacion_por_pelicula()

    # ══════════════════════════════════════════════════════════════════
    # OPCIÓN 1 ─ Programación general (todas las salas, todas las funciones)
    # ══════════════════════════════════════════════════════════════════

    '''
    Autor: Juan David Ortiz
    Fecha: 19/05/2026  (refactorizado 23/05/2026)
    Metodo mostrar_programacion_general: Recopila todas las funciones de
    todas las salas y delega en _construir_tabla_programacion.
    Entradas: None
    Salidas:  None
    '''

    def mostrar_programacion_general(self) -> None:
        funciones_con_sala = []
        for sala in self.complejo.get_lista_salas():
            if sala is not None:
                for funcion in sala.get_programacion():
                    if funcion is not None:
                        funciones_con_sala.append((funcion, sala.get_identificador()))

        self._construir_tabla_programacion(funciones_con_sala, "PROGRAMACION SEMANAL - GENERAL")

    # ══════════════════════════════════════════════════════════════════
    # OPCIÓN 2 ─ Programación por sala
    # ══════════════════════════════════════════════════════════════════

    '''
    Autor: Juan David Ortiz / David Chica López
    Fecha: 23/05/2026
    Metodo mostrar_programacion_por_sala: Lista las salas disponibles,
    pide al usuario que elija una y muestra solo sus funciones en la
    tabla semanal reutilizando _construir_tabla_programacion.
    Entradas: None
    Salidas:  None
    '''

    def mostrar_programacion_por_sala(self) -> None:
        # Listar salas disponibles
        salas_disponibles = []
        for sala in self.complejo.get_lista_salas():
            if sala is not None:
                salas_disponibles.append(sala)

        if len(salas_disponibles) == 0:
            print("\nNo hay salas registradas en el sistema.")
            input("\nEnter para continuar...")
            return

        encabezado = f"| {'#':<3} | {'Sala ID':<15} | {'Valor boleta':<20} | {'Filas':<15} | {'Sillas/Fila':<15} |"
        sep        = "-" * len(encabezado)
        print(f"\n{sep}\n{encabezado}\n{sep}")
        for idx, sala in enumerate(salas_disponibles):
            print(f"| {idx+1:<3} | {sala.mostrar_info()}")
        print(sep)

        num_sala = solicitar_dato("\nSeleccione el número de sala a consultar: ", "numero", 1, len(salas_disponibles))
        sala_elegida = salas_disponibles[num_sala - 1]

        funciones_con_sala = []
        for funcion in sala_elegida.get_programacion():
            if funcion is not None:
                funciones_con_sala.append((funcion, sala_elegida.get_identificador()))

        self._construir_tabla_programacion(
            funciones_con_sala,
            f"PROGRAMACION SEMANAL - SALA {sala_elegida.get_identificador()}"
        )

    # ══════════════════════════════════════════════════════════════════
    # OPCIÓN 3 ─ Programación por película
    # ══════════════════════════════════════════════════════════════════

    '''
    Autor: Juan David Ortiz / David Chica López
    Fecha: 23/05/2026
    Metodo mostrar_programacion_por_pelicula: Muestra la lista de
    películas con funciones programadas, pide al usuario que elija una
    y muestra el horario de esa película en todas las salas donde se
    presenta, indicando la sala en cada celda.
    Entradas: None
    Salidas:  None
    '''

    def mostrar_programacion_por_pelicula(self) -> None:
        # Recopilar películas que tienen al menos una función programada
        ids_con_funcion = set()
        funciones_totales = []  # lista de (funcion, sala_id)

        for sala in self.complejo.get_lista_salas():
            if sala is not None:
                for funcion in sala.get_programacion():
                    if funcion is not None:
                        ids_con_funcion.add(funcion.get_identificador_pelicula())
                        funciones_totales.append((funcion, sala.get_identificador()))

        if len(ids_con_funcion) == 0:
            print("\nNo hay funciones programadas en ninguna sala.")
            input("\nEnter para continuar...")
            return

        # Mostrar lista de películas con funciones
        peliculas_con_funcion = []
        for i in range(self.contador_peliculas):
            p = self.peliculas[i]
            if p is not None and p.get_id() in ids_con_funcion:
                peliculas_con_funcion.append(p)

        encabezado = f"| {'#':<3} | {'ID':<8} | {'Nombre en español':<30} |"
        sep        = "-" * len(encabezado)
        print(f"\n{sep}\n{encabezado}\n{sep}")
        for idx, p in enumerate(peliculas_con_funcion):
            print(f"| {idx+1:<3} | {p.get_id():<8} | {p.get_nombre_espanol():<30} |")
        print(sep)

        num_peli   = solicitar_dato("\nSeleccione el número de película a consultar: ", "numero", 1, len(peliculas_con_funcion))
        peli_elegida = peliculas_con_funcion[num_peli - 1]

        # Filtrar solo las funciones de esa película
        funciones_filtradas = [
            (f, sid) for f, sid in funciones_totales
            if f.get_identificador_pelicula() == peli_elegida.get_id()
        ]

        self._construir_tabla_programacion(
            funciones_filtradas,
            f"PROGRAMACION SEMANAL - {peli_elegida.get_nombre_espanol().upper()}"
        )

    # ══════════════════════════════════════════════════════════════════
    # Mantener compatibilidad: mostrar_programacion_semanal redirige
    # al nuevo menú (por si algún lugar del código aún la invoca)
    # ══════════════════════════════════════════════════════════════════

    def mostrar_programacion_semanal(self, var: int) -> None:
        if var == 1:
            self.mostrar_programacion_general()
        elif var == 2:
            self.mostrar_programacion_por_sala()
        elif var == 3:
            self.mostrar_programacion_por_pelicula()
        else:
            print("Opción incorrecta")
            

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


    def reservar_boleta(self, usuario, sala, identificador_funcion, identificador_sala, cant_boletas, fila, columna_inicial, precio_total = 0) -> bool:
        
        if usuario is None:
            print("Usuario no encontrado.")
            return False
        
        if sala is None:
            print("Sala no encontrada.")
            return False
        
<<<<<<< HEAD
=======
        funcion = None
        for i in sala.get_programacion():
            if i is not None:
                print(f"ID funcion: {i.get_identificador_funcion()}")
                if i.get_identificador_funcion() == identificador_funcion:
                    funcion = i
                    break
               
            
            
        
        if funcion is None:
            print("Función no encontrada.")
            return False
        mapa = funcion.get_mapa_sala()
        
>>>>>>> 09611155dfe6d0da1dd163da9b59c7a78e3782ab
        print("\n-------------------------------------------------")
        print("        Vas a realizar una reserva de boletas          ")
        print("-------------------------------------------------\n")
        
<<<<<<< HEAD
        funcion = sala.get_programacion()[identificador_funcion - 1]

        if funcion is None:
            print("Función no encontrada.")
            return False

        mapa = funcion.get_mapa_sala()
=======
        if columna_inicial + cant_boletas > mapa.shape[1]:
            print("Las columnas seleccionadas se salen del rango de la sala.")
            return False
>>>>>>> 09611155dfe6d0da1dd163da9b59c7a78e3782ab
        
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

<<<<<<< HEAD

obj:SistemaCine
obj = SistemaCine()
obj.login()

=======
    def emitir_boleta(self, usuario, sala, identificador_funcion) -> None:
        pass
        
>>>>>>> 09611155dfe6d0da1dd163da9b59c7a78e3782ab
if __name__ == "__main__":
    obj:SistemaCine
    obj = SistemaCine()
    obj.login()
