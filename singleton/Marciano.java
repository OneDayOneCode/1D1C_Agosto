package singleton;

public final class Marciano {

    private final static Marciano marciano = new Marciano();
    private static int cMarcianos;

    private Marciano() {
        cMarcianos = 10;
    }

    public static Marciano getMarciano() {
        return marciano;
    }

    public static void eliminar() {
        if(cMarcianos > 0) cMarcianos--;
    }

    public static int getCMarcianos() {
        return cMarcianos;
    }

    public static void cuantosMarcianosQ() {
        if(cMarcianos > 0)
            System.out.printf("Quedan %d marcianos\n", cMarcianos);
        else
            System.out.println("Ya no quedan marcianos...\nHaz ganado.");
    }
}
