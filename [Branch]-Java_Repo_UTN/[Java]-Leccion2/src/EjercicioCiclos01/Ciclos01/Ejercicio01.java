package EjercicioCiclos01.Ciclos01;

import javax.swing.*;

//PROGRAMACION_II
/*============CLASE 2 - VIERNES-01/09/2022============*/
/*Ejercicio 1 con JOptionPane: Leer un número y mostrar su cuadrado, repetir el proceso hasta que s eintroduzca un número negativo*/
public class Ejercicio01 {
    public static void main(String[] args) {
        int numero, cuadrado;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while (numero >= 0) { //Mientras el número sea igual a cero o positivo
            cuadrado = (int) Math.pow(numero, 2);
            System.out.println("El número " + numero + " elevado al cuadrado es: " + cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        }
        System.out.println("El porgrama a finalizado por negativo");
    }
}

