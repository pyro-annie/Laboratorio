def solicitar_numero_decimal():
    while True:
        entrada = input("Ingresa un número decimal: ")
        try:
            # Intenta convertir la entrada a un número flotante
            numero = float(entrada)
            # Verifica si la entrada es un número decimal (no entero)
            if '.' in entrada:
                return numero
            else:
                print("Error: Debes ingresar un número decimal, no un número entero.")
        except ValueError:
            # Se ejecuta si la conversión falla, lo que significa que no es un número
            print("Error: La entrada no es válida. Asegúrate de ingresar solo números decimales.")

# Solicita al usuario que ingrese un número decimal válido
numero_decimal = solicitar_numero_decimal()

# Separa el número en su parte entera y fraccionaria
parteEntera = int(numero_decimal)
parteFraccionaria = numero_decimal - parteEntera

# Imprime la parte entera y fraccionaria
print(f"Parte entera: {parteEntera}")
print(f"Parte fraccionaria: {parteFraccionaria:.2f}")
