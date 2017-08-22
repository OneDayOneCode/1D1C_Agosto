#include <stdio.h>
#define MAX(n1, n2) (n1 > n2) ? n1 : n2

int main(int argc, char** argv)
{
    int numero_1;
    int numero_2;

    printf("Numero 1:");
    scanf("%d", &numero_1);

    printf("Numero 2:");
    scanf("%d", &numero_2);

    printf("\nEl numero mayor es %d\n", MAX(numero_1, numero_2));

    return 0;
}
