#include <stdio.h>  // Biblioteca estándar de entrada y salida para funciones como printf y fgets.
#include <math.h>   // Biblioteca de matemáticas para funciones como modf, que separa la parte fraccionaria y entera de un número.
#include <stdbool.h> // Biblioteca para definir el tipo de dato bool (booleano) para verdadero o falso.
#include <string.h> // Biblioteca para manejar cadenas de caracteres y funciones como strlen y strcspn.
#include <stdlib.h> // Biblioteca estándar para funciones de conversión de cadenas a números, como strtod.

int main() {
    char buffer[1024]; // Arreglo de caracteres para almacenar la entrada del usuario.
    double numero, parteEntera, parteFraccionaria; // Variables para almacenar el número completo, su parte entera y fraccionaria.
    bool entradaValida = false; // Variable booleana para controlar la validación de la entrada.

    while (!entradaValida) { // Bucle que se repite hasta que la entrada sea válida.
        printf("Ingrese un numero decimal: "); // Solicita al usuario que ingrese un número decimal.
        if (fgets(buffer, sizeof(buffer), stdin)) { // Lee la línea de entrada y la almacena en buffer.
            buffer[strcspn(buffer, "\n")] = 0; // Elimina el salto de línea al final de la entrada, si existe.
            char *ptr; // Puntero para usar con strtod y detectar caracteres no numéricos después del número.
            numero = strtod(buffer, &ptr); // Convierte la cadena a un número decimal y almacena el resto en ptr.
            if (ptr == buffer || *ptr != '\0') { // Verifica si ptr no se ha movido o si hay caracteres después del número.
                printf("Entrada invalida. Por favor ingrese solo numeros y un punto decimal.\n"); // Mensaje de error si la entrada no es válida.
            } else {
                entradaValida = true; // Marca la entrada como válida si todo está correcto.
                parteFraccionaria = modf(numero, &parteEntera); // Separa el número en su parte entera y fraccionaria.
                printf("Parte entera: %.0f\n", parteEntera); // Muestra la parte entera.
                printf("Parte fraccionaria: %.2f\n", parteFraccionaria); // Muestra la parte fraccionaria con dos decimales.
            }
        } else {
            int c; // Variable para leer caracteres adicionales si se excede el tamaño del buffer.
            while ((c = getchar()) != '\n' && c != EOF) { } // Limpia el buffer de entrada.
            printf("Error al leer la entrada. Intente de nuevo.\n"); // Mensaje de error si hay un problema al leer la entrada.
        }
    }

    return 0; // Termina el programa con éxito.
}
