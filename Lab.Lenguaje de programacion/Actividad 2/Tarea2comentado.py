# Definición de la función solicitar_numero_decimal
def solicitar_numero_decimal():
    # Bucle infinito para solicitar al usuario un número hasta que se ingrese correctamente
    while True:
        entrada = input("Ingresa un número decimal: ")
        try:
            # Intenta convertir la entrada a un número flotante
            numero = float(entrada)
            # Verifica si la entrada contiene un punto decimal
            if '.' in entrada:
                # Si es un número decimal, retorna el número
                return numero
            else:
                # Si no contiene un punto decimal, se considera entero y muestra error
                print("Error: Debes ingresar un número decimal, no un número entero.")
        except ValueError:
            # Se ejecuta si la conversión a flotante falla, indicando que no es un número
            print("Error: La entrada no es válida. Asegúrate de ingresar solo números decimales.")

# Llamada a la función para solicitar un número decimal al usuario
numero_decimal = solicitar_numero_decimal()

# Separa el número decimal en su parte entera y fraccionaria
parteEntera = int(numero_decimal)  # Obtiene la parte entera usando conversión a entero
parteFraccionaria = numero_decimal - parteEntera  # Resta la parte entera del número original para obtener la fracción

# Imprime la parte entera y fraccionaria con formato
print(f"Parte entera: {parteEntera}")  # Muestra la parte entera
print(f"Parte fraccionaria: {parteFraccionaria:.2f}")  # Muestra la parte fraccionaria con dos decimales
