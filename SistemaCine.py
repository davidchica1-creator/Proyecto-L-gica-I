from Usuario import*
from funciones_utiles import solicitar_dato
from SalasCine import*
from Pelicula import*

class sistemaCine:

    def login(self)->None:
        opcion:int
        print("Bienvenidos a ¿Qué hay para ver?")
        opcion=int(input("Ingresa una de las opciones:\n1.Ingresar.\n2.Salir\n"))

    def menu_crear_sala(complejo):
        print("Registro de Nueva Sala")

        identificador_sala = int(input("Ingrese el identificador de la sala: "))
        solicitar_dato(identificador_sala, "entero", 1, 12)

        valor_boleta = int(input("Ingrese el valor de la boleta: "))
        solicitar_dato(valor_boleta, "entero", 1)

        cant_filas = int(input("Ingrese cantidad de filas: "))
        solicitar_dato(cant_filas, "entero", 1)

        sillas_por_fila = int(input("Ingrese sillas por fila: "))
        solicitar_dato(sillas_por_fila, "entero", 1)
        
        nueva_sala = SalaCine(identificador_sala, valor_boleta, cant_filas, sillas_por_fila)
        
        exito = complejo.agregar_sala(nueva_sala)
        
        if exito:
            print("Proceso terminado con éxito.")
        else:
            print("No se pudo realizar el registro.")
        

        

