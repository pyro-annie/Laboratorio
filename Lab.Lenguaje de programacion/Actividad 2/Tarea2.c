#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

int main() {
    char buffer[1024];
    double numero, parteEntera, parteFraccionaria;
    bool entradaValida = false;

    // Solicitar al usuario un número hasta que la entrada sea válida
    while (!entradaValida) {
        printf("Ingrese un numero decimal: ");
        if (fgets(buffer, sizeof(buffer), stdin)) {
            // Verificar si la entrada contiene caracteres no deseados
            entradaValida = true;
            for (int i = 0; i < strlen(buffer); i++) {
                if ((buffer[i] < '0' || buffer[i] > '9') && buffer[i] != '.' && buffer[i] != '\n') {
                    entradaValida = false;
                    break;
                }
            }
            if (entradaValida) {
                // Convertir la entrada a un número decimal
                numero = atof(buffer);
                parteFraccionaria = modf(numero, &parteEntera);
                printf("Parte entera: %.0f\n", parteEntera);
                printf("Parte fraccionaria: %.2f\n", parteFraccionaria);
            } else {
                printf("Entrada invalida. Por favor ingrese solo numeros y un punto decimal.\n");
            }
        } else {
            // Error al leer la entrada
            printf("Error al leer la entrada. Intente de nuevo.\n");
            entradaValida = false;
        }
    }

    return 0;
}
