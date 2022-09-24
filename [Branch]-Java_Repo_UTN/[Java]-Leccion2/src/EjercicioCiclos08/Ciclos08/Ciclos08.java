package EjercicioCiclos08.Ciclos08;

import java.util.Scanner;

/**
 * @author Aguppesce
 */
//PROGRAMACIÓN_II
/*============CLASE 05 - VIERNES-23/09/2022============*/
//Ejercicio 08 con Scanner: Pedir un número N, y mostrar todos los números del 1 al N.
public class Ciclos08 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        System.out.printf("Ingrese un número: ");
        int numero = leer.nextInt();
        int i = 1;
        while(i <= numero){
            System.out.println(i);
            i++;
        }
    }
}

/*
 //SOLUCIÓN CLASE
public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un número: ");
        int numero = Integer.parseInt(entrada.nextInt());
        int i = 1;
        while(i <= numero){
            System.out.println(i);
            i++;
        }
    }
 */
