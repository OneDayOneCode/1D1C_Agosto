#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script que agrega números a una lista siempre y cuando sean positivos
# E imprime el máximo de la lista una vez dejemos de ingresar números 

# Declaramos una lista vacia

lista = []

# Pedimos al usuario que ingrese un número 
# y lo almacenamos en la variable num

num = int(input("Ingrese un número positivo para iniciar la lista:\n "))

# Usamos un ciclo while

while num > 0:
	# Agregamos el contenido de numero a la lista
	lista.append(num)
	# Agregamos más números y el ciclo se repite siempre y cuando sean positivos
	num = int(input("Ingrese un número (cuando guste cortar solo ingrese uno negativo):\n"))

print ("El máximo de la lista es: %d" % max(lista))
print "El contenido de la lista es: ", lista

