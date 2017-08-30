#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script qu imprime la serie fibonacci de un rango de números
# Para más información 'googlear' como funciona la serie fibonacci, nunca dejes de aprender, leer  y ser curioso ;) 

# Declaramos variables

numero = 1
ultimo = 0
antes_de_ultimo = 0

print "Esta es la serie fibonacci de cierto rango, para modificar...\nRevise el código y cambie el rango en el ciclo for:"

for contador in range(0, 10):
	# Se imprime la variable contador concatenada 
	# de numero que ira cambiando conforme el cuerpo del ciclo
	print contador, " = ", numero
	# Reasignamos contenidos de variables 
	antes_de_ultimo = ultimo
	
	ultimo = numero
	
	numero = antes_de_ultimo + ultimo


