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