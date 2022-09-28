package Ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
		/**============CLASE 6 - VIERNES-13/05/2022============*/
        //EJERCICIO 1
        //1. Mostrar: Ingrese los siguientes datos del libro
        //2. Digite el nombre del libro
        //3. Digite el ID del libro
        //4. Digite el precio del libro
        //5. Indicar si el envío es gratuito (True/False)
        //6. Mostrar:
        //      Nombre:
        //      ID:
        //      Precio:
        //      Envío Gratuito ?:

        Scanner leer = new Scanner(System.in);
        boolean gratis;

        System.out.print("Envío gratis (S/N)?: ");
        String envioGratuito=leer.nextLine();
        System.out.print("Ingrese nombre del libro: ");
        String nombreLibro=leer.nextLine();
        System.out.print("Ingrese id del libro: ");
        long idLibro=Long.parseLong(leer.nextLine());
        System.out.print("Ingrese precio del libro: ");
        double precioLibro=Double.parseDouble(leer.nextLine());

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

//Respuestas de cuestionario en casa (ver power point clase)
//1. El tipo de datos var a = 0 puede ser de tipo int, tipo byte o tipo short
//2. El rango -32,768 a 32,767 (System.out.println(Short.MIN_VALUE); System.out.println(Short.MAX_VALUE);)
//3. Tiene 8 bytes
//4. 32 bits
//5. Tipo Double
//6. 32 bits