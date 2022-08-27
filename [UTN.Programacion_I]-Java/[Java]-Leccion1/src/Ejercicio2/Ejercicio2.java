package Ejercicio2;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
		/**============CLASE 7 - VIERNES-20/05/2022============*/
        //EJERCICIO 2
        //Hacer un programa que calcule e imprima el salario de un empleado, a partir de sus horas
        //semanales trabajadas y de su salario por hora.
        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese cantidad de horas semanales trabajadas: ");
        int horasSemanales=Integer.parseInt(leer.nextLine());

        System.out.print("Ingrese salario por hora: ");
        float salarioHora=Float.parseFloat(leer.nextLine());

        System.out.println("Su salario es: $"+(horasSemanales*salarioHora));

    }
}
