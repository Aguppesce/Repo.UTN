package arreglos_ejercicio_1;

import java.util.Scanner;

/**
 * @author Aguppesce
 */
/*============CLASE 11 - VIERNES-11/11/2022============*/
//Ejercicio 1: Leer 5 números, guardarlos en un arreglo y mostrarlos en el mismo orden introducidos.
public class Arreglos_Ejercicio_1 {
    public static void main(String[] args) {

        int arreglo[] = new int[5];
        Scanner leer = new Scanner(System.in);
        int numero;

        for (int i = 0; i < arreglo.length ; i++) {
            System.out.print("Ingrese un número para la posición [" + i + "]: ");
            numero = leer.nextInt();
            arreglo[i] = numero;
        }

        System.out.println("Números según el orden ingresado: ");

        for (int i = 0; i < arreglo.length; i++) {
            System.out.print(arreglo[i] + ", ");
        }

    }
}


//SOLUCIÓN CLASE
//    Scanner entrada = new Scanner(System.in);
//    float[] arreglos = new float[5];
//
//        System.out.println("Guardando los datos en el arreglo");
//                for (int i = 0; i < 5; i++) {
//        System.out.print((i+1)+ ". Digite un número: ");
//        arreglos[i] = entrada.nextFloat();
//        }
//        System.out.println("\nImprimir los elementos del arreglo: ");
//        for (float i: arreglos) {
//        System.out.print(i+" ");
//        }
//        System.out.println("\n");