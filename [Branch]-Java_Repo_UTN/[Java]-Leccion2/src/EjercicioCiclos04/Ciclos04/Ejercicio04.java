package EjercicioCiclos04.Ciclos04;

import javax.swing.*;
import java.util.Scanner;
//PROGRAMACION_II
/*============CLASE 03 - VIERNES-09/09/2022============*/
/*Ejercicio 4 con JOptionPane: Pedir números hasta que se teclee uno negativo,y mostrar cuántos números se han introducido. Lo hacemos primer con la clase Scanner y luego lo hacemos con la clase JOptionPane*/
public class Ejercicio04 {
    public static void main(String[] args) {
        Integer numero, conteo = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número"));
        while (numero >= 0) {
            JOptionPane.showMessageDialog(null, "El número " + numero + " es POSITIVO");
            conteo ++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro número"));
        }
        JOptionPane.showMessageDialog(null, "A ingresado " + conteo + " números que no son negativos");
    }
}
