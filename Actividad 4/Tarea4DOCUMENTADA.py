def sumar_y_multiplicar(arreglo, multiplicador):
    """
    Esta función toma un arreglo de números y un multiplicador, luego suma los elementos del arreglo y multiplica el resultado por el multiplicador.
    La función también considera la ley de los signos al multiplicar.

    Parámetros:
    - arreglo (list): Una lista de enteros que representa la serie numérica a sumar.
    - multiplicador (int): El número entero por el cual se multiplicará la suma del arreglo.

    Retorna:
    - int: El resultado de la suma de los elementos del arreglo multiplicado por el multiplicador.
           Si ambos, la suma y el multiplicador, son negativos, se multiplica sus valores absolutos.
           Si el multiplicador es cero, el resultado será cero, independientemente de la suma del arreglo.
    """
    # Verifica si el multiplicador es cero, ya que cualquier número multiplicado por cero es cero.
    if multiplicador == 0:
        return 0

    # Calcula la suma de los elementos del arreglo.
    suma = sum(arreglo)

    # Si tanto la suma como el multiplicador son negativos, se multiplica sus valores absolutos.
    # Esto es conforme a la ley de los signos: menos por menos es más.
    if suma < 0 and multiplicador < 0:
        return abs(suma) * abs(multiplicador)
    else:
        # En cualquier otro caso, se realiza la multiplicación directamente.
        return suma * multiplicador

def solicitar_entrada_numerica(mensaje, tipo='int'):
    """
    Pide al usuario que ingrese un número y verifica que sea del tipo especificado (entero o flotante).
    Si el usuario ingresa un valor que no se puede convertir al tipo especificado, se le solicitará que intente de nuevo.

    Parámetros:
    - mensaje (str): El mensaje que se mostrará al usuario para pedirle que ingrese un número.
    - tipo (str): El tipo de número que se espera ('int' para enteros o 'float' para flotantes).

    Retorna:
    - int o float: El número ingresado por el usuario, ya convertido al tipo especificado.
    """
    while True:
        entrada_usuario = input(mensaje)
        try:
            # Intenta convertir la entrada del usuario al tipo especificado.
            if tipo == 'int':
                return int(entrada_usuario)
            elif tipo == 'float':
                return float(entrada_usuario)
        except ValueError:
            # Si la conversión falla, informa al usuario y pide que intente de nuevo.
            print(f"Por favor, ingresa un número válido. {'Entero' if tipo == 'int' else 'Flotante'} esperado.")

def solicitar_serie_numerica():
    """
    Solicita al usuario que ingrese una serie de números enteros separados por comas.
    Verifica que todos los elementos ingresados sean enteros y que la cantidad de números esté entre 1 y 10.

    Retorna:
    - list: Una lista de enteros que representa la serie numérica ingresada por el usuario.
    """
    while True:
        entrada_usuario = input("Ingresa la serie numérica separada por comas (ejemplo: 1,2,3,4,5): ")
        elementos = entrada_usuario.split(',')
        serie_numerica = []

        for elemento in elementos:
            elemento = elemento.strip()  # Elimina espacios en blanco al inicio y final del elemento.
            if elemento:  # Verifica que el elemento no esté vacío.
                try:
                    # Intenta convertir el elemento a entero y lo añade a la lista si es exitoso.
                    numero = int(elemento)
                    serie_numerica.append(numero)
                except ValueError:
                    # Si la conversión falla, informa al usuario y reinicia el proceso.
                    print("Por favor, asegúrate de que todos los elementos sean números enteros.")
                    break
        else:
            # Verifica que la lista tenga entre 1 y 10 elementos.
            if serie_numerica and len(serie_numerica) <= 10:
                return serie_numerica
            else:
                print("La serie debe contener entre 1 y 10 números.")

def main():
    """
    Función principal del programa. Solicita al usuario una serie numérica y un multiplicador,
    luego llama a la función sumar_y_multiplicar para obtener y mostrar el resultado.
    Permite al usuario repetir el proceso o terminar el programa.

    No tiene parámetros ni retorna valores.
    """
    while True:
        # Solicita al usuario una serie numérica y un multiplicador.
        serie_numerica = solicitar_serie_numerica()
        multiplicador = solicitar_entrada_numerica("Ingresa el número multiplicador: ", 'int')

        # Calcula y muestra el resultado de la operación.
        resultado_final = sumar_y_multiplicar(serie_numerica, multiplicador)
        print(f"El resultado de la operación es: {resultado_final}")

        # Pregunta al usuario si desea repetir el proceso o terminar el programa.
        if input("¿Deseas intentar de nuevo? Escribe 'si' para continuar o cualquier otra cosa para salir: ").lower() != 'si':
            print("Gracias por utilizar el programa. ¡Hasta luego!")
            break

# Verifica si el script se está ejecutando como programa principal y, en ese caso, llama a la función main.
if __name__ == "__main__":
    main()
