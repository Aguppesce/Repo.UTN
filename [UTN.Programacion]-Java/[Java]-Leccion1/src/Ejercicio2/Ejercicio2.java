package Ejercicio2;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
		
		//=========================CLASE 7 - VIERNES-20/05/2022=========================*/
        int horasSemanales;
        float salarioHora;
        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese cantidad de horas semanales trabajadas: ");
        horasSemanales=Integer.parseInt(leer.nextLine());

        System.out.print("Ingrese salario por hora: ");
        salarioHora=Float.parseFloat(leer.nextLine());

        System.out.println("Su salario es: $"+(horasSemanales*salarioHora));

    }
}
