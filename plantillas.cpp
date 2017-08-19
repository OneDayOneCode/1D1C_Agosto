#include <iostream>
using namespace std;

/*
 *  Ejemplo sobre las plantillas en C++
 */

template <class NUM>
void suma(NUM numero_1, NUM numero_2)
{
    cout <<"Resultado = "<< numero_1 + numero_2 << endl;
}

int main()
{
    suma(20.5, 20.5);

    return 0;
}
