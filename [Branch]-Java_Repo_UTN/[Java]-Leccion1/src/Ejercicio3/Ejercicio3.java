package Ejercicio3;

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
		/**============CLASE 8 - VIERNES-27/05/2022============*/
        //Sacar área y perímetro de un rectángulo
        //Fórmula: Área = alto*ancho;
        //Fórmula: Perímetro=(alto+ancho)*2;

        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese alto: ");
        float alto= Float.parseFloat(leer.nextLine());
        System.out.print("Ingrese ancho: ");
        float ancho= Float.parseFloat(leer.nextLine());
        System.out.println("El área es: "+(alto*ancho));
        System.out.println("El perímetro es: "+((alto+ancho)*2));

    }
}
