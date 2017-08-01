#!/usr/bin/python
# -*- coding: utf-8 -*-

# Cifrado parecido al cifrado Cesar
# Recorre 3 indices de caracter para cifrar un mensaje, aunque en este caso
# le pregunta al usuario la cantidad de saltos
# Este programa esta en la versión 2 de Python, intente migrar a ka versión 3
# Declaramos una variable

LONG_LLAVE = 26

# Funcion que interactua con el usuario para ver si desea cifrar o descifrar
# La opción elegida por el usuario se guarda en la variable opcion. 
# El condicional if chequea si existe la opción deseada ingresada por el usuario. 
# El usuario tendrá que escribir la cadena cifrar o c (para cifrar un mensaje) 
# o tendrá que escribir descifrar o d (para descifrar un mensaje). 
# El método split() convierte la cadena "cifrar c descifrar d" en una lista. 

def getOpcion():
	while True:
		print '¿Tu quieres cifrar o descifrar?'
		opcion = raw_input().lower()
		if opcion in 'cifrar c descifrar d'.split():
			return opcion
		else:
			print 'Escribir "cifrar", "c" o "descifrar", "d".'

# Ingreso del mensaje por el usuario
# Esta funcion guarda el mensaje ingresado por el usuario

def getMensaje():
	print 'Escriba el mensaje:'
	return raw_input()

# Ahora vamos a obtener la llave del usuario
# Con el bucle while nos aseguramos de que el usuario ingrese un número
# mayor o igual a 1 y menos o igual a 26, el numero que tiene la varianle LONG_LLAVE

def getLlave():
	llave = 0
	while True:
		print('Ingresar la llave (1-%s)' %(LONG_LLAVE))
		llave = int(input())
		if (llave >= 1 and llave <= LONG_LLAVE):
			return llave

# Ciframos o desciframos un mensaje con la clave dada

def getTraducirMensaje(opcion, mensaje, llave):
	# Tenemos tres parametros la opcion del usuario, el mensaje y la llave
	if opcion[0] == 'd':
		llave = -llave
	traducir = ''
	# El método isalpha() devuelve True si la cadena contiene solo letras (minúsculas y mayúsculas) de la A a la Z.
	# Si la cadena contiene otros caracteres el método isalpha() devolverá False. 
	
	for simbolo in mensaje:
		if simbolo.isalpha():
			num = ord(simbolo)
			num += llave
		# Este for itera sobre cada letra del mensaje asegurando que sea una letra con el método isalpha().
		# Los números, signos de puntuación, etc, quedarán en su forma original. La variable num guardará la letra convertida a número por la función ord().
		# Y por último se suma la llave para desplazar la letra.
		# El método isupper() devolverá True si la cadena tiene al menos una letra en mayúsculas y no contiene minúsculas.
		# El método islower() devolverá True si la cadena tiene al menos una letra en minúscula y no contiene mayúsculas.
		
		if simbolo.isupper():
			if num > ord('Z'):
				num -= 26
			elif num < ord('A'):
				num += 26
		elif simbolo.islower():
			if num > ord('z'):
				num -= 26
				elif num < ord('a'):
					num += 26
					traducir += chr(num)
	else:
		traducir += simbolo
	return traducir
						

opcion = getOpcion()
mensaje = getMensaje
llave = getLlave

print ('El texto traducido es:')
print (getTraducirMensaje(opcion, mensaje, llave))

