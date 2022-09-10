package EjercicioCiclos04.Ciclos04;

import java.util.Scanner;

public class Ciclos04 {
    public static void main(String[] args) {
        //PROGRAMACION_II

        /*============CLASE 03 - VIERNES-09/09/2022============*/

        /*Ejercicio 4: Pedir números hasta que se teclee uno negativo,y mostrar cuántos números se han introducido. Lo hacemos primer con la clase Scanner y luego lo hacemos con la clase JOptionPane*/

        Scanner leer = new Scanner(System.in);
        Integer numero, conteo = 0;

        System.out.println("Para salir ingrese un número negativo");
        System.out.print("Ingrese un número: ");
        numero = Integer.parseInt(leer.nextLine());

        while (numero >= 0) {
            System.out.println("El número " + numero + " es POSITIVO");
            conteo ++;
            System.out.print("Ingrese otro número: ");
            numero = Integer.parseInt(leer.nextLine());
        }
        System.out.println("A ingresado " + conteo + " números que no son negativos");
    }
}
