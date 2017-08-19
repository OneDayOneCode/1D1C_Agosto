/*
 *  Singleton basico
 */

final class Singleton
{
    private final static Singleton singleton = new Singleton();

    private Singleton()
    {
        System.out.println("Ya e sido creado");
    }

    public static Singleton getSingleton()
    {
        return singleton;
    }
}

public class Main
{
    public static void main(String[] args)
    {
        Singleton singleton_1 = Singleton.getSingleton();
    }
}
