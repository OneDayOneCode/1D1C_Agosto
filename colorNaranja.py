#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Se denomina llamada recursiva a aquellas funciones que en su
    algoritmo, hacen referencia a si misma
"""

# Definimos una función que recibe un parametro

def jugar(intento=1):
	respuesta = raw_input("¿De qué color es una naranja?\n")
	if respuesta != "naranja":
		if intento < 3:
			print "\nFallaste! Inténtalo de nuevo ;)"
			intento += 1
			jugar(intento) # Se vuelve a llamar la función de manera recursiva
		else:
			print "\nPerdiste!"
	else:
		print "\nGanaste!!"


jugar()
