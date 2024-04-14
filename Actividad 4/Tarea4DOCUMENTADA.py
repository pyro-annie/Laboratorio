def sumar_y_multiplicar(arreglo, multiplicador):
    """
    Calcula la suma de los elementos de un arreglo y luego multiplica el resultado por un multiplicador.

    Parámetros:
    arreglo (list): Una lista de números enteros.
    multiplicador (int): Un número entero que se usará para multiplicar la suma del arreglo.

    Retorna:
    int: El resultado de sumar todos los elementos del arreglo y multiplicar la suma por el multiplicador.
    """
    # Si el multiplicador es cero, no es necesario realizar la operación
    if multiplicador == 0:
        return 0
    # Suma los elementos del arreglo y multiplica el resultado por el multiplicador
    return sum(arreglo) * multiplicador

def solicitar_entrada_numerica(mensaje, tipo='int'):
    # Bucle infinito hasta que se reciba una entrada válida
    while True:
        entrada_usuario = input(mensaje)
        try:
            # Intenta convertir la entrada a entero o flotante según el tipo
            return int(entrada_usuario) if tipo == 'int' else float(entrada_usuario)
        except ValueError:
            # Si la conversión falla, solicita al usuario que ingrese un número válido
            print(f"Por favor, ingresa un número válido. {'Entero' if tipo == 'int' else 'Flotante'} esperado.")

def solicitar_serie_numerica():
    # Bucle infinito hasta que se reciba una serie numérica válida
    while True:
        entrada_usuario = input("Ingresa la serie numérica separada por comas (ejemplo: 1,2,3,4,5): ")
        try:
            # Crea una lista de enteros a partir de la entrada del usuario
            serie_numerica = [int(elemento) for elemento in entrada_usuario.split(',') if elemento.strip()]
            # Verifica que la longitud de la serie esté dentro del rango permitido
            if 1 <= len(serie_numerica) <= 10:
                return serie_numerica
            else:
                # Si la serie no tiene la longitud adecuada, informa al usuario
                print("La serie debe contener entre 1 y 10 números.")
        except ValueError:
            # Si algún elemento no es un entero, informa al usuario
            print("Por favor, asegúrate de que todos los elementos sean números enteros.")

def main():
    # Bucle principal del programa
    while True:
        # Solicita al usuario una serie numérica
        serie_numerica = solicitar_serie_numerica()
        # Solicita al usuario un número multiplicador
        multiplicador = solicitar_entrada_numerica("Ingresa el número multiplicador: ", 'int')
        # Calcula el resultado final utilizando la función sumar_y_multiplicar
        resultado_final = sumar_y_multiplicar(serie_numerica, multiplicador)
        # Muestra el resultado de la operación
        print(f"El resultado de la operación es: {resultado_final}")
        # Pregunta al usuario si desea realizar otra operación
        if input("¿Deseas intentar de nuevo? Escribe 'si' para continuar o cualquier otra cosa para salir: ").lower() != 'si':
            # Si el usuario decide no continuar, agradece su uso del programa y termina el bucle
            print("Gracias por utilizar el programa. ¡Hasta luego!")
            break

# Verifica si el script es el punto de entrada principal y, de ser así, ejecuta la función main
if __name__ == "__main__":
    main()
