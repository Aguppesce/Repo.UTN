package EjercicioCiclos02.Ciclos02;

import java.util.Scanner;

public class Ejercicio02 {

    //PROGRAMACION_II

    /*============CLASE 2 - VIERNES-01/09/2022============*/

    /*Ejercicio 02: Leer un número e indicar si es positivo o negativo. El proceso se repetira hasta que se introduzca un 0*/
    //CON Scanner
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Ingrese un número: ");

        var numero = Integer.parseInt(entrada.nextLine());
        while (numero != 0) {
            if (numero > 0) {
                System.out.print("El número " + numero + " es POSITIVO");
            }else{
                System.out.print("El número " + numero + "es NEGATIVO");
            }
            System.out.print("Ingrese un número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El número " + numero + " finaliza el programa");
    }
}
