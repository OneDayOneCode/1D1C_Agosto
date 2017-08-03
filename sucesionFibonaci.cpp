/*
 * sucecionFibonaci
 * Copyright (C) 2017 Marcos <jigoku_shujin@hotmail.com>
 *
 * Distributed under terms of the S/L license.
 */

/*
 *  Sucesion fibonaci usando recursividad
 */

#include <iostream>
using namespace std;

int sucecion (int);

int main()
{
    cout << sucecion (10);
}

int sucecion(int n)
{   
    if (n == 1)
    {
        n = 0;
    } 

    else if (n == 2)
    {
        n = 1;
    }

    else 
    {
        n =  sucecion (n - 1) + sucecion (n  - 2);
    }

    return n;
}
