def solicitar_numero_decimal():
    while True:
        entrada = input("Ingresa un número decimal: ")
        if entrada.count('.') == 1:
            try:
                numero = float(entrada)
                return numero
            except ValueError:
                print("Error: La entrada no es válida. Asegúrate de ingresar solo números decimales.")
        else:
            print("Error: Debes ingresar un número decimal con un solo punto.")

def imprimir_partes(numero_decimal):
    parteEntera = int(numero_decimal)
    parteFraccionaria = numero_decimal - parteEntera
    print(f"Parte entera: {parteEntera}")
    print(f"Parte fraccionaria: {parteFraccionaria:.2f}")

def main():
    while True:
        numero_decimal = solicitar_numero_decimal()
        imprimir_partes(numero_decimal)
        
        respuesta = input("¿Quieres intentar con otro número decimal? (sí/no): ").strip().lower()
        if respuesta in ['no', 'salir']:
            print("Programa cerrado.")
            break
        elif respuesta != 'si':
            print("Por favor, responde solo con 'sí' o 'no'.")

if __name__ == "__main__":
    main()