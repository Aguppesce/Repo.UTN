package arreglos_ejercicio_4;

import java.util.Scanner;

/**
 * @author Aguppesce
 */
/*============CLASE 14 - VIERNES-02/12/2022============*/
/*Ejercicio 4: Leer 10 números enteros, guardarlos en un arreglo. Debemos mostrarlos en el siguiente orden:
el primero, el último, el segundo, el penúltimo, el tercero, etc.*/

public class Arreglos_Ejercicio_4 {
    public static void main(String[] args) {

        int arreglo[] = new int[10];
        Scanner leer = new Scanner(System.in);
        int num;

        for (int i = 0; i < arreglo.length; i++) {
            System.out.print("Ingrese un número: ");
            num = leer.nextInt();
            arreglo[i] = num;
        }

        for (int i = 0; i < arreglo.length; i++) {
            
        }



    }
}
