# Esta función solicita al usuario que ingrese un número decimal.
def solicitar_numero_decimal():
    # Bucle infinito para solicitar al usuario un número decimal.
    while True:
        entrada = input("Ingresa un número decimal: ")
        # Verificar si la entrada contiene exactamente un punto.
        if entrada.count('.') == 1:
            try:
                # Intentar convertir la entrada a un número decimal (float).
                numero = float(entrada)
                # Si la conversión es exitosa, retornar el número.
                return numero
            except ValueError:
                # Si ocurre un error en la conversión, informar al usuario.
                print("Error: La entrada no es válida. Asegúrate de ingresar solo números decimales.")
        else:
            # Si la entrada no contiene exactamente un punto, informar al usuario.
            print("Error: Debes ingresar un número decimal con un solo punto.")

# Esta función imprime la parte entera y fraccionaria de un número decimal.
def imprimir_partes(numero_decimal):
    # Convertir el número decimal a su parte entera.
    parteEntera = int(numero_decimal)
    # Calcular la parte fraccionaria restando la parte entera del número decimal.
    parteFraccionaria = numero_decimal - parteEntera
    # Imprimir la parte entera y la parte fraccionaria con dos decimales.
    print(f"Parte entera: {parteEntera}")
    print(f"Parte fraccionaria: {parteFraccionaria:.2f}")

# Función principal que ejecuta el programa.
def main():
    # Bucle infinito para procesar números decimales.
    while True:
        # Solicitar al usuario un número decimal.
        numero_decimal = solicitar_numero_decimal()
        # Imprimir las partes entera y fraccionaria del número decimal.
        imprimir_partes(numero_decimal)
        
        # Solicitar al usuario si desea continuar o salir.
        respuesta = input("¿Quieres intentar con otro número decimal? (sí/no): ").strip().lower()
        # Si la respuesta es 'no' o 'salir', terminar el programa.
        if respuesta in ['no', 'salir']:
            print("Programa cerrado.")
            break
        # Si la respuesta no es 'si', informar al usuario y solicitar nuevamente.
        elif respuesta != 'si':
            print("Por favor, responde solo con 'sí' o 'no'.")

# Punto de entrada del programa.
if __name__ == "__main__":
    main()
