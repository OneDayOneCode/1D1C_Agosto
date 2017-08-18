#include <stdio.h>

/*
 *  Programa que calcula si una persona es mayor de edad
 */

void mayor_edad(char* nombre, int edad)
{
    // Operador ternario en C: (condicion) ? verdadero: falso
    (edad >= 18) ? printf("%s es mayor de edad.\n", nombre) :
        printf("%s es menor de edad.\n", nombre);
}

int main()
{
    char nombre[30];
    int edad;

    printf("Nombre:");
    scanf("%s", &nombre);

    printf("Edad:");
    scanf("%d", &edad);

    mayor_edad(nombre, edad);

    return 0;
}
