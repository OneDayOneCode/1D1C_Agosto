/*
 * Ejemplo muy basico sobre una lambda en java
 */

@FunctionalInterface
interface Operacion
{
   int suma(int numero_1, int numero_2);
}

public class Lambda
{
    public Lambda(int numero_1, int numero_2)
    {
        Operacion op = (int n1, int n2)->{return n1 + n2; };
        System.out.printf("El resultado de la suma es %d\n",
                op.suma(numero_1, numero_2));
    }

    public static void main(String[] args)
    {
        Lambda lambda = new Lambda(20, 20);
    }
}


