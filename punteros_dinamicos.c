#include <stdio.h>
#include <stdlib.h> // con esta libreria se trabaja la memoria dinamica

/*
 *  Programa que desmuestra como usar
 *  la memoria dinamica en C
 */

int main(int argc, char** argv)
{
    // malloc reserva el espacio de memoria
    // a este tipo de inicializacion se le llama punteros dinamicos
    char* nombre = malloc(sizeof(char) * 20);

    printf("Nombre:");
    fgets(nombre, 20, stdin);

    printf("\nHola mi nombre es %s\n", nombre);

    // se libera el bloque de memoria que se reservo
    free(nombre);

    return 0;
}
