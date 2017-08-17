#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script que te dice si tu año es bisiesto y por que

print ("Comprobador de años bisiestos")

fecha = int(input("Escriba un año y le dire si es bisiesto: "))



if fecha % 400 == 0 or (fecha % 100 != 0 and fecha % 4 == 0):
	print "El  anio", fecha, " es un anio bisiesto."
else:
	print "El anio", fecha, " no es un anio bisiesto."

# Nota, el coding no me funcionó por una mala actualización personal de mi SO (los paquetes)
