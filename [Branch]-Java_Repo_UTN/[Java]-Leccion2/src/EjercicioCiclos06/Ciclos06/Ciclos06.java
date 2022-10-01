package EjercicioCiclos06.Ciclos06;

import java.util.Scanner;
/**
 * @author Aguppesce
 */
//PROGRAMACIÓN_II
/*============CLASE 04 - VIERNES-16/09/2022============*/
//Ejercicio 06 con Scanner: Pedir números hasta que se teclee un 0, mostrar la suma de todos los números introducidos.
public class Ciclos06 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        Integer numero;
        Integer sumarNumeros = 0;
        do {
            System.out.print("Ingrese un número: ");
            numero = leer.nextInt();
            sumarNumeros += numero;
        }while (numero != 0);
        System.out.println("Suma de todos los números ingresados: " + sumarNumeros);
    }
}
