package arreglos_ejercicio_5;

import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

/**
 * @author Aguppesce
 */
/*============CLASE 14 - VIERNES-02/12/2022============*/
/*Ejercicio 5: Leer por teclado dos tablas de 10 números enteros y mezclarlas en una tercera de la forma:
 * El 1° de A
 * El 1° de B
 * El 2° de A
 * El 2° de B
 * ... */

public class Arreglos_EJercicio_5 {
    public static void main(String[] args) {

        Scanner leer = new Scanner(System.in);

        int arreglo1[] = new int[10];
        int arreglo2[] = new int[10];
        int arreglo3[] = new int[20];

        int num, indice1 = 0, indice2 = 0;

        Random rand = new Random();

        System.out.println("Llenar arreglo 1: ");
        for (int i = 0; i < arreglo1.length; i++) {
            System.out.printf("Ingrese valor de posición [" + (i + 1) + "]: ");
            num = leer.nextInt();
            //num= rand.nextInt(10+1);
            arreglo1[i] = num;
        }

        System.out.println("Llenar arreglo 2: ");
        for (int i = 0; i < arreglo1.length; i++) {
            System.out.printf("Ingrese valor de posición [" + (i + 1) + "]: ");
            num = leer.nextInt();
            //num= rand.nextInt(10+1);
            arreglo2[i] = num;
        }

        System.out.println("Llenado de arreglo 3: ");
        for (int i = 0; i < arreglo3.length; i++) {

            if (i % 2 == 0 && indice1 < arreglo1.length - 1) {
                arreglo3[i] = arreglo1[indice1];
                indice1++;
            } else if (indice2 < arreglo2.length - 1) {
                arreglo3[i] = arreglo2[indice2];
                indice2++;
            }
        }

        for (int i = 0; i < arreglo3.length; i++) {
            System.out.printf("[" + arreglo3[i] + "], ");
        }

        /*System.out.println(Arrays.toString(arreglo1));
        System.out.println(Arrays.toString(arreglo2));
        System.out.println(Arrays.toString(arreglo3));*/
    }
}
