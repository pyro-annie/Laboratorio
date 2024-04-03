#include <stdio.h>  // Biblioteca estándar de entrada y salida para operaciones de I/O.
#include <string.h> // Biblioteca para manipular arrays de caracteres.
#include <ctype.h>  // Biblioteca para clasificar caracteres y convertir entre mayúsculas y minúsculas.
#include <stdbool.h> // Biblioteca para definir el tipo de dato bool (booleano).

// Función que determina si un carácter es válido en un nombre de variable.
bool es_caracter_variable(char c) {
    return isalpha(c) || isdigit(c) || c == '_'; // Verifica si es letra, dígito o guión bajo.
}

int main() {
    char input[100]; // Array para almacenar la entrada del usuario.
    printf("Introduce una variable (caracter, booleano o numero entero): ");
    // Bucle que se ejecuta hasta que se interrumpe la entrada.
    while (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\n")] = '\0'; // Elimina el salto de línea al final de la entrada.
        if (input[0] == '\0') { // Verifica si la entrada está vacía.
            printf("No has introducido nada. Inténtalo de nuevo.\n");
        } else if (strlen(input) == 1 && isalpha(input[0])) { // Verifica si es un único carácter alfabético.
            printf("Has introducido un caracter: %c\n", input[0]);
        } else if (strcmp(input, "true") == 0 || strcmp(input, "false") == 0) { // Verifica si es un booleano.
            printf("Has introducido una variable booleana: %s\n", input);
        } else {
            bool esNumero = true, esNegativo = input[0] == '-'; // Inicializa variables para verificar si es un número.
            for (int i = esNegativo ? 1 : 0; input[i] != '\0'; i++) { // Itera sobre la entrada para verificar si es un número.
                if (!isdigit(input[i])) {
                    esNumero = false;
                    break;
                }
            }
            if (esNumero) { // Si es un número, verifica si es negativo y lo imprime.
                printf(esNegativo ? "Los numeros negativos no son validos, intenta de nuevo.\n" : "Has introducido un numero entero: %s\n", input);
            } else {
                bool esVariableCaracter = true; // Inicializa variable para verificar si es un nombre de variable válido.
                for (int i = 0; input[i] != '\0'; i++) { // Itera sobre la entrada para verificar si es un nombre de variable válido.
                    if (!es_caracter_variable(input[i])) {
                        esVariableCaracter = false;
                        break;
                    }
                }
                // Imprime si es un nombre de variable válido o si contiene caracteres no válidos.
                printf(esVariableCaracter ? "Has introducido una variable de tipo caracter: %s\n" : "Los caracteres especiales o decimales no son validos, intenta de nuevo.\n", input);
            }
        }
        // Solicita nuevamente la entrada al usuario.
        printf("Introduce una variable (caracter, booleano o numero entero): ");
    }
    return 0; // Finaliza el programa.
}
