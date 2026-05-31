import numpy as np
from Reserva import *
from datetime import datetime, timedelta
from Usuario import*
from funciones_utiles import solicitar_dato, limpiar_pantalla, ordenar_por_burbuja
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
        self.ARCHIVO_USUARIOS = "usuarios.npy"
        self.ARCHIVO_PELICULAS = "peliculas.npy"
        self.ARCHIVO_COMPLEJO = "complejo.npy"
        self.MAX_USUARIOS = 100
        self.MAX_PELICULAS = 50

        self.usuarios, self.contador_clientes = self.cargar_datos(self.ARCHIVO_USUARIOS, self.MAX_USUARIOS)

        if self.contador_clientes == 0:
            self.usuarios[0] = Usuario("Admin123", "Admin123*", 1)
            self.usuarios[1] = Usuario("Vendedor123", "Vendedor123*", 2)
            self.contador_clientes = 1

        self.peliculas, self.contador_peliculas = self.cargar_datos(self.ARCHIVO_PELICULAS, self.MAX_PELICULAS)

        try:
            temp_complejo = np.load(self.ARCHIVO_COMPLEJO, allow_pickle=True)
            self.complejo = temp_complejo[0]
            self.contador_salas = self.complejo.get_cantidad_salas()
        except:
            self.complejo = Complejo()
            self.contador_salas = 0

    '''
    ============================================================================================================================================================================
    ESTE BLOQUE DE CODIGO CUMPLE CON EL REQUERIMIENTO 1, R1. INGRESAR USUARIO
    '''
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
            contrasena = input("Ingrese la contraseña: ")

            if usuario_ingresado == "Admin123" and contrasena == "Admin123*":
                user = Usuario("Admin", 123, 1)
                user.menu_admin(self)
            elif usuario_ingresado == "Vendedor123" and contrasena == "Vendedor123*":
                user = Usuario("Vendedor", 123, 2)
                user.menu_vendedor(self)
            else:

                user = self.get_usuario_por_documento(usuario_ingresado)
                if user and user.get_contrasena() == contrasena:
                    user.menu_cliente(self)
                    encontrado = True
                else:
                    encontrado = False
                
                if not encontrado:
                    print("\n ==Error: Usuario no encontrado o contraseña incorrecta==")

    '''
    ============================================================================================================================================================================
    '''

    '''
    ============================================================================================================================================================================
    ESTE BLOQUE DE CODIGO CUMPLE CON EL REQUERIMIENTO 2, R2. CREAR CLIENTE
    
    '''

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

        nombre = solicitar_dato("\nIngrese el nombre completo del cliente: ", "texto")
        documento = solicitar_dato("Ingrese el usuario (documento) del cliente: ", "numero")
        contrasena_gen = (f"{documento}{nombre[0].lower()}*")
        
        if self.contador_clientes >= 100 :
            print ("Se ha alcanzado el máximo de usuarios permitidos por el sistema.")
            return False
        
        if self.get_usuario_por_documento(documento):
            print("El usuario ya existe")
            return False

        nuevo = Usuario(nombre, documento, 3)

        self.usuarios[self.contador_clientes] = nuevo
        self.contador_clientes += 1

        print("\nCliente creado con éxito\n")
        print("Las credenciales del nuevo cliente son:\n")
        print("Usuario:", documento)
        print("Contraseña:", contrasena_gen)
        self.guardar_todo()

        return True
    
    '''
    ============================================================================================================================================================================
    '''

    '''
    ============================================================================================================================================================================
    ESTE BLOQUE DE CODIGO CUMPLE CON EL REQUERIMIENTO 3, R3. CONSULTAR PROGRAMACION DE CADA SALA DE CINE O DEL COMPLEJO COMPLETO
    '''
    
    '''
    Autor: Juan David Ortiz / David Chica López
    Fecha: 23/05/2026
    Metodo construir_tabla_programacion: Helper interno que genera y
    muestra la tabla semanal de franjas horarias dado un iterable de
    funciones. Permite filtrar por sala o película reutilizando lógica.
    Entradas: funciones_con_sala -> lista de tuplas (Funcion, sala_id)
              titulo             -> encabezado que se imprime sobre la tabla
    Salidas:  None
    '''

    def construir_tabla_programacion(self, funciones_con_sala: np.ndarray, titulo: str) -> None:

        hoy = datetime.now()
        inicio_semana = hoy - timedelta(days=hoy.weekday())
        inicio_semana = inicio_semana.replace(hour=0, minute=0, second=0, microsecond=0)

        fechas_str = np.empty(7, dtype=object)
        for i in range(7):
            dia = inicio_semana + timedelta(days=i)
            fechas_str[i] = dia.strftime("%d/%m/%Y")

        dias_es = np.array(["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"], dtype=object)

        franjas = np.empty((8, 3), dtype=object)
        fila_idx = 0
        for h in range(8, 24, 2):
            franjas[fila_idx][0] = h * 60
            franjas[fila_idx][1] = (h + 2) * 60
            franjas[fila_idx][2] = f"{h:02d}:00-{(h+2)%24:02d}:00"
            fila_idx += 1

        tabla = np.full((8, 7), "", dtype=object)

        for item in funciones_con_sala:
            if item is None:
                continue
            funcion, sala_id = item
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

        ancho_franja = 12
        ancho_dia    = 23

        for i in range(8):
            for j in range(7):
                if tabla[i][j]:
                    for entrada in tabla[i][j].split("\n"):
                        if len(entrada) + 2 > ancho_dia:
                            ancho_dia = len(entrada) + 2

        separador = "+" + "-" * ancho_franja
        for _ in range(7):
            separador += "+" + "-" * ancho_dia
        separador += "+"

        print(f"\n{titulo}")
        print(separador)

        encabezado = "|" + "FRANJA".center(ancho_franja)
        for i in range(7):
            fecha_obj = datetime.strptime(fechas_str[i], "%d/%m/%Y")
            txt_dia = f"{dias_es[i]} ({fecha_obj.day})"
            encabezado += "|" + txt_dia.center(ancho_dia)
        encabezado += "|"
        print(encabezado)
        print(separador)

        for i in range(8):

            sub_lineas = np.full((7,), fill_value=None, dtype=object)
            for j in range(7):
                if tabla[i][j]:
                    sub_lineas[j] = tabla[i][j].split("\n")
                else:
                    sub_lineas[j] = np.array([""], dtype=object)

            max_sub = 0
            for s in sub_lineas:
                if s is not None:
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


    '''
    Autor: Juan David Ortiz
    Fecha: 19/05/2026  (refactorizado 23/05/2026)
    Metodo mostrar_programacion_general: Recopila todas las funciones de
    todas las salas y delega en construir_tabla_programacion.
    Entradas: None
    Salidas:  None
    '''

    def mostrar_programacion_general(self) -> None:
        funciones_con_sala = np.full((60,), fill_value=None, dtype=object)
        idx = 0
        lista_salas = self.complejo.get_lista_salas()
        for i in range(len(lista_salas)):
            if lista_salas[i] is not None:
                prog = lista_salas[i].get_programacion()
                for j in range(len(prog)):
                    if prog[j] is not None:
                        funciones_con_sala[idx] = (prog[j], lista_salas[i].get_identificador())
                        idx += 1

        self.construir_tabla_programacion(funciones_con_sala, "PROGRAMACION SEMANAL - GENERAL")


    '''
    Autor: Juan David Ortiz / David Chica López
    Fecha: 23/05/2026
    Metodo mostrar_programacion_por_sala: Lista las salas disponibles,
    pide al usuario que elija una y muestra solo sus funciones en la
    tabla semanal reutilizando construir_tabla_programacion.
    Entradas: None
    Salidas:  None
    '''

    def mostrar_programacion_por_sala(self) -> None:
        salas_disponibles = np.full((12,), fill_value=None, dtype=object)
        contador = 0
        lista_salas = self.complejo.get_lista_salas()
        for i in range(len(lista_salas)):
            if lista_salas[i] is not None:
                salas_disponibles[contador] = lista_salas[i]
                contador += 1

        if contador == 0:
            print("\nNo hay salas registradas en el sistema.")
            input("\nEnter para continuar...")
            return

        encabezado = f"| {'#':<3} | {'Sala ID':<15} | {'Valor boleta':<20} | {'Filas':<15} | {'Sillas/Fila':<15} |"
        sep        = "-" * len(encabezado)
        print(f"\n{sep}\n{encabezado}\n{sep}")
        for i in range(contador):
            print(f"| {i+1:<3} | {salas_disponibles[i].mostrar_info()}")
        print(sep)

        num_sala = solicitar_dato("\nSeleccione el número de sala a consultar: ", "numero", 1, contador)
        sala_elegida = salas_disponibles[num_sala - 1]

        funciones_con_sala = np.full((5,), fill_value=None, dtype=object)
        prog_sala = sala_elegida.get_programacion()
        idx_f = 0
        for i in range(len(prog_sala)):
            if prog_sala[i] is not None:
                funciones_con_sala[idx_f] = (prog_sala[i], sala_elegida.get_identificador())
                idx_f += 1

        self.construir_tabla_programacion(
            funciones_con_sala,
            f"PROGRAMACION SEMANAL - SALA {sala_elegida.get_identificador()}"
        )


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
        ids_con_funcion = np.full((50,), fill_value=-1, dtype=int)
        funciones_totales = np.full((60,), fill_value=None, dtype=object)
        idx_ids = 0
        idx_func = 0

        lista_salas = self.complejo.get_lista_salas()
        for i in range(len(lista_salas)):
            if lista_salas[i] is not None:
                prog = lista_salas[i].get_programacion()
                for j in range(len(prog)):
                    if prog[j] is not None:
                        ids_con_funcion[idx_ids] = prog[j].get_identificador_pelicula()
                        funciones_totales[idx_func] = (prog[j], lista_salas[i].get_identificador())
                        idx_ids += 1
                        idx_func += 1

        if idx_ids == 0:
            print("\nNo hay funciones programadas en ninguna sala.")
            input("\nEnter para continuar...")
            return

        peliculas_con_funcion = np.full((self.MAX_PELICULAS), fill_value=None, dtype=object)
        contador_peli_prog = 0
        for i in range(self.contador_peliculas):
            p = self.peliculas[i]
            if p is not None and p.get_id() in ids_con_funcion:
                peliculas_con_funcion[contador_peli_prog] = p
                contador_peli_prog += 1

        encabezado = f"| {'#':<3} | {'ID':<8} | {'Nombre en español':<30} |"
        sep        = "-" * len(encabezado)
        print(f"\n{sep}\n{encabezado}\n{sep}")
        for i in range(contador_peli_prog):
            p = peliculas_con_funcion[i]
            print(f"| {i+1:<3} | {p.get_id():<8} | {p.get_nombre_espanol():<30} |")
        print(sep)

        num_peli   = solicitar_dato("\nSeleccione el número de película a consultar: ", "numero", 1, contador_peli_prog)
        peli_elegida = peliculas_con_funcion[num_peli - 1]

        funciones_filtradas = np.full((60), fill_value=None, dtype=object)
        contador_filtradas = 0
        for i in range(len(funciones_totales)):
            item = funciones_totales[i]
            if item is not None and item[0].get_identificador_pelicula() == peli_elegida.get_id():
                funciones_filtradas[contador_filtradas] = item
                contador_filtradas += 1

        self.construir_tabla_programacion(
            funciones_filtradas,
            f"PROGRAMACION SEMANAL - {peli_elegida.get_nombre_espanol().upper()}"
        )


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
    ============================================================================================================================================================================
    '''

    '''
    ============================================================================================================================================================================
    ESTE BLOQUE DE CODIGO CUMPLE CON EL REQUERIMIENTO 4, R4. CONSULTAR POR LA INFORMACION DE UNA PELICULA
    '''

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
    
    '''
    ============================================================================================================================================================================
    '''

    '''
    ============================================================================================================================================================================
    ESTE BLOQUE DE CODIGO CUMPLE CON EL REQUERIMIENTO 5, R5. VISUALIZAR MAPA DE SALA QUE DESEA RESERVAR
    '''

    '''
    Autor: Salomé García Velásquez / David Chica Lopez
    Fecha: 23/05/2026
    Metodo mostrar_mapa_funcion: Permite al usuario seleccionar una sala y una función 
    para visualizar el mapa de asientos.
    Entradas: None
    Salidas: None
    '''
    def mostrar_mapa_funcion(self) -> None:
        
        lista_de_salas = self.complejo.get_lista_salas()
        
        if self.complejo.get_cantidad_salas() == 0:
            print("\nNo hay salas registradas en el sistema.")
            input("\nPresione Enter para continuar...")
            return

        print("\n--- Selección de Sala ---")
        for i in range(len(lista_de_salas)):
            if lista_de_salas[i] is not None:
                print(f"{i+1}) Sala {lista_de_salas[i].get_identificador()}")
        
        cantidad_salas = self.complejo.get_cantidad_salas()
        indice_sala = solicitar_dato("\nSeleccione el número de la sala: ", "numero", 1, cantidad_salas)
        sala_seleccionada = lista_de_salas[indice_sala - 1]

        programacion_sala = sala_seleccionada.get_programacion()
        
        funciones_validas = np.full((5,), fill_value=None, dtype=object)
        contador_f = 0
        for j in range(len(programacion_sala)):
            if programacion_sala[j] is not None:
                funciones_validas[contador_f] = programacion_sala[j]
                contador_f += 1

        if contador_f == 0:
            print(f"\nLa sala {sala_seleccionada.get_identificador()} no tiene funciones programadas.")
            input("\nPresione Enter para continuar...")
        else:
            print(f"\n--- Funciones disponibles en Sala {sala_seleccionada.get_identificador()} ---")
            for k in range(contador_f):
                funcion_actual = funciones_validas[k]
                
                nombre_peli = "Desconocida"
                for peli in self.peliculas:
                    if peli is not None and peli.get_id() == funcion_actual.get_identificador_pelicula():
                        nombre_peli = peli.get_nombre_espanol()
                        break
                
                print(f"{k+1}) {nombre_peli} - {funcion_actual.get_fecha()} a las {funcion_actual.get_hora_inicio()}")

            indice_f = solicitar_dato("\nSeleccione el número de la función para ver el mapa: ", "numero", 1, contador_f)
            funcion_elegida = funciones_validas[indice_f - 1]
            
            limpiar_pantalla()
            print(f"\nSALA: {sala_seleccionada.get_identificador()} | HORA: {funcion_elegida.get_hora_inicio()}")
            funcion_elegida.mostrar_mapa()
            
            input("\nPresione Enter para volver...")

    '''
    ============================================================================================================================================================================
    '''
    
    '''
    ============================================================================================================================================================================
    ESTE BLOQUE DE CODIGO CUMPLE CON EL REQUERIMIENTO 6, R6. RESERVAR BOLETAS PARA UNA PELÍCULA
    '''

    '''
    Autor: salomé García Velásquez / David Chica López
    Fecha: 20/05/2026
    Metodo reservar_boleta: Gestiona el proceso completo de reserva de boletas.
    Identifica si es vendedor o cliente, valida existencia del cliente,
    permite seleccionar sala, función y asientos, y crea el objeto Reserva.
    Entradas: usuario_sesion (el usuario que está realizando la operación)
    Salidas: bool (True si se realizó con éxito, False en caso contrario)
    '''

    def reservar_boleta(self, usuario_sesion: Usuario) -> bool:
        limpiar_pantalla()
        encabezado = "|         Registro de nueva reserva          |"
        separador = "-" * len(encabezado)
        print(f"\n{separador}")
        print(encabezado)
        print(separador)

        cliente_final = None
        if usuario_sesion.get_tipo_usuario() == 2: 
            documento = solicitar_dato("\nIngrese el número de documento del cliente: ", "numero")
            cliente_final = self.get_usuario_por_documento(documento)
            if cliente_final is None:
                print(f"\nError: El cliente con documento {documento} no existe en el sistema.")
                print("Debe registrarlo primero antes de realizar una reserva.")
                input("\nPresione Enter para continuar...")
                return False
        else:
            cliente_final = usuario_sesion
            print(f"Usuario encontrado, nombre de usuario: {cliente_final.get_nombre()}")

        if self.complejo.get_cantidad_salas() == 0:
            print("\nNo hay salas registradas en el sistema.")
            input("\nPresione Enter para continuar...")
            return False
            
        print("\nSalas disponibles:")
        salas = self.complejo.get_lista_salas()
        enc_s = f"| {'#':<3} | {'Sala ID':<15} | {'Valor boleta':<20} |"
        sep_s = "-" * len(enc_s)
        print(f"{sep_s}\n{enc_s}\n{sep_s}")
        for i in range(len(salas)):
            if salas[i] is not None:
                print(f"| {i+1:<3} | S{salas[i].get_identificador():<14} | {salas[i].get_valor_boleta():<20} |")
        print(sep_s)

        num_sala = solicitar_dato("\nSeleccione el número de la sala: ", "numero", 1, self.complejo.get_cantidad_salas())
        sala_seleccionada = salas[num_sala - 1]

        if sala_seleccionada.get_cant_funciones() == 0:
            print(f"\nLa sala {sala_seleccionada.get_identificador()} no tiene funciones programadas.")
            input("\nPresione Enter para continuar...")
            return False

        print(f"\nFunciones disponibles en Sala {sala_seleccionada.get_identificador()}:")
        programacion = sala_seleccionada.get_programacion()
        funciones_validas = np.full((5,), fill_value=None, dtype=object)
        contador_fv = 0
        for i in range(len(programacion)):
            if programacion[i] is not None:
                funciones_validas[contador_fv] = programacion[i]
                contador_fv += 1

        enc_f = f"| {'#':<3} | {'ID Función':<12} | {'Fecha':<12} | {'Hora':<10} |"
        sep_f = "-" * len(enc_f)
        print(f"{sep_f}\n{enc_f}\n{sep_f}")
        for i in range(contador_fv):
            f = funciones_validas[i]
            print(f"| {i+1:<3} | {f.get_id_funcion():<12} | {f.get_fecha():<12} | {f.get_hora_inicio():<10} |")
        print(sep_f)

        num_func = solicitar_dato("\nSeleccione el número de la función: ", "numero", 1, contador_fv)
        funcion_elegida = funciones_validas[num_func - 1]

        print("\nEstado actual de los asientos ( . = libre, X = ocupado ):")
        funcion_elegida.mostrar_mapa()

        cant_boletas = solicitar_dato("\nIngrese la cantidad de boletas a reservar: ", "numero", 1, sala_seleccionada.get_sillas_por_fila())
        
        while True:
            fila_letra = solicitar_dato("Ingrese la letra de la fila (ej: A): ", "letra").upper()
            letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            idx_fila = letras.find(fila_letra)
            if idx_fila != -1 and idx_fila < sala_seleccionada.get_cant_filas():
                break
            print(f"Error: La fila '{fila_letra}' no existe en esta sala.")
        
        col_inicio = solicitar_dato(f"Ingrese el número de la silla inicial (1-{sala_seleccionada.get_sillas_por_fila()}): ", "numero", 1, sala_seleccionada.get_sillas_por_fila()) - 1

        if col_inicio + cant_boletas > sala_seleccionada.get_sillas_por_fila():
            print("\nError: No hay suficientes sillas consecutivas en esa fila.")
            input("Presione Enter para volver...")
            return False

        mapa = funcion_elegida.get_mapa_sala()
        for i in range(cant_boletas):
            if mapa[idx_fila, col_inicio + i] != 0:
                print("\nError: Uno o más asientos seleccionados ya están ocupados.")
                input("Presione Enter para volver...")
                return False

        asientos_ids = np.full((cant_boletas,), fill_value="", dtype=object)
        for i in range(cant_boletas):
            mapa[idx_fila, col_inicio + i] = 1
            asientos_ids[i] = f"{'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[idx_fila]}{col_inicio + i + 1}"
            
        precio_total = cant_boletas * sala_seleccionada.get_valor_boleta()
        
        funcion_elegida.agregar_asientos_reservados(cant_boletas)
        
        reserva_nueva = Reserva(cliente_final.get_usuario(), funcion_elegida.get_id_funcion(), sala_seleccionada.get_identificador(), cant_boletas, asientos_ids, precio_total)
        self.complejo.agregar_reserva(reserva_nueva)

        print("\nSu reserva ha sido guardada con éxito.")
        self.emitir_boleta(reserva_nueva)
        self.guardar_todo()
        input("\nPresione Enter para continuar...")
        return True

    '''
    ============================================================================================================================================================================
    '''

    '''
    ============================================================================================================================================================================
    ESTE BLOQUE DE CODIGO CUMPLE CON EL REQUERIMIENTO 7, R7. GESTIONAR PROGRAMCION DE LAS PELICULAS
    '''

    '''
    Autor: David Chica López
    Fecha: 23/05/2026
    Metodo gestionar_programacion: Permite la administración de funciones por sala.
    Entradas: None
    Salidas: None
    '''
    def gestionar_programacion(self) -> None:

        if self.complejo.get_cantidad_salas() == 0 or self.contador_peliculas == 0:
            print("No hay salas registradas para programar funciones o no hay películas registradas.")
            return
        
        limpiar_pantalla()
        encabezado = "|         Gestión de Programación de Funciones          |"
        separador = "-" * len(encabezado)
        print(f"\n{separador}")
        print(encabezado)
        print(separador)

        print("\nSalas disponibles:")
        encabezado_salas = f"| {'#':<3} | {'Sala ID':<15} | {'Valor boleta':<20} | {'Filas':<15} | {'Sillas/Fila':<15} |"
        sep_salas = "-" * len(encabezado_salas)
        
        print(f"\n{sep_salas}\n{encabezado_salas}\n{sep_salas}")
        
        lista_salas = self.complejo.get_lista_salas()
        for i in range(len(lista_salas)):
            if lista_salas[i] is not None:
                print(f"| {i+1:<3} |{lista_salas[i].mostrar_info()}")
        print(sep_salas)

        cant_salas = self.complejo.get_cantidad_salas()
        idx_sala = solicitar_dato("\nSeleccione una sala para gestionar: ", "numero", 1, cant_salas) - 1
        sala_seleccionada = lista_salas[idx_sala]

        print(f"\nTrabajando en Sala: {sala_seleccionada.get_identificador()}")
        print("\n\t1) Crear función\n\t2) Modificar función\n\t3) Renovar programación general\n\t4) Salir\n")
        
        opcion = solicitar_dato("Seleccione una opción: ", "numero", 1, 4)

        match opcion:
            case 1:
                self.complejo.crear_funcion(self, sala_seleccionada)
                self.guardar_todo()
            case 2:
                self.complejo.modificar_funcion(self, sala_seleccionada)
                self.guardar_todo()
            case 3:
                confirmacion_admin = solicitar_dato("¿Está seguro? Esto eliminará todas las funciones del sistema (si/no): ", "si_no")
                if confirmacion_admin == "si":
                    self.complejo.renovar_programacion_semanal()
                    self.guardar_todo()
            case 4:
                return

    '''
    ============================================================================================================================================================================
    '''
    
    '''
    ============================================================================================================================================================================
    ESTE BLOQUE DE CODIGO CUMPLE CON EL REQUERIMIENTO 8, R8. EMITIR BOLETA
    '''

    '''
    Autor: Salome García Velásquez / David Chica López
    Fecha: 23/05/2026
    Metodo emitir_boleta: Muestra en pantalla la informacion de la boleta con los datos de la reserva. Fecha de venta(mismo dia de la funcion), hora, nombre del complejo, 
    sala de funcion, nombre de la pelicula, calificacion de la pelicula, precio total, lista de sillas reservadas 
    Entradas: Reserva
    Salidas: None
    '''
    def emitir_boleta(self, reserva: Reserva) -> None:

        print("\nGenerando boleta de reserva...")
        input("\nPresione Enter para ver la boleta...")

        usuario = self.get_usuario_por_documento(reserva.get_usuario())
        nombre_cliente = usuario.get_nombre() if usuario else "Desconocido"

        nombre_peli, calif_peli = "No encontrada", "N/A"
        fecha_func, hora_func = "N/A", "N/A"
        
        id_sala = reserva.get_sala()
        sala = self.complejo.get_sala(id_sala)
        
        if sala is not None:
            for funcion in sala.get_programacion():
                if funcion is not None and funcion.get_id_funcion() == reserva.get_id_funcion():
                    fecha_func = funcion.get_fecha()
                    hora_func = funcion.get_hora_inicio()
                    
                    for peli in self.peliculas:
                        if peli is not None and peli.get_id() == funcion.get_identificador_pelicula():
                            nombre_peli = peli.get_nombre_espanol()
                            calif_peli = peli.get_calificacion()
                            break
                    break

        asientos_str = ", ".join(map(str, reserva.get_asientos()))

        lineas = [
            f" Cliente: {nombre_cliente}",
            f" Película: {nombre_peli}",
            f" Fecha Funcion: {fecha_func}",
            f" Hora Funcion: {hora_func}",
            f" Sala: {id_sala}",
            f" Calificación: {calif_peli}",
            f" Precio Total: ${reserva.get_precio_total():,}",
            f" Fecha Venta: {reserva.get_fecha_venta()}",
            f" Asientos: {asientos_str}"
        ]

        titulo = "BOLETA DE RESERVA"
        ancho_total = max(max(len(l) for l in lineas), len(titulo)) + 4
        separador = "-" * ancho_total

        print(f"\n{separador}")
        print(f"|{titulo.center(ancho_total - 2)}|")
        print(separador)
        for linea in lineas:
            print(f"| {linea.ljust(ancho_total - 3)}|")
        print(separador)

    '''
    ============================================================================================================================================================================
    '''

    '''
    ============================================================================================================================================================================
    ESTE BLOQUE DE CODIGO CUMPLE CON EL REQUERIMIENTO 9, R9. CREAR O MODIFICAR PELICULAS
    '''

    '''
    Autor: David Chica López  
    Fecha: 10/05/2026
    Método agregar_pelicula: Permite agregar una película a la lista de películas.
    Entradas: None
    Salidas: Cadena de texto que confirma que la pelicula fue creada con exito
    '''

    def agregar_pelicula(self)-> str:

        anno_actual = datetime.now().year
        limpiar_pantalla()

        encabezado = "|         Registro de nueva pelicula          |"
        separador = "-" * len(encabezado)
        print(f"\n{separador}")
        print(encabezado)
        print(separador)

        if self.contador_peliculas >= 50:
            print("Error: Capacidad máxima de películas alcanzada")
            return

        nombre_espanol = solicitar_dato("Ingrese el nombre en español de la película: ", "texto")
        nombre_original = solicitar_dato("\nIngrese el nombre original de la película: ", "texto")
        
        identificador_pelicula = self.contador_peliculas + 1

        anno_estreno = solicitar_dato("\nIngrese el año de estreno de la película: ", "numero", 1900, anno_actual)
        duracion = solicitar_dato("\nIngrese la duración (en minutos) de la película: ", "numero", 90, 180)
        
        gen_opc = solicitar_dato("\n---Géneros de la película---\n\n1) Drama \n2) Suspenso \n3) Terror \n4) Acción \n5) Comedia \n6) Infantil\n\nIngrese una opción: ", "numero", 1, 6)
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

        pais_origen = solicitar_dato("\nIngrese el país de origen de la película: ", "texto")

        cal_opc = solicitar_dato("\n---Tipos de clasificación de la película---\n\n1) G      (General) \n2) PG     (Se recomienda la compañía de un adulto) \n3) PG-13  (Se recomienda la compañía de un adulto para menores de 13 años) \n4) R      (Prohibida la entrada a menores de 17 años sin compañía de un adulto) \n5) NC-17  (Prohibida la entrada a menores de 18 años sin compañía de un adulto)\n\nIngrese una opción: ", "numero", 1, 5)
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
        self.guardar_todo()

    '''
    ============================================================================================================================================================================
    '''
    
    '''
    ============================================================================================================================================================================
    ESTE BLOQUE DE CODIGO CUMPLE CON EL REQUERIMIENTO 10, R10.CONSULTAR PORCENTAJE DE OCUPACION
    '''
    
    '''
    Autor: David Chica López  
    Fecha: 23/05/2026
    Metodo consultar_porcentaje_ocupacion: Permite al administrador consultar el porcentaje de ocupación de cada funcion en cada sala, ordenado de mayor a menor.
    Entradas: None
    Salidas: None
    '''

    def consultar_porcentaje_ocupacion(self) -> None:
        if self.complejo.get_cantidad_salas() == 0:
            print("\nNo hay salas registradas en el sistema.")
            input("\nPresione Enter para continuar...")
            return
        
        
        encabezado = "|         Porcentaje de ocupación por sala          |"
        separador = "-" * len(encabezado)
        print(f"\n{separador}")
        print(encabezado)
        print(separador)

        MAX_RESULTADOS = 60
        lista_de_resultados = np.full((MAX_RESULTADOS, 3), fill_value=None, dtype=object)
        contador_resultados = 0

        salas_del_sistema = self.complejo.get_lista_salas()
        for sala_actual in salas_del_sistema:
            if sala_actual != None:
                programacion_de_la_sala = sala_actual.get_programacion()
                
                for funcion_actual in programacion_de_la_sala:
                    if funcion_actual != None:

                        capacidad_total = sala_actual.get_cant_filas() * sala_actual.get_sillas_por_fila()
                        sillas_vendidas = funcion_actual.get_asientos_reservados()
                        
                        if capacidad_total > 0:
                            porcentaje_calculado = (sillas_vendidas / capacidad_total) * 100
                        else:
                            porcentaje_calculado = 0.0
                            
                        id_de_la_sala = sala_actual.get_identificador()
                        id_de_la_funcion = funcion_actual.get_id_funcion()
                        
                        lista_de_resultados[contador_resultados] = np.array([porcentaje_calculado, id_de_la_sala, id_de_la_funcion], dtype=object)
                        contador_resultados += 1

        if contador_resultados == 0:
            print("No se encontraron funciones programadas en las salas.")
        else:

            cantidad_items = contador_resultados
            for i in range(cantidad_items):
                for j in range(0, cantidad_items - i - 1):

                    if lista_de_resultados[j][0] < lista_de_resultados[j + 1][0]:

                        auxiliar = lista_de_resultados[j]
                        lista_de_resultados[j] = lista_de_resultados[j + 1]
                        lista_de_resultados[j + 1] = auxiliar

            for i in range(contador_resultados):
                item = lista_de_resultados[i]
                print(f"|Sala: S{item[1]} | Función: {item[2]} | Ocupación: {item[0]:.2f} %|")
        print(separador)
        input("\nPresione Enter para volver al menú...")




    '''
    ============================================================================================================================================================================
    '''

    '''
    ============================================================================================================================================================================
    ESTE BLOQUE DE CODIGO CUMPLE CON EL REQUERIMIENTO 11, R11. CONSULTAR RECAUDO TOTAL
    '''

    '''
    Autor: Salome Garcia Velasquez
    Fecha: 25/05/2026
    Metodo consultar_recaudo: Permite al administrador consultar el recaudo total ya sea de una sala especifica o del complejo completo.
    Entradas: None
    Salidas: None
    '''

    def consultar_recaudo(self) -> None:

        if self.complejo.get_cantidad_salas() == 0:
            print("No hay salas registradas en el complejo.")
            return

        encabezado = "|         Consultar recaudo total          |"
        separador = "-" * len(encabezado)
        print(f"\n{separador}")
        print(encabezado)
        print(separador)

        print("\n\t1) Recaudo de una sala especifica\n\t2) Recaudo del complejo completo\n")
        tipo_consulta = solicitar_dato("Seleccione una opcion: ", "numero", 1, 2)

        lista_salas = self.complejo.get_lista_salas()

        if tipo_consulta == 1:
            
            ancho_tabla = 38
            separador = "-" * ancho_tabla
            print(f"\n{separador}")
            print(f"|{'Listado de salas disponibles':^36}|")
            print(separador)

            print(f"| {'#':^3} | {'Sala ID':^10} | {'Valor boleta':^15} |")
            print(separador)

            for i in range(len(lista_salas)):
                if lista_salas[i] is not None:
                    print(f"| {i+1:^3} | {lista_salas[i].get_identificador():^10} | {lista_salas[i].get_valor_boleta():^15} |")
            print(separador)

            identificador_sala = solicitar_dato("Ingrese la sala que desea consultar el recaudo: ", "numero", 1, self.complejo.get_cantidad_salas())
            sala = self.complejo.get_sala(identificador_sala)
            
            valor_boleta = sala.get_valor_boleta()
            recaudo_total = 0

            encabezado = f"|Recaudo por función de sala {identificador_sala}|"
            separador = "-" * len(encabezado)
            print(f"\n{separador}")
            print(encabezado)
            print(separador)

            for i in range(len(sala.get_programacion())):
                funcion = sala.get_programacion()[i]
                if funcion is not None:
                    recaudo_funcion = funcion.get_asientos_reservados() * valor_boleta
                    recaudo_total += recaudo_funcion
                    print(f"| Función {funcion.get_id_funcion():<15} | Recaudo: ${recaudo_funcion:<20} |")

            print(f"\n  Recaudo total sala {identificador_sala}: ${recaudo_total:,.0f}")

            input("\nPresione Enter para continuar...")
            return

        elif tipo_consulta == 2:
            recaudo_complejo = 0
            print("\n--- Recaudo del complejo completo ---")
            for i in range(len(lista_salas)):
                sala = lista_salas[i]
                if sala is not None:
                    valor_boleta = sala.get_valor_boleta()
                    recaudo_sala = 0
                    for j in range(len(sala.get_programacion())):
                        funcion = sala.get_programacion()[j]
                        if funcion is not None:
                            recaudo_funcion = funcion.get_asientos_reservados() * valor_boleta
                            recaudo_sala += recaudo_funcion
                    recaudo_complejo += recaudo_sala
                    print(f"  Sala {sala.get_identificador()}: ${recaudo_sala:,.0f}")
            print(f"\n  Recaudo total del complejo: ${recaudo_complejo:,.0f}")
            
            input("\nPresione Enter para continuar...")
            return


    '''
    ============================================================================================================================================================================
    '''

    '''
    ============================================================================================================================================================================
    ESTE BLOQUE DE CODIGO CUMPLE CON EL REQUERIMIENTO 12, R12. CREAR SALA DE CINE
    '''

    '''
    Autor: David Chica López  
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

            identificador_sala = self.contador_salas + 1

            valor_boleta = solicitar_dato("\nIngrese el valor de la boleta: ", "numero", 5000, 50000)

            cant_filas = solicitar_dato("\nIngrese cantidad de filas ( minimo 10, máximo 26 ): ", "numero", 10, 26)

            sillas_por_fila = solicitar_dato("\nIngrese sillas por fila ( mínimo 10, máximo 30 ): ", "numero", 10, 30)

            sala_nueva = SalaCine(identificador_sala, valor_boleta, cant_filas, sillas_por_fila)
            self.contador_salas += 1
            exito = self.complejo.agregar_sala(sala_nueva)
            
            if exito:
                print("\nProceso terminado con éxito.")
                self.guardar_todo()
            else:
                print("No se pudo realizar el registro.")
    '''
    ============================================================================================================================================================================
    '''
    
    '''
    Autor: Salome Garcia   
    Fecha: 21/05/2026  
    Getter de usuario por documento: Permite buscar un usuario en el sistema a partir de su número de documento.
    Entradas: documento (número de documento del usuario a buscar)
    Salidas: Usuario (usuario encontrado) o None (si no se encuentra el usuario)
    '''
    
    def get_usuario_por_documento(self, documento):

        doc_buscado = str(documento)
        for i in range(self.contador_clientes):
            if self.usuarios[i] is not None:
                if str(self.usuarios[i].get_usuario()) == doc_buscado:
                    return self.usuarios[i]
        return None
    
    '''
    Autor: David Chica López  
    Fecha: 30/05/2026
    Metodo cargar_datos: Carga los datos de un archivo en un arreglo específico
    Entradas: archivo(el nombre del archivo), num_max_datos(que es la cantidad maxima de datos que puede tener ese archivo)
    Salidas: Una tupla que contiene el arreglo y la cantidad de datos que carga
    '''

    def cargar_datos(self, archivo: str, num_max_datos: int) -> tuple[np.ndarray, int]:
        try:
            arreglo_de_datos = np.load(archivo, allow_pickle=True)
            i = 0
            while (i < len(arreglo_de_datos) and arreglo_de_datos[i] is not None):
                i += 1
            return arreglo_de_datos, i
        except (FileNotFoundError, EOFError, OSError):
            print(f"No se pudo cargar el archivo {archivo}. Se creó un arreglo de datos vacío!")
            arreglo_de_datos = np.full((num_max_datos), fill_value=None, dtype=object)
            return arreglo_de_datos, 0
        
    '''
    Autor: David Chica López  
    Fecha: 30/05/2026
    Metodo guardar_datos: Guarda los datos de un arreglo en un archivo
    Entradas: arreglo_de_datos(el arreglo a guardar), archivo(el nombre del archivo)
    Salidas: booleano que indica si se pudo guardar los datos o no
    '''

    def guardar_datos(self, arreglo_de_datos: np.ndarray, archivo: str) -> bool:
        try:
            np.save(archivo, arreglo_de_datos)
            return True
        except Exception as e:
            print(f"Error: no se pudieron almacenar los datos en el archivo {archivo}. {e}")
            return False

    '''
    Autor: David Chica López  
    Fecha: 30/05/2026
    Metodo guardar_todo: Guarda todos los datos del sistema en archivos correspondientes
    Entradas: None
    Salidas: None
    '''

    def guardar_todo(self) -> None:
        """ Centraliza el guardado de todos los datos persistentes del sistema """
        print("\nGuardando datos del sistema...")
        self.guardar_datos(self.usuarios, self.ARCHIVO_USUARIOS)
        self.guardar_datos(self.peliculas, self.ARCHIVO_PELICULAS)
        self.guardar_datos(np.array([self.complejo], dtype=object), self.ARCHIVO_COMPLEJO)
        print("Datos guardados correctamente.")

if __name__ == "__main__":
    obj:SistemaCine
    obj = SistemaCine()
    obj.login()
