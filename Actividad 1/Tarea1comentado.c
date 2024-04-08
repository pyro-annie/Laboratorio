#include <stdio.h>  // Biblioteca estándar de entrada y salida para operaciones de I/O.
#include <string.h> // Biblioteca para manipular arrays de caracteres.
#include <ctype.h>  // Biblioteca para clasificar caracteres y convertir entre mayúsculas y minúsculas.
#include <stdbool.h> // Biblioteca para definir el tipo de dato bool (booleano).

// Función para verificar si un carácter es válido en un nombre de variable.
bool es_caracter_variable(char c) {
    // Un carácter válido es una letra, un dígito o un guión bajo.
    return isalpha(c) || isdigit(c) || c == '_';
}

// Función para limpiar el buffer de entrada si se excede el tamaño del input.
void limpiar_buffer() {
    int c;
    // Lee caracteres hasta encontrar un salto de línea o el final del archivo.
    while ((c = getchar()) != '\n' && c != EOF);
}

int main() {
    // Array para almacenar la entrada del usuario.
    char input[100];
    // Solicita al usuario que introduzca una variable o 'Salir' para terminar.
    printf("Introduce una variable (caracter, booleano o numero entero) o escribe 'Salir' para cerrar el programa: ");
    
    // Bucle principal que se ejecuta hasta que el usuario decida salir.
    while (fgets(input, sizeof(input), stdin)) {
        // Elimina el salto de línea al final de la entrada si existe.
        input[strcspn(input, "\n")] = '\0';
        
        // Comprueba si el usuario desea salir del programa.
        if (strcmp(input, "Salir") == 0) {
            printf("Cerrando el programa...\n");
            break;
        }
        
        // Si la entrada está vacía, solicita al usuario que intente de nuevo.
        if (strlen(input) == 0) {
            printf("No has introducido nada. Inténtalo de nuevo.\n");
            continue;
        }
        
        // Asume que la entrada es válida inicialmente.
        bool entrada_valida = true;
        // Verifica cada carácter de la entrada.
        for (int i = 0; input[i] != '\0'; i++) {
            // Si algún carácter no es válido, marca la entrada como inválida.
            if (!es_caracter_variable(input[i])) {
                entrada_valida = false;
                break;
            }
        }
        
        // Si la entrada es válida, imprime un mensaje confirmando la entrada.
        if (entrada_valida) {
            printf("Has introducido una variable válida: %s\n", input);
        } else {
            // Si la entrada no es válida, solicita al usuario que intente de nuevo.
            printf("La entrada no cumple con los criterios esperados. Inténtalo de nuevo.\n");
        }
        
        // Solicita al usuario que introduzca otra variable o 'Salir'.
        printf("Introduce una variable (caracter, booleano o numero entero) o escribe 'Salir' para cerrar el programa: ");
    }
    
    // Termina el programa con éxito.
    return 0;
}
