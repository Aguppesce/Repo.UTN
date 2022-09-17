package EjercicioCiclos06.Ciclos06;

import javax.swing.*;

/**
 * @author Aguppesce
 */
public class Ejercicio06 {
    //PROGRAMACIÓN_II
    /*============CLASE 04 - VIERNES-16/09/2022============*/
    //Ejercicio 06: Pedir números hasta que se teclee un 0, mostrar la suma de todos los números introducidos.
    public static void main(String[] args) {
        Integer numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número"));
        Integer sumarNumeros = 0;
         do {
             sumarNumeros += numero;
             numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número"));
        }while (numero != 0);
        JOptionPane.showMessageDialog(null, "Suma de los números ingresados " + sumarNumeros);
    }
}
