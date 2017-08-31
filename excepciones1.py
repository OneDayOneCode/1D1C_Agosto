#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Las excepciones o errores que se pueden producir durante la ejecución de
# un programa Python se gestionan con una construcción try-except.

# Excecpión básica de TypeError

while True:
	try:  # Prueba este bloque de código
		numero = int(input("Introduce solo un entero:\n")) # Almacena el dato de usuario en la variable numero
		print "Su número es el ", numero, " y esde tipo ", type(numero) # Imprime el número y su tipo de dato
		break # Se rompe el programa y finaliza la excepción
	except: # En caso de no meter un número, se lanza el siguiente mensaje de error y se repite el ciclo hasta obtener un entero
		print ("Debe introducir solo un número entero!!")
	


