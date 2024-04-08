def identificar_variable(variable):
    variable = variable.strip().lower()
    if variable.isdigit():
        return "Entero"
    elif variable in {"true", "false"}:
        return "Booleano"
    elif variable.isalpha():
        return "Carácter"
    else:
        return "Error"

def main():
    while True:
        variable_usuario = input("Introduce una variable (Carácter, Entero o Booleano) o escribe 'salir' para cerrar el programa: ").strip().lower()
        if variable_usuario == "salir":
            print("Programa cerrado.")
            break
        tipo = identificar_variable(variable_usuario)
        if tipo != "Error":
            print(f"La variable introducida es de tipo: {tipo}")
            break
        else:
            print("Error: Tipo de variable no reconocido. Por favor, introduce una variable válida.")

if __name__ == "__main__":
    main()