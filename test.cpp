/*
 * test.cpp
 * Copyright (C) 2017 Marcos <jigoku_shujin@hotmail.com>
 *
 * Distributed under terms of the S/L license.
 */

#include <iostream>
using namespace std;

/*
 *  Template C++ declaracion e implementacion
 */

template<class SUM>
void suma(SUM numero1, SUM numero2)
{
    cout << numero1 + numero2 << endl;
}

int main ()
{
    suma(3.33, 35.3);
}
