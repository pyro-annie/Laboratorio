#include <stdio.h>
#include <stdlib.h>

void opcion1() {
    int a, b, suma;
    char buffer[100];
    
    do {
        printf("Indica primer numero: ");
        if (scanf("%d", &a) != 1) {
            printf("Por favor, ingrese un numero valido.\n");
            scanf("%[^\n]", buffer); // Limpiar el búfer de entrada
        } else {
            break;
        }
    } while (1);
    
    do {
        printf("Indica segundo numero: ");
        if (scanf("%d", &b) != 1) {
            printf("Por favor, ingrese un numero valido.\n");
            scanf("%[^\n]", buffer); // Limpiar el búfer de entrada
        } else {
            break;
        }
    } while (1);
    
    suma = a + b;
    printf("La suma de %d + %d = %d\n", a, b, suma);
}

void opcion2() {
    int a, b, resta;
    char buffer[100];
    
    do {
        printf("Indica primer numero: ");
        if (scanf("%d", &a) != 1) {
            printf("Por favor, ingrese un numero valido.\n");
            scanf("%[^\n]", buffer); // Limpiar el búfer de entrada
        } else {
            break;
        }
    } while (1);
    
    do {
        printf("Indica segundo numero: ");
        if (scanf("%d", &b) != 1) {
            printf("Por favor, ingrese un numero valido.\n");
            scanf("%[^\n]", buffer); // Limpiar el búfer de entrada
        } else {
            break;
        }
    } while (1);
    
    resta = a - b;
    printf("La resta de %d - %d = %d\n", a, b, resta);
}

void opcion3() {
    int a, b, mult;
    char buffer[100];
    
    do {
        printf("Indica primer numero: ");
        if (scanf("%d", &a) != 1) {
            printf("Por favor, ingrese un numero valido.\n");
            scanf("%[^\n]", buffer); // Limpiar el búfer de entrada
        } else {
            break;
        }
    } while (1);
    
    do {
        printf("Indica segundo numero: ");
        if (scanf("%d", &b) != 1) {
            printf("Por favor, ingrese un numero valido.\n");
            scanf("%[^\n]", buffer); // Limpiar el búfer de entrada
        } else {
            break;
        }
    } while (1);
    
    mult = a * b;
    printf("La multiplicacion de %d * %d = %d\n", a, b, mult);
}

void opcion4() {
    float a, b, division;
    char buffer[100];
    
    do {
        printf("Indica primer numero: ");
        if (scanf("%f", &a) != 1) {
            printf("Por favor, ingrese un numero valido.\n");
            scanf("%[^\n]", buffer); // Limpiar el búfer de entrada
        } else {
            break;
        }
    } while (1);
    
    do {
        printf("Indica segundo numero: ");
        if (scanf("%f", &b) != 1) {
            printf("Por favor, ingrese un numero valido.\n");
            scanf("%[^\n]", buffer); // Limpiar el búfer de entrada
        } else if (b == 0) {
            printf("No se puede dividir por cero. Intente nuevamente.\n");
        } else {
            break;
        }
    } while (1);
    
    if (b != 0) {
        division = a / b;
        printf("La division de %.2f / %.2f = %.2f\n", a, b, division);
    }
}

int main() {
    int op;
    int continuar = 1;
    
    while (continuar) {
        printf("BIENVENIDO AL MENU\n");
        printf("1. Sumar\n");
        printf("2. Resta\n");
        printf("3. Multiplicacion\n");
        printf("4. Division\n");
        printf("0. Salir\n");
        
        if (scanf("%d", &op) != 1) {
            printf("Por favor, ingrese un numero valido.\n");
            scanf("%*s"); // Limpiar el búfer de entrada
            continue;
        }
        
        switch(op) {
            case 1:
                opcion1();
                break;
            case 2:
                opcion2();
                break;
            case 3:
                opcion3();
                break;
            case 4:
                opcion4();
                break;
            case 0:
                printf("Gracias por usar el programa\n");
                continuar = 0;
                break;
            default:
                printf("Opcion no valida. Intente nuevamente.\n");
                break;
        }
    }
    
    return 0;
}