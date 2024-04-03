# Definición de la función 'identificar_variable'
def identificar_variable(variable):
    # Elimina espacios en blanco al inicio y al final de la entrada
    variable = variable.strip()
    # Verifica si la entrada es un número entero
    if variable.isdigit():
        return "Entero"
    # Verifica si la entrada es un valor booleano (True o False)
    elif variable.lower() in ["true", "false"]:
        return "Booleano"
    # Verifica si la entrada es alfabética (solo letras)
    elif variable.isalpha():
        return "Carácter"
    # Si no cumple con las condiciones anteriores, retorna un error
    else:
        return "Error"

# Definición de la función principal 'main'
def main():
    # Bucle infinito para solicitar al usuario una entrada
    while True:
        # Solicita al usuario que introduzca una variable y la formatea
        variable_usuario = input("Introduce una variable (Carácter, Entero o Booleano): ").strip().lower()
        # Llama a la función 'identificar_variable' para determinar el tipo
        tipo = identificar_variable(variable_usuario)
        # Si el tipo es válido, imprime el tipo y termina el bucle
        if tipo in ["Carácter", "Entero", "Booleano"]:
            print(f"La variable introducida es de tipo: {tipo}")
            break
        # Si el tipo no es válido, informa al usuario y solicita otra entrada
        else:
            print("Error: Tipo de variable no reconocido. Por favor, introduce una variable válida (Carácter, Entero o Booleano).")

# Verifica si el script es el punto de entrada principal y llama a 'main'
if __name__ == "__main__":
    main()
