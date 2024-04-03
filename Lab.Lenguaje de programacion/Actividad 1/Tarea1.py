def identificar_variable(variable):
    variable = variable.strip()
    if variable.isdigit():
        return "Entero"
    elif variable.lower() in ["true", "false"]:
        return "Booleano"
    elif variable.isalpha():
        return "Carácter"
    else:
        return "Error"

def main():
    while True:
        variable_usuario = input("Introduce una variable (Carácter, Entero o Booleano): ").strip().lower()
        tipo = identificar_variable(variable_usuario)
        if tipo in ["Carácter", "Entero", "Booleano"]:
            print(f"La variable introducida es de tipo: {tipo}")
            break
        else:
            print("Error: Tipo de variable no reconocido. Por favor, introduce una variable válida (Carácter, Entero o Booleano).")

if __name__ == "__main__":
    main()