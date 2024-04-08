#include <stdio.h>
#include <stdlib.h>

// Función para realizar la suma de dos números.
void opcion1() {
    int a, b, suma;
    char buffer[100]; // Buffer para manejar la entrada incorrecta.
    
    // Solicita el primer número hasta que sea válido.
    do {
        printf("Indica primer numero: ");
        if (scanf("%d", &a) != 1) {
            printf("Por favor, ingrese un numero valido.\n");
            scanf("%[^\n]", buffer); // Limpiar el búfer de entrada si no es un número.
        } else {
            break; // Salir del bucle si el número es válido.
        }
    } while (1);
    
    // Solicita el segundo número hasta que sea válido.
    do {
        printf("Indica segundo numero: ");
        if (scanf("%d", &b) != 1) {
            printf("Por favor, ingrese un numero valido.\n");
            scanf("%[^\n]", buffer); // Limpiar el búfer de entrada si no es un número.
        } else {
            break; // Salir del bucle si el número es válido.
        }
    } while (1);
    
    suma = a + b; // Realiza la suma.
    printf("La suma de %d + %d = %d\n", a, b, suma); // Muestra el resultado.
}

// Función para realizar la resta de dos números.
void opcion2() {
    // ... (Similar a la función opcion1 con la operación de resta)
}

// Función para realizar la multiplicación de dos números.
void opcion3() {
    // ... (Similar a la función opcion1 con la operación de multiplicación)
}

// Función para realizar la división de dos números.
void opcion4() {
    // ... (Similar a la función opcion1 con la operación de división y verificación de división por cero)
}

// Función principal que muestra el menú y maneja las opciones.
int main() {
    int op; // Variable para la opción seleccionada.
    int continuar = 1; // Controla la continuidad del menú.
    
    // Bucle principal del menú.
    while (continuar) {
        // Muestra las opciones del menú.
        printf("BIENVENIDO AL MENU\n");
        printf("1. Sumar\n");
        printf("2. Resta\n");
        printf("3. Multiplicacion\n");
        printf("4. Division\n");
        printf("0. Salir\n");
        
        // Solicita la opción del usuario.
        if (scanf("%d", &op) != 1) {
            printf("Por favor, ingrese un numero valido.\n");
            scanf("%*s"); // Limpiar el búfer de entrada si no es un número.
            continue; // Continúa al inicio del bucle si la entrada no es válida.
        }
        
        // Maneja la opción seleccionada.
        switch(op) {
            case 1:
                opcion1(); // Llama a la función de suma.
                break;
            case 2:
                opcion2(); // Llama a la función de resta.
                break;
            case 3:
                opcion3(); // Llama a la función de multiplicación.
                break;
            case 4:
                opcion4(); // Llama a la función de división.
                break;
            case 0:
                printf("Gracias por usar el programa\n"); // Mensaje de despedida.
                continuar = 0; // Establece 'continuar' en 0 para salir del bucle y terminar el programa.
                break;
            default:
                printf("Opcion no valida. Intente nuevamente.\n"); // Mensaje de error para opciones no reconocidas.
                break;
        }
    }
    
    return 0; // Retorna 0 para indicar la terminación exitosa del programa.
}
