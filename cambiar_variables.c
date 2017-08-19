#include <stdio.h>

void cambiar_variable(int* numero_1, int* numero_2)
{
    printf("\nCambiando valores\n");
    int aux = *numero_1;
    *numero_1 = *numero_2;
    *numero_2 = aux;
}

int main()
{
    int n1 = 20;
    int n2 = 30;

    printf("Valores iniciales\nNumero 1 = %d\nNumero 2 = %d\n", n1, n2);

    cambiar_variable(&n1, &n2);

    printf("Numero 1 = %d\nNumero 2  = %d\n", n1, n2);

    return 0;
}
