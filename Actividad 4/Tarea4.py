def sumar_y_multiplicar(arreglo, multiplicador):
    if multiplicador == 0:
        return 0
    return sum(arreglo) * multiplicador

def solicitar_entrada_numerica(mensaje, tipo='int'):
    while True:
        entrada_usuario = input(mensaje)
        try:
            return int(entrada_usuario) if tipo == 'int' else float(entrada_usuario)
        except ValueError:
            print(f"Por favor, ingresa un número válido. {'Entero' if tipo == 'int' else 'Flotante'} esperado.")

def solicitar_serie_numerica():
    while True:
        entrada_usuario = input("Ingresa la serie numérica separada por comas (ejemplo: 1,2,3,4,5): ")
        try:
            serie_numerica = [int(elemento) for elemento in entrada_usuario.split(',') if elemento.strip()]
            if 1 <= len(serie_numerica) <= 10:
                return serie_numerica
            else:
                print("La serie debe contener entre 1 y 10 números.")
        except ValueError:
            print("Por favor, asegúrate de que todos los elementos sean números enteros.")

def main():
    while True:
        serie_numerica = solicitar_serie_numerica()
        multiplicador = solicitar_entrada_numerica("Ingresa el número multiplicador: ", 'int')
        resultado_final = sumar_y_multiplicar(serie_numerica, multiplicador)
        print(f"El resultado de la operación es: {resultado_final}")
        if input("¿Deseas intentar de nuevo? Escribe 'si' para continuar o cualquier otra cosa para salir: ").lower() != 'si':
            print("Gracias por utilizar el programa. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
