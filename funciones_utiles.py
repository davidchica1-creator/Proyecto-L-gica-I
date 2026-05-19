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
    while True:
        entrada = input(mensaje).strip()
        
        if not entrada:
            print("Error: El campo no puede estar vacío.")
            continue
            
        if tipo_esperado == 'texto':
            if entrada.isdigit():
                print("Error: El texto no puede ser solo números.")
                continue
            
            tiene_letra = False
            for caracter in entrada:
                if caracter.isalpha():
                    tiene_letra = True
                    break 
            if not tiene_letra:
                print("Error: El texto debe contener letras válidas, no solo símbolos.")
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
                continue 
        
        elif tipo_esperado == 'si_no':
            if entrada.isdigit():
                print("Error: Debes ingresar 'si' o 'no'.")
                continue
            
            if entrada.lower() == 'si' or entrada.lower() == 'no':
                return entrada.lower()
            else:
                print("Error: Debes ingresar 'si' o 'no'.")
                continue

        elif tipo_esperado == 'fecha':
            if validar_formato(entrada, "%d/%m/%Y"):
                return entrada
            else:
                print("Error: El formato de fecha debe ser DD/MM/AAAA.")
                continue
        elif tipo_esperado == 'hora':
            if validar_formato(entrada, "%H:%M"):
                return entrada
            else:
                print("Error: El formato de hora debe ser HH:MM.")
                continue
        else:
            print(f"Error interno: El tipo esperado '{tipo_esperado}' no existe.")
            return None

'''
Autor: David Chica López
Fecha: 04/05/2026
Función: validar_formato
'''

def validar_formato(cadena, formato):
    try:
        datetime.strptime(cadena, formato)
        return True
    except ValueError:
        return False


'''
Autor: David Chica López
Fecha: 18/05/2026
Función: horas_minutos
Entradas: Cadena de texto con el formato HH:MM
Salidas: Numero entero con la cantidad de minutos desde la medianoche
'''

def horas_minutos(time_str: str) -> int:
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes
    
