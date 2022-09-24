package EjercicioCiclos08.Ciclos08;

import javax.swing.*;

/**
 * @author Aguppesce
 */
//PROGRAMACIÓN_II
/*============CLASE 05 - VIERNES-23/09/2022============*/
//Ejercicio 08 con JOptionPane: Pedir un número N, y mostrar todos los números del 1 al N.
public class Ejercicio08 {
    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        int i = 1;
        while(i <= numero){
            JOptionPane.showMessageDialog(null, i);
            i++;
        }
    }
}

/*
 //SOLUCIÓN CLASE
public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
        int i = 1;
        while(i <= numero){
            JOptionPane.showMessageDialog(null, i);
            i++;
        }
    }
 */