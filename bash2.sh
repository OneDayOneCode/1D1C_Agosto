#!/bin/bash

# Recuerda hacer ejecutable el archivo con  chmod +x bash2.sh
# echo imprime lineas  en pantalla
# Creando archvios, directorios, eliminando,,,, etc en Bash

echo 'Vamos a crear y mover archivos entre directorios, todo dentro de una carpeta creada en tu Home'
echo 'Usando cp, mv, ls, touch, rm, mkdir, cd ..'
echo 'Creamos una carpeta llamada prueba y accedemos a ella'

# mkdir crea directorios nuevos
mkdir prueba
echo 'Creando.......................'
cd prueba
echo 'Ingresando....................'
echo -e 'Listo!\nCreamos un archivo llamado archivo1.txt'

# Con el comando touch se crea un archivo
touch archivo1.txt
echo 'Creando archivo...'
echo 'Listo!'
echo 'Ahora hacemos un listado en nuestro directorio'
echo '---------------------------------------------------------------------'
ls
echo '---------------------------------------------------------------------' 

# Creamos una copia del fichero con cp dela siguiente manera
echo 'Ahora creamos un backup de archivo1.txt, llamado archivo1_b.txt'
cp archivo1.txt archivo1_b.txt
echo -e 'Copiando...\nListo!\nAhora listamos de nuevo, junto a la opción -l'
echo '----------------------------------------------------------------------'
ls -l
echo '----------------------------------------------------------------------'
echo 'Creando un directorio con mkdir'
mkdir directorioA
echo -e 'Creando...\nListo!\nVeamos todo..'
echo '----------------------------------------------------------------------'
ls 
echo '----------------------------------------------------------------------'
echo 'Ahora movemos con mv seguido del destino un archivo a un directorio'
echo 'Estamos moviendo archivo1_b.txt a directorioA'
mv archivo1_b.txt directorioA/
echo -e 'Listo!\nAhora hagamos un listado de nuevo'
echo '----------------------------------------------------------------------'
ls
echo '----------------------------------------------------------------------'
echo 'Bien!, lo siguiente es moverse a directorioA y hacer un listado para ver el archivo'
cd directorioA
echo -e 'ingresando...\nListo!\nHagamos un listado..'
echo '--------------------------'
ls
echo '--------------------------'
echo -e 'Vamos hacia arriba con cd ..\nMoviendo....'
cd ..
echo 'Listo, ahora estamos en ..'
pwd
echo 'Eliminemos el directorioA recursivamente (con sus archivos internos)'
rm -r directorioA
echo -e 'Eliminando...\nListo!\nAhora borremos el archivo1.txt'
rm archivo1.txt
echo -e 'Borrando...\nListo!\nVerificando que no existe el archivo con ls de nuevo..'
echo '-----------------------------------------------------------------------'
ls
echo '-----------------------------------------------------------------------'
echo 'Por ultimo nos movemos un directorio arriba para poder borrar el directorio prueba y que este Script se pueda volver a ejecutar'
cd ..
rm -r prueba
echo -e 'Listo, usted puede volver a ejecutar el archivo y todo se crea y elimina en el proceso\nSaludos!'
