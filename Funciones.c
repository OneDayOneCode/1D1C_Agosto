/*
 ============================================================================
 Name        : HolaMundo.c
 Author      : Token
 Version     :0.0
 Copyright   : Done by Token
 Description : Funciones en C.
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

//Declaración de funciones aquí.
void mensaje(char mensaje[]);
void sumar(int n1,int n2);
void restar(int n1,int n2);

int main(void)
{
	mensaje("Buenos días\n");
	printf("Hola Mundo\n");
	sumar(1,2);
	restar(1,2);
	return 0;
}

//Definición de funciones debajo de este mensaje.
void mensaje(char mensaje[])
{
	printf("%s",mensaje);
	return;
}

void sumar(int n1,int n2)
{
	int numero=n1+n2;
	printf("La suma de %d + %d es: %d\n",n1,n2,numero);
	return;
}

void restar(int n1,int n2)
{
	int numero=n1-n2;
	printf("La resta de %d - %d es: %d\n",n1,n2,numero);
	return;
}
