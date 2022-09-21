package Ejercicio6;

import java.util.Scanner;

public class Ejercicio6 {
    public static void main(String[] args) {
		/**============CLASE 9 - VIERNES-03/06/2022============*/
		//Guillermo tiene N dólares. Luis tiene la mitad de lo que posee Guillermo. Juan tiene
        //la mitad de lo que poseen Luis y Guillermo juntos. Hacer un programa que calcule e
        //imprima la cantidad de dinero que tienen entre los tres.
        Scanner leer = new Scanner(System.in);
        float dGuille;

        System.out.print("Dolares Guillermo: ");
        dGuille = Float.parseFloat(leer.nextLine());

        System.out.println("Dolares Guillermo: $" + dGuille);
        System.out.println("Dolares Luis: $" + (dGuille/2));
        System.out.println("Dolares Juan: $" + (dGuille+(dGuille/2))/2);
    }
}
