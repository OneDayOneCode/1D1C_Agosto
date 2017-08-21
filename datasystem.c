#include <stdio.h>

/*
 *  Programa que determina que trabajador tiene un menor y
 *  mayor salario.
 */

struct emplado
{
    char nombre[30];
    char sexo[15];
    int sueldo;
};

void salario_menor_mayor(struct emplado e[], int num_empleados)
{
    int mayor_sueldo = e[0].sueldo, posicion_m = 0;
    int menor_sueldo = e[0].sueldo, posicion_me = 0;

    for(int i = 0; i < num_empleados; i++)
    {
       if(e[i].sueldo > mayor_sueldo)
       {
           mayor_sueldo = e[i].sueldo;
           posicion_m = i;
       }

       if(e[i].sueldo < menor_sueldo)
       {
           menor_sueldo = e[i].sueldo;
           posicion_me = i;
       }
    }

    printf("\nLa persona con mayor salario es %s\n", e[posicion_m].nombre);
    printf("La persona con menor salario es %s\n", e[posicion_me].nombre);

}

int main(int argc, char* argv[])
{
   int num_empleado;

   printf("Numero de empleados:");
   scanf("%d", &num_empleado);

   struct emplado emp[num_empleado];

   for(int i = 0; i < num_empleado; i++)
   {
       printf("\nNombre:");
       scanf("%s", &emp[i].nombre);

       printf("Sexo:");
       scanf("%s", &emp[i].sexo);

       printf("Sueldo:");
       scanf("%d", &emp[i].sueldo);
   }

   salario_menor_mayor(emp, num_empleado);

    return 0;
}

