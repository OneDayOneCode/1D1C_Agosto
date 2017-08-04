package calculadora;
import java.util.Scanner;
import java.util.InputMismatchException;

public class Calculadora implements Operaciones
{
    private Scanner entrada;

    public Calculadora()
    {
       entrada = new Scanner(System.in);  
    }
    
    public void usuarioOperacion()
    {
        try
        {
            System.out.print("Digite la operacion con espacios\nOperacion:");
            operaciones(numeros(), operador(), numeros());
        }

        catch(InputMismatchException e)
        {
            System.out.println("Digito la operacion sin espacios o digito un numero no entero.");
        }
            
        finally
        {
            entrada.close();
        }
    }

    private int numeros()
    {
        return entrada.nextInt();
    }

    private char operador()
    {
        return entrada.next().charAt(0);
    }

    private void operaciones(int n1, char oper, int n2)
    {
        switch(oper)
        {
            case '+':
                    System.out.printf("%d %c %d = %d\n", n1, oper, n2, suma(n1, n2));
            break;
        
            case '-':
                 System.out.printf("%d %c %d = %d\n", n1, oper, n2, resta(n1, n2));
            break;
        
            case '*':                                                              
                System.out.printf("%d %c %d = %d\n", n1, oper, n2, mul(n1, n2));  
            break;
        
            case '/':                                                              
                System.out.printf("%d %c %d = %f%n\n", n1, oper, n2, div(n1, n2));  
            break;

            default:
                   System.err.println("La operacion no recibio los numeros apropiados");
            break;
        }
        
    }

}

interface Operaciones
{
        default public int suma(int numero_1, int numero_2)
        {
            return numero_1 + numero_2;
        }

        default public int resta(int numero_1, int numero_2)
        {
            return numero_1 - numero_2;
        }

        default public int mul(int numero_1, int numero_2)
        {
            return numero_1 * numero_2;
        }

        default public float div(int numero_1, int numero_2)
        {
            return (float) numero_1/numero_2;
        }
}
