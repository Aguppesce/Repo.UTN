package EjercicioCiclos03.Ciclos03;

import javax.swing.*;
import java.util.Scanner;

public class Ejercicio03 {
    public static void main(String[] args) {

        //PROGRAMACION_II

        /*============CLASE 03 - VIERNES-09/09/2022============*/

        /*Ejercicio 3: Leer números hasta que se introduzca un cero. Para cada uno indicar si es par o impar. Primero lo haremos con la clase Scanner. Luego con la clase JOptionPane*/

        Scanner leer = new Scanner(System.in);

        var numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        while (numero != 0) {
            if (numero % 2 == 0) {
                JOptionPane.showMessageDialog(null, "El número: " + numero + " es PAR");
            } else {
                JOptionPane.showMessageDialog(null, "El número: " + numero + " es IMPAR");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese de nuevo un número: "));
        }

    }
}
