'''
Autor: David Chica López
Fecha: 03/06/2026

Función para validar entradas de usuario.
La función de solicitar_dato se utiliza para validar entradas de texto y números, asegurando que no estén vacías y 
cumplan con los requisitos de tipo y rango en donde sus entradas son; el mensaje a validar, el tipo de dato esperado esperado, y los 
valores mínimo y máximo en caso de se usen menus de opciones, para evitar repetición de código.
'''

from datetime import datetime

def solicitar_dato(mensaje, tipo_esperado, min_val=None, max_val=None):
    """Función genérica para validar entradas de usuario."""
    while True:
        entrada = input(mensaje).strip()
        
        if not entrada:
            print("Error: El campo no puede estar vacío.")
            continue
            
        if tipo_esperado == 'texto':
            if entrada.isdigit():
                print("Error: El nombre no puede ser solo números.")
                continue
            return entrada
            
        elif tipo_esperado == 'numero':
            try:
                valor = int(entrada)
                if min_val is not None and valor < min_val:
                    print(f"Error: El valor mínimo permitido es {min_val}.")
                    continue
                if max_val is not None and valor > max_val:
                    print(f"Error: El valor máximo permitido es {max_val}.")
                    continue
                return valor
            except ValueError:
                print("Error: Debes ingresar un número entero válido.")

'''
Función para validar formato de fecha y hora.
La función validar_formato se utiliza para verificar que una cadena de texto cumpla con un formato específico, como fechas o horas, 
utilizando el módulo datetime para analizar la entrada.
'''

def validar_formato(entrada: str, formato: str) -> bool:
    try:

        datetime.strptime(entrada, formato)
        return True
    except ValueError:

        return False
    
