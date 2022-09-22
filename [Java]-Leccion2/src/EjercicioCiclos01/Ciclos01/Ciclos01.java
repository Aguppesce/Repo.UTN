package EjercicioCiclos01.Ciclos01;

import java.util.Scanner;

public class Ciclos01 {

    //PROGRAMACION_II

    /*============CLASE 2 - VIERNES-01/09/2022============*/

    /*Ejercicio 1: Leer un número y mostrar su cuadrado, repetir el proceso hasta que s eintroduzca un número negativo*/
    public static void main(String[] args) {

        Scanner leer = new Scanner(System.in);

        int numero, cuadrado;
        System.out.print("Ingrese un número: ");
        numero = Integer.parseInt(leer.nextLine());

        while (numero >= 0) { //Mientras el número sea igual a cero o positivo
            cuadrado = (int) Math.pow(numero, 2);
            System.out.println("El número " + numero + " elevado al cuadrado es: " + cuadrado);
            System.out.print("Digite otro número: ");
            numero = Integer.parseInt(leer.nextLine());
        }
        System.out.println("El porgrama a finalizado por negativo");
    }
}
