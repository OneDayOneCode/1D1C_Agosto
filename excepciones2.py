#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Excepción  de teclado con ctrl-C 
# Poner atencióna las clausulas del código 

try:  # Bloque de código a “vigilar”
    texto = input('Teclear :')  # introducir un dato

except KeyboardInterrupt:  # captura excepción de interrupción 
    print('\nSe ha pulsado ctrl+c') # Interrupción al presionar Ctrl+c

else:  # se ejecuta si no hay error
    print('Ha tecleado {}'.format(texto)) # muestra cadena introducida
 
finally:  # se ejecuta tanto si hay error como si no
    print('fin de programa')  # muestra mensaje final
