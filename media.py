#!/usr/bin/env python
# -*- coding: utf-8 -*-

print ("Este programa devuelve la media de la suma de dos números")

# Creando la función 

def escribe_media(x, y):
	# Calculando media
	media = (x + y) / 2
	print "La media de ", x, " y ", y, " es: ", media
	return


# El usuario ingresa dos valores

valorA = input("Ingrese el primero número:\n")
valorB = input("Ingrese el segundo número:\n")

# Llamada a la función con paso de parametros que sustituyen 'x' y 'y' en la función

escribe_media(valorA, valorB)

print ("Fín del programa :)")
