#!/bin/bash

# Recuerda dar permisos de ejecución con chmod +x 
echo 'Welcome, este es un ejemplo de redirigir el standar output en la shell'
echo -e 'Creando el directorio dir1\n...............\nListo'
mkdir dir1
echo 'Ingresando.......'
cd dir1
echo -e 'Creamos 5 archivos con nombres de números..\nListo'
touch uno.txt dos.txt tres.txt cuatro.txt cinco.txt
echo ' Ahora guardemos la salida ls con opción -l en un fichero'
ls -l > infofiles.txt 
echo -e 'Listo!\nChecamos el contenido del archivo con el comando cat'
cat infofiles.txt
echo 'Podemos ingresar información con >>, vamos a ingresar un texto al final '
uname -a >> infofiles.txt
echo -e '.............\nListo, ahora leemos el archivo de nuevo'
cat infofiles.txt
echo 'Es todo por ahora y eliminamos los archivos con rm'
cd ..
rm -r dir1
