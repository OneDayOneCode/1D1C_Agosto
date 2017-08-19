#include <stdio.h> // Cabecera que contiene la entrada y salida estandar

/*
 *  Programa que te da el resultado de una sucesion numerica
 *  Ejemplo: 1 + 2 + 3 = 6.
 *
 *  En este caso usare la recursividad.
 */

int sucesion(int n)
{
    if(n == 1)
    {
        n = 1;
    }

    else
    {
        n += sucesion(n-1);
    }

    return n;
}

int main()
{
    int numero;

    printf("n + ");
    scanf("%d", &numero);

    printf("Resultado de la sucesion es %d\n", sucesion(numero));

    return 0;
}
