package Ejercicio4;

import java.util.Scanner;

public class Ejercicio4 {
    public static void main(String[] args) {

		//=========================CLASE 8 - VIERNES-27/05/2022=========================*/
        
        Scanner leer = new Scanner(System.in);

        System.out.print("Ingrese número 1:");
        int num1=Integer.parseInt(leer.nextInt());
        System.out.print("Ingrese número 2:");
        int num2=Integer.parseInt(leer.nextInt());

        var resultado = (num1>num2) ? "Número 1 es el mayor" : "Número 2 es el mayor";
        System.out.println(resultado);

        //Solución clase
        System.out.print("Digite un número: ");
        int n1 = Integer.parseInt(leer.nextLine());
        System.out.print("Digite otro número: ");
        int n2 = Integer.parseInt(leer.nextLine());
        System.out.print("El número mayor es: ");
        System.out.println(n1 > n2 ? n1 : n2);

    }
}
