package EjercicioCiclos02.Ciclos02;

import javax.swing.*;
import java.util.Scanner;

public class Ciclos02 {
    //PROGRAMACION_II

    /*============CLASE 2 - VIERNES-01/09/2022============*/

    /*Ejercicio 02: Leer un número e indicar si es positivo o negativo. El proceso se repetira hasta que se introduzca un 0*/
    //CON JOptionPane
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);


        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while (numero != 0) {
            if (numero > 0) {
                JOptionPane.showMessageDialog(null,"El número: "+numero+" es POSITIVO");
            }else{
                JOptionPane.showMessageDialog(null,"El número: "+numero+" es NEGATIVO");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        }
        JOptionPane.showMessageDialog(null,"El número " + numero + " finaliza el programa");
    }
}
