#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

bool es_caracter_variable(char c) {
    return isalpha(c) || isdigit(c) || c == '_';
}

int main() {
    char input[100];
    printf("Introduce una variable (caracter, booleano o numero entero): ");
    while (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\n")] = '\0';
        if (input[0] == '\0') {
            printf("No has introducido nada. Inténtalo de nuevo.\n");
        } else if (strlen(input) == 1 && isalpha(input[0])) {
            printf("Has introducido un caracter: %c\n", input[0]);
        } else if (strcmp(input, "true") == 0 || strcmp(input, "false") == 0) {
            printf("Has introducido una variable booleana: %s\n", input);
        } else {
            bool esNumero = true, esNegativo = input[0] == '-';
            for (int i = esNegativo ? 1 : 0; input[i] != '\0'; i++) {
                if (!isdigit(input[i])) {
                    esNumero = false;
                    break;
                }
            }
            if (esNumero) {
                printf(esNegativo ? "Los numeros negativos no son validos, intenta de nuevo.\n" : "Has introducido un numero entero: %s\n", input);
            } else {
                bool esVariableCaracter = true;
                for (int i = 0; input[i] != '\0'; i++) {
                    if (!es_caracter_variable(input[i])) {
                        esVariableCaracter = false;
                        break;
                    }
                }
                printf(esVariableCaracter ? "Has introducido una variable de tipo caracter: %s\n" : "Los caracteres especiales o decimales no son validos, intenta de nuevo.\n", input);
            }
        }
        printf("Introduce una variable (caracter, booleano o numero entero): ");
    }
    return 0;
}
