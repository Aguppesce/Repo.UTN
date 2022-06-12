package Ejercicio3;

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
	
		//=========================CLASE 8 - VIERNES-27/05/2022=========================*/
        //Fórmula: Área = alto*ancho;
        //Fórmula: Perímetro=(alto+ancho)*2;

        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese alto: ");
        int alto= Integer.parseInt(leer.nextLine());
        System.out.print("Ingrese ancho: ");
        int ancho= Integer.parseInt(leer.nextLine());
        System.out.println("El área es: "+(alto*ancho));
        System.out.println("El perímetro es: "+((alto+ancho)*2));

    }
}
