package EjercicioCiclos05.Ciclos05;

import java.util.Random;
import java.util.Scanner;
//PROGRAMACION_II
/*============CLASE 03 - VIERNES-09/09/2022============*/
/*Ejercicio 5 con Scanner: Realizar un juego para adivinar un número, para ello generar un número aleatorio entre 0-100, y luego ir pidiendo números indicando "es mayor" o "es menor" según sea mayor o menor con respecto a N. El proceso termina cuando el usuario acierta y mostramos el número de intentos hechos*/
public class Ciclos05 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        Random random = new Random();
        int numeroRandom = random.nextInt(10) + 1;
        int contador = 0;
        System.out.println(numeroRandom);
        System.out.print("Ingrese un número: ");
        int numeroUsuario = leer.nextInt();
        while (numeroUsuario != numeroRandom) {
            if (numeroUsuario > numeroRandom) {
                System.out.println("Es mayor al número random");
                contador++;
            } else {
                System.out.println("Es menor al número random");
                contador++;
            }
            System.out.print("Vuelva a intentarlo. Ingrese otro número: ");
            numeroUsuario = leer.nextInt();
        }
        System.out.println("Ha ganado! Números de intentos hechos [" + contador + "]");
    }
}
