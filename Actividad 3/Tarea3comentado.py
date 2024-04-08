# Esta función solicita al usuario que ingrese un número y lo valida.
def obtener_numero(solicitud):
    while True:  # Bucle infinito hasta que se ingrese un número válido.
        try:
            # Intenta convertir la entrada del usuario en un número flotante.
            valor = float(input(solicitud).strip())
            return valor  # Si es exitoso, retorna el valor.
        except ValueError:
            # Si se produce un error, indica al usuario que ingrese un número válido.
            print("Por favor, introduce un número válido.")

# Esta función ajusta el resultado a entero si no tiene decimales.
def mostrar_resultado(resultado):
    # Retorna el resultado como entero si no tiene parte decimal, de lo contrario, como flotante.
    return int(resultado) if resultado.is_integer() else resultado

# Esta función maneja la entrada de los dos números para la operación matemática.
def operacion_matematica(operacion, mensaje):
    print(mensaje)  # Muestra el mensaje correspondiente a la operación.
    num1 = obtener_numero("Introduce el primer número: ")  # Solicita el primer número.
    num2 = obtener_numero("Introduce el segundo número: ")  # Solicita el segundo número.
    return num1, num2  # Retorna ambos números.

# Esta función realiza la operación matemática seleccionada.
def calcular(operacion, num1, num2):
    # Realiza la operación basada en la opción elegida por el usuario.
    if operacion == 'sumar':
        return num1 + num2
    elif operacion == 'restar':
        return num1 - num2
    elif operacion == 'multiplicar':
        return num1 * num2
    elif operacion == 'dividir':
        # Verifica que el divisor no sea cero antes de dividir.
        return num1 / num2 if num2 != 0 else None

# Esta función muestra el menú de operaciones y maneja la lógica del programa.
def menu():
    # Diccionario que asocia cada opción del menú con su operación y mensaje correspondiente.
    operaciones = {
        '1': ('sumar', "Vamos a sumar dos números."),
        '2': ('restar', "Vamos a restar dos números."),
        '3': ('multiplicar', "Vamos a multiplicar dos números."),
        '4': ('dividir', "Vamos a dividir dos números.")
    }
    while True:  # Bucle infinito para el menú.
        print("\\nMenú de operaciones matemáticas:")
        # Muestra las opciones de operaciones matemáticas disponibles.
        for opcion, (operacion, _) in operaciones.items():
            print(f"{opcion}. {operacion.capitalize()}")
        print("5. Salir")  # Opción para salir del programa.
        opcion = input("Elige una opción (1-5): ").strip()  # Solicita al usuario que elija una opción.
        if opcion in operaciones:  # Si la opción es válida, realiza la operación.
            operacion, mensaje = operaciones[opcion]
            num1, num2 = operacion_matematica(operacion, mensaje)
            resultado = calcular(operacion, num1, num2)
            if resultado is not None:
                # Muestra el resultado si la división no fue por cero.
                print(f"Resultado de la operación: {mostrar_resultado(resultado)}")
            else:
                # Informa al usuario que no se puede dividir por cero.
                print("No se puede dividir por cero, intenta de nuevo.")
        elif opcion == '5':  # Si la opción es 5, sale del programa.
            print("Saliendo del programa...")
            break
        else:
            # Informa al usuario que la opción no es válida y repite el menú.
            print("Opción no válida, intenta de nuevo.")

menu()  # Llama a la función del menú para iniciar el programa.

