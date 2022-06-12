package Ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
		//=========================CLASE 7 - VIERNES-20/05/2022=========================*/
        Scanner leer = new Scanner(System.in);
        String nombreLibro;
        long idLibro;
        double precioLibro;
        String envioGratuito;
        boolean gratis;

        System.out.print("Envío gratis (S/N)?: ");
        envioGratuito=leer.nextLine();
        System.out.print("Ingrese nombre del libro: ");
        nombreLibro=leer.nextLine();
        System.out.print("Ingrese id del libro: ");
        idLibro=leer.nextLong();
        System.out.print("Ingrese precio del libro: ");
        precioLibro=leer.nextDouble();

        System.out.println("Nombre del libro: "+nombreLibro);
        System.out.println("ID del libro: "+idLibro);
        System.out.println("Precio del libro: $"+precioLibro);

        if(envioGratuito.toUpperCase().equals("S")){
            gratis=true;
            System.out.println("Envío Gratis: " + gratis);
        }else if(envioGratuito.toUpperCase().equals("N")){
            gratis=false;
            System.out.println("Envio Gratis: " + gratis);
        }else{
            gratis=false;
            System.out.println("Opción inválida");
        }
    }
}
//1) El tipo de datos var a = 0 puede ser de tipo int, tipo byte o tipo short
//2) El rango -32,768 a 32,767 (System.out.println(Short.MIN_VALUE); System.out.println(Short.MAX_VALUE);)
//3) Tiene 8 bytes
//4) 32 bits
//5) Tipo Double
//6) 32 bits