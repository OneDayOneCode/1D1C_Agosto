#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Calcular e imprimir la suma de 1+2+3+4+5+6.......+50
# Asignamos a una variable el rango del 1 - 51, osea los primeros 50 números

r = range(1, 51)

# Con la función sum se suman los números de una lista

print sum(r),  "Es el resultado de sumar del 1 al 50, uno a uno!"


# Calcular e imprimir el producto 1*2*3*4*5...*50
#Declaramos dos variables
n = 1
h = 1

# Con un ciclo while hacemos lo siguiente..
while n <= 10:
	# Mientras n sea menor o igual a 20 entonces...
	# Multiplicamos h por el valor de n durante cada recorrido del ciclo
	h *= n
	# Ahora a la variable n le sumamos 1 y continua el ciclo
	n += 1

# Al final se imprime el nuevo valor de h
print "El resultado de multiplicar del 1 al 50 uno a uno no da.. ", h
