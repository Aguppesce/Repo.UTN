package EjercicioCiclos03.Ciclos03;

import java.util.Scanner;
//PROGRAMACION_II
/*============CLASE 03 - VIERNES-09/09/2022============*/
/*Ejercicio 3 con Scanner: Leer números hasta que se introduzca un cero. Para cada uno indicar si es par o impar. Primero lo haremos con la clase Scanner. Luego con la clase */

public class Ciclos03 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        System.out.println("Para salir ingrese 0");
        System.out.print("Ingrese un número: ");
        Integer numero = leer.nextInt();
        while(numero!=0){
            if(numero % 2 == 0){
                System.out.println("El número es par");
            } else{
                System.out.println("El número es impar");
            }
            System.out.print("Ingrese de nuevo un número: ");
            numero = leer.nextInt();
        }
    }
}
