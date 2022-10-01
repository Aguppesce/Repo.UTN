package EjercicioCiclos10.Ciclos10;

import javax.swing.*;

/**
 * @author Aguppesce
 */
//PROGRAMACIÓN_II
/*============CLASE 06 - VIERNES-30/09/2022============*/
//Ejercicio 10 con JOptionPane: Pedir 10 números y escribir la suma total.
public class Ejercico10 {
    public static void main(String[] args) {
        int numero,acumulador=0;
        for(int i = 0; i < 10; i++){
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número para la posición "+(i+1)+": "));
            acumulador += numero;
        }
        JOptionPane.showMessageDialog(null,"Suma de los números ingresados: " + acumulador);
    }
}

//SOLUCIÓN CLASE
    /*public static void main(String[] args) {
        int numero,suma=0;
        for(int i = 1; i <= 10; i++){
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número "+(i+1)+": "));
            suma += numero;
        }
        JOptionPane.showMessageDialog(null,"La suma de todos los números es: " + suma);
    }*/
