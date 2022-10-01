package EjercicioCiclos10.Ciclos10;

import java.util.Scanner;

/**
 * @author Aguppesce
 */
//PROGRAMACIÓN_II
/*============CLASE 06 - VIERNES-30/09/2022============*/
//Ejercicio 10 con Scanner: Pedir 10 números y escribir la suma total.
public class Ciclos10 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int numero,acumulador=0;
        for(int i = 0; i < 10; i++){
            System.out.print("Ingrese número para la posición "+(i+1)+": ");
            numero = leer.nextInt();
            acumulador += numero;
        }
        System.out.println("Suma de los números ingresados: " + acumulador);
    }
}

//SOLUCIÓN CLASE
    /*public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int numero, suma = 0;
        for(int i = 1; i <=10; i++){
            System.out.println("Digite un número");
            numero = Integer.parseInt(entrada.nextLine());
            suma += numero;
        }
        System.out.println("\nLa suma de todos los números es: "+suma);
    }*/

