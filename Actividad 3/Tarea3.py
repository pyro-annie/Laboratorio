def obtener_numero(solicitud):
    while True:
        try:
            valor = float(input(solicitud).strip())
            return valor
        except ValueError:
            print("Por favor, introduce un número válido.")

def mostrar_resultado(resultado):
    return int(resultado) if resultado.is_integer() else resultado

def operacion_matematica(operacion, mensaje):
    print(mensaje)
    num1 = obtener_numero("Introduce el primer número: ")
    num2 = obtener_numero("Introduce el segundo número: ")
    return num1, num2

def calcular(operacion, num1, num2):
    if operacion == 'sumar':
        return num1 + num2
    elif operacion == 'restar':
        return num1 - num2
    elif operacion == 'multiplicar':
        return num1 * num2
    elif operacion == 'dividir':
        return num1 / num2 if num2 != 0 else None

def menu():
    operaciones = {
        '1': ('sumar', "Vamos a sumar dos números."),
        '2': ('restar', "Vamos a restar dos números."),
        '3': ('multiplicar', "Vamos a multiplicar dos números."),
        '4': ('dividir', "Vamos a dividir dos números.")
    }
    while True:
        print("\\nMenú de operaciones matemáticas:")
        for opcion, (operacion, _) in operaciones.items():
            print(f"{opcion}. {operacion.capitalize()}")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ").strip()
        if opcion in operaciones:
            operacion, mensaje = operaciones[opcion]
            num1, num2 = operacion_matematica(operacion, mensaje)
            resultado = calcular(operacion, num1, num2)
            if resultado is not None:
                print(f"Resultado de la operación: {mostrar_resultado(resultado)}")
            else:
                print("No se puede dividir por cero, intenta de nuevo.")
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

menu()
