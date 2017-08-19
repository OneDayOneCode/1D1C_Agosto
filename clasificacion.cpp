/*
 *  Problema:
 *      Hacer una estructura con los siguientes campos
 *      nombre, edad, sexo y club, asignar una categoria al competidor
 *      juvenil <= 18
 *      señor <= 40
 *      veterano > 40
 */

#include <iostream>
#include <string.h>
using namespace std;

// Declaracion de una estructura en C++
struct Corredor
{
    char nombre[30];
    char club[30];
    char sexo[10];
    int edad;


} * corredor;

int main ()
{
    // Manejo de memoria dinamica
    corredor = new Corredor;
    char categoria[30] = "Categoria:";

    // Uso el getline para limpiar el buffer de entrada ...
    //  ... y evitar que se captura '\n'
    cout << "Nombre:";
    cin.getline(corredor->nombre, 30, '\n');

    cout << "Edad:";
    cin >> corredor->edad;
    cin.ignore(256, '\n');

    cout << "Sexo:";
    cin.getline(corredor->sexo, 10, '\n');

    cout << "Club:";
    cin.getline(corredor->club, 30, '\n');

    if (corredor->edad>= 7 && corredor->edad <= 18)
    {
        // Concatencion de una cadena de caracteres
        strcat(categoria, "Juvenlin");
    }

    else if (corredor->edad >= 19 && corredor->edad <= 40)
    {
        strcat(categoria, "Señor");
    }

    else if(corredor->edad > 40 && corredor->edad <= 100)
    {
        strcat(categoria, "Veterano");
    }

    cout << "\nNombre:" << corredor->nombre << endl;
    cout << "Edad:" << corredor->edad << endl;
    cout << "Sexo:" << corredor->sexo << endl;
    cout << "Club:" << corredor->club << endl;
    cout << categoria << endl;

    // Se libera el bloque de memoria
    delete corredor;

    return 0;
}
