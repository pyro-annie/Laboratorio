#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

bool es_caracter_variable(char c) {
    return isalpha(c) || isdigit(c) || c == '_';
}

void limpiar_buffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int main() {
    char input[100];
    printf("Introduce una variable (caracter, booleano o numero entero) o escribe 'Salir' para cerrar el programa: ");
    
    while (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\n")] = '\0';
        
        if (strcmp(input, "Salir") == 0) {
            printf("Cerrando el programa...\n");
            break;
        }
        
        if (strlen(input) == 0) {
            printf("No has introducido nada. Inténtalo de nuevo.\n");
            continue;
        }
        bool entrada_valida = true;
        for (int i = 0; input[i] != '\0'; i++) {
            if (!es_caracter_variable(input[i])) {
                entrada_valida = false;
                break;
            }
        }
        
        if (entrada_valida) {
            printf("Has introducido una variable válida: %s\n", input);
        } else {
            printf("La entrada no cumple con los criterios esperados. Inténtalo de nuevo.\n");
        }
        
        printf("Introduce una variable (caracter, booleano o numero entero) o escribe 'Salir' para cerrar el programa: ");
    }
    
    return 0;
}