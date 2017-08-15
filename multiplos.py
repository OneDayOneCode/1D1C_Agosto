#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Vamos a imprimir los números del 1 al 50, calcular la suma de los
pares por un lado y los impares por otro"""

# Ingresamos un número dentro de la variable 'entrada' con la función input

entrada = input("Hola, vamos a imprimir los multiplos de su número:\nIngrese el número....")

# Declaramos dos variables, una para pasar durante el while y otra como contador

var = 1
cont = 0

"""Aplicamos un while para nuestra operación
   Mientras la variable 'var' que vale 1 para comenzar, sea menor a 50 se aplica
   lo siguiente"""
while var < 50:
    # Si el residuo de la división de var y entrada da cero..
    if var%entrada == 0:
        # Entonces, se imprime var
        print var,
        cont += 1 # A la variable cont se le suma 1
    var += 1 # a nuestra variabke var se le suma 1

# Se imprime el resultado concatenado
print "\nEntre 1 y 50 hay ",cont, "números multiplos de ", entrada 
