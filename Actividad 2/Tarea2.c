#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char buffer[1024];
    double numero, parteEntera, parteFraccionaria;
    bool entradaValida = false;

    while (!entradaValida) {
        printf("Ingrese un numero decimal: ");
        if (fgets(buffer, sizeof(buffer), stdin)) {
            buffer[strcspn(buffer, "\n")] = 0;
            char *ptr;
            numero = strtod(buffer, &ptr);
            if (ptr == buffer || *ptr != '\0') {
                printf("Entrada invalida. Por favor ingrese solo numeros y un punto decimal.\n");
            } else {
                entradaValida = true;
                parteFraccionaria = modf(numero, &parteEntera);
                printf("Parte entera: %.0f\n", parteEntera);
                printf("Parte fraccionaria: %.2f\n", parteFraccionaria);
            }
        } else {
            int c;
            while ((c = getchar()) != '\n' && c != EOF) { }
            printf("Error al leer la entrada. Intente de nuevo.\n");
        }
    }

    return 0;
}
