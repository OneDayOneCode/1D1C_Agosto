package singleton;

import java.util.Scanner;

public class Juego {

    public static void main(String[] args) {

        Marciano marciano = Marciano.getMarciano();
        Scanner sc = new Scanner(System.in);
        int disparo;

        do {
            System.out.print("(Disparo)-> $");
            disparo = sc.nextInt();

            for(int i = 0; i < disparo; i++) marciano.eliminar();
            marciano.cuantosMarcianosQ();
        } while(marciano.getCMarcianos() != 0);
    }
}
