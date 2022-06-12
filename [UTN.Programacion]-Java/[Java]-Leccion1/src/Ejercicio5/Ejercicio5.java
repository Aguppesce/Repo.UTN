package Ejercicio5;

import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {

		//=========================CLASE 9 - VIERNES-03/06/2022=========================*/
        
        Scanner leer = new Scanner(System.in);
        System.out.print("Ingrese nota 1: ");
        float nota1 = Float.parseFloat(leer.nextLine());
        System.out.print("Ingrese nota 2: ");
        float nota2 = Float.parseFloat(leer.nextLine());
        System.out.print("Ingrese nota 3: ");
        float nota3 = Float.parseFloat(leer.nextLine());

        System.out.println("La suma de las notas es: " + (nota1+nota2+nota3));


    }
}
