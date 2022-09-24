package EjercicioCiclos05.Ciclos05;

import javax.swing.*;
import java.util.Random;
import java.util.Scanner;
//PROGRAMACION_II
/*============CLASE 03 - VIERNES-09/09/2022============*/
/*Ejercicio 5 con JOptionPane: Realizar un juego para adivinar un número, para ello generar un número aleatorio entre 0-100, y luego ir pidiendo números indicando "es mayor" o "es menor" según sea mayor o menor con respecto a N. El proceso termina cuando el usuario acierta y mostramos el número de intentos hechos*/
public class Ejercicio05 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        Random random = new Random();
        int numeroRandom = random.nextInt(10) + 1;
        int contador = 0;
        System.out.println(numeroRandom);
        int numeroUsuario = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        while (numeroUsuario != numeroRandom) {
            if (numeroUsuario > numeroRandom) {
                JOptionPane.showMessageDialog(null, "Es mayor al número random");
                contador++;
            } else {
                JOptionPane.showMessageDialog(null, "Es menor al número random");
                contador++;
            }
            numeroUsuario = Integer.parseInt(JOptionPane.showInputDialog("Vuelva a intentarlo. Ingrese otro número: "));
        }
        JOptionPane.showMessageDialog(null, "Ha ganado! Números de intentos hechos [" + contador + "]");

    }
}
