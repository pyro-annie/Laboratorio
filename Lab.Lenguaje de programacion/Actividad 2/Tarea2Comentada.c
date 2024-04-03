#include <stdio.h> // Incluye la biblioteca estándar de entrada y salida
#include <math.h> // Incluye la biblioteca matemática

int main() {
    double numero = 7.52; // Declara e inicializa la variable 'numero' con el valor 7.52
    double parteEntera, parteFraccionaria; // Declara las variables para la parte entera y fraccionaria

    // La función modf separa 'numero' en su parte entera y fraccionaria
    // La parte entera se almacena en 'parteEntera' y la función retorna la parte fraccionaria
    parteFraccionaria = modf(numero, &parteEntera);

    // Multiplica la parte fraccionaria por 100 para convertirla en un número entero (52 en este caso)
    parteFraccionaria *= 100;

    // Imprime la parte entera y fraccionaria
    // %.0f formatea el número para no mostrar decimales
    printf("Parte entera: %.0f\n", parteEntera);
    printf("Parte fraccionaria: %.0f\n", parteFraccionaria);

    return 0; // Termina la ejecución del programa con éxito
}
