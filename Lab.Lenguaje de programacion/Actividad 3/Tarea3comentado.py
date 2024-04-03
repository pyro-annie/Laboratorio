# Esta función solicita al usuario un número y lo valida.
def obtener_numero(solicitud):
    while True:  # Bucle infinito hasta que se ingrese un número válido.
        entrada = input(solicitud).strip()  # Solicita entrada y elimina espacios en blanco.
        if entrada:  # Verifica que la cadena no esté vacía.
            try:
                valor = float(entrada)  # Intenta convertir la entrada a un número flotante.
                return valor  # Si es exitoso, retorna el valor.
            except ValueError:  # Si la conversión falla, se maneja la excepción.
                print("Por favor, introduce un número válido.")  # Pide al usuario que ingrese un número válido.
        else:
            print("No se permiten cadenas vacías. Inténtalo de nuevo.")  # Informa que no se aceptan cadenas vacías.

# Esta función convierte el resultado a entero si es un número entero, de lo contrario lo deja como flotante.
def mostrar_resultado(resultado):
    return int(resultado) if resultado.is_integer() else resultado  # Usa comprensión condicional para la conversión.

# Esta función maneja la operación matemática solicitando dos números al usuario.
def operacion_matematica(operacion):
    num1 = obtener_numero(f"Introduce el primer número para {operacion}: ")  # Obtiene el primer número.
    num2 = obtener_numero(f"Introduce el segundo número para {operacion}: ")  # Obtiene el segundo número.
    return num1, num2  # Retorna ambos números.

# Funciones para cada operación matemática que devuelven el resultado de la operación correspondiente.
def suma():
    num1, num2 = operacion_matematica('sumar')  # Obtiene los números para sumar.
    return mostrar_resultado(num1 + num2)  # Realiza la suma y muestra el resultado.

def resta():
    num1, num2 = operacion_matematica('restar')  # Obtiene los números para restar.
    return mostrar_resultado(num1 - num2)  # Realiza la resta y muestra el resultado.

def multiplicacion():
    num1, num2 = operacion_matematica('multiplicar')  # Obtiene los números para multiplicar.
    return mostrar_resultado(num1 * num2)  # Realiza la multiplicación y muestra el resultado.

def division():
    while True:  # Bucle infinito hasta que el divisor sea diferente de cero.
        num1, num2 = operacion_matematica('dividir')  # Obtiene los números para dividir.
        if num2 != 0:  # Verifica que el divisor no sea cero.
            return mostrar_resultado(num1 / num2)  # Realiza la división y muestra el resultado.
        else:
            print("No se puede dividir por cero, intenta de nuevo.")  # Informa que no se puede dividir por cero.

# Esta función muestra un menú de operaciones matemáticas y maneja la selección del usuario.
def menu():
    opciones = {
        '1': suma,
        '2': resta,
        '3': multiplicacion,
        '4': division
    }  # Diccionario de opciones de operaciones.
    while True:  # Bucle infinito para el menú.
        print("\nMenú de operaciones matemáticas:")  # Muestra las opciones del menú.
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ").strip()  # Solicita la opción al usuario.
        if opcion in opciones:  # Verifica si la opción está en el diccionario.
            resultado = opciones[opcion]()  # Ejecuta la función asociada a la opción.
            print(f"Resultado de la operación: {resultado}")  # Muestra el resultado de la operación.
        elif opcion == '5':  # Si la opción es 5, sale del programa.
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")  # Informa que la opción no es válida.

menu()  # Llama a la función del menú para iniciar el programa.
