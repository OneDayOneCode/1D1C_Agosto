/*
 * Numero.java
 * Copyright (C) 2017 Marcos <jigoku_shujin@hotmail.com>
 *
 * Distributed under terms of the S/L license.
 */
import java.util.Scanner;
import java.util.InputMismatchException;

/*
 * Pequeño ejemplo en java sobre una clase anidada
 *
 */

public class Numero
{
    private Scanner entrada;
    private NumerosIE numerosEIE; // EIE : En Ingles y Español

    public Numero()
    {
        this.entrada = new Scanner(System.in);
        this.numerosEIE = new NumerosIE();
    }

    public void numerosEnEI()
    {
       try
       {
            int numeroUsuario = this.datoUsuario();
            this.numerosEIE.numeroEnEyI(numeroUsuario);
       }

       catch(ArrayIndexOutOfBoundsException e)
       {
           System.out.println("El número no esta en un rango del 1 al 10.");
       }

       catch(InputMismatchException e)
       {
           System.out.println("El número no es dato de tipo numerico entero.");
       }

       finally
       {
           this.entrada.close();
       }
    }

    private int datoUsuario()
    {
        System.out.print("Escriba un digito númerico positivo:");
        return this.entrada.nextInt();
    }

    private class NumerosIE
    {
        private String numeros[];

        public NumerosIE()
        {   
            this.numeros = new String[10];
            this.setNumerosIE();
        }

        public void setNumerosIE()
        {
            this.numeros[0] = "Uno\nOne";
            this.numeros[1] = "Dos\nTwo";
            this.numeros[2] = "Tres\nThree";
            this.numeros[3] = "Cuatro\nFour";
            this.numeros[4] = "Cinco\nFive";
            this.numeros[5] = "Seis\nSix";
            this.numeros[6] = "Siete\nSeven";
            this.numeros[7] = "Ocho\nEigth";
            this.numeros[8] = "Nueve\nNine";
            this.numeros[9] = "Diez\nTeen";
        }

        public void numeroEnEyI(int subindice)
        {
            System.out.println(this.numeros[subindice - 1]);
        }
    };
}
