package CondicionalEjercicio3;
import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        /**============CLASE 10 - VIERNES-10/06/2022============*/
        //EJERCICIO 1: SISTEMA DE CALIFICACIONES CON IF-ELSE
        Scanner leer = new Scanner(System.in);
        System.out.println("Digite un número entre 0 y 10: ");
        var calificacion = Integer.parseInt(leer.nextLine());
        if (calificacion >= 9 && calificacion <= 10) {
            System.out.println("A");
        } else if (calificacion >= 8 && calificacion <= 9) {
            System.out.println("B");
        } else if (calificacion >= 7 && calificacion <= 8) {
            System.out.println("C");
        } else if (calificacion >= 6 && calificacion <= 7) {
            System.out.println("D");
        } else if (calificacion >= 0 && calificacion <= 6) {
            System.out.println("F");
        } else {
            System.out.println("Fuera de rango");
        }
        //EJERCICIO 1: SISTEMA DE CALIFICACIONES CON SWITCH
        System.out.println("Digite un número entre 0 y 10: ");
        calificacion = Integer.parseInt(leer.nextLine());
        switch (calificacion) {
            case 9: case 10:
                System.out.println("A");
                break;
            case 8:
                System.out.println("B");
                break;
            case 7:
                System.out.println("C");
                break;
            case 0: case 1: case 2: case 3: case 4: case 5: case 6:
                System.out.println("D");
                break;
            default:
                System.out.println("Fuera de rango");
        }
    }
}
