def obtener_numero(solicitud):
    while True:
        entrada = input(solicitud).strip()
        if entrada:
            try:
                valor = float(entrada)
                return valor
            except ValueError:
                print("Por favor, introduce un número válido.")
        else:
            print("No se permiten cadenas vacías. Inténtalo de nuevo.")

def mostrar_resultado(resultado):
    return int(resultado) if resultado.is_integer() else resultado

def operacion_matematica(operacion):
    num1 = obtener_numero(f"Introduce el primer número para {operacion}: ")
    num2 = obtener_numero(f"Introduce el segundo número para {operacion}: ")
    return num1, num2

def suma():
    num1, num2 = operacion_matematica('sumar')
    return mostrar_resultado(num1 + num2)

def resta():
    num1, num2 = operacion_matematica('restar')
    return mostrar_resultado(num1 - num2)

def multiplicacion():
    num1, num2 = operacion_matematica('multiplicar')
    return mostrar_resultado(num1 * num2)

def division():
    while True:
        num1, num2 = operacion_matematica('dividir')
        if num2 != 0:
            return mostrar_resultado(num1 / num2)
        else:
            print("No se puede dividir por cero, intenta de nuevo.")

def menu():
    opciones = {
        '1': suma,
        '2': resta,
        '3': multiplicacion,
        '4': division
    }
    while True:
        print("\nMenú de operaciones matemáticas:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ").strip()
        if opcion in opciones:
            resultado = opciones[opcion]()
            print(f"Resultado de la operación: {resultado}") 
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

menu()