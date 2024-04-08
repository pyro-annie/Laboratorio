# Esta función identifica el tipo de una variable basada en su contenido.
def identificar_variable(variable):
    # Elimina espacios en blanco al principio y al final de la cadena y convierte a minúsculas
    variable = variable.strip().lower()
    
    # Comprueba si la cadena representa un número entero
    if variable.isdigit():
        return "Entero"
    # Comprueba si la cadena es un valor booleano (true o false)
    elif variable in {"true", "false"}:
        return "Booleano"
    # Comprueba si la cadena contiene solo letras del alfabeto
    elif variable.isalpha():
        return "Carácter"
    # Si no cumple ninguna de las condiciones anteriores, retorna "Error"
    else:
        return "Error"

# Esta es la función principal que se ejecuta al iniciar el programa.
def main():
    # Bucle infinito hasta que se introduzca una variable válida o el usuario escriba "salir"
    while True:
        # Solicita al usuario que introduzca una variable y la procesa
        variable_usuario = input("Introduce una variable (Carácter, Entero o Booleano) o escribe 'salir' para cerrar el programa: ").strip().lower()
        
        # Si el usuario escribe "salir", termina el programa
        if variable_usuario == "salir":
            print("Programa cerrado.")
            break
        
        # Llama a la función identificar_variable para determinar el tipo de la variable introducida
        tipo = identificar_variable(variable_usuario)
        
        # Si el tipo no es "Error", imprime el tipo y sale del bucle
        if tipo != "Error":
            print(f"La variable introducida es de tipo: {tipo}")
            break
        # Si el tipo es "Error", solicita al usuario que introduzca una variable válida
        else:
            print("Error: Tipo de variable no reconocido. Por favor, introduce una variable válida.")

# Punto de entrada del programa. Si el archivo se ejecuta como script principal, llama a la función main
if __name__ == "__main__":
    main()
