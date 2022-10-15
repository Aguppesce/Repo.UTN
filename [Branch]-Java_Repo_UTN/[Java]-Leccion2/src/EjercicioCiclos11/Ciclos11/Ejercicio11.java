package EjercicioCiclos11.Ciclos11;

import javax.swing.*;

/**
 * @author Aguppesce
 */
//PROGRAMACIÓN_II
/*============CLASE 07 - VIERNES-14/10/2022============*/
//Ejercicio 11 con JOptionPane: Diseñar un programa que muestre el producto de los 10 primero números impares.
public class Ejercicio11 {
    public static void main(String[] args) {
        int i = 0, contador = 0, producto = 1;
        while (contador < 10) {
            if (i % 2 != 0) {
                producto *= i;
                contador++;
            }
            i++;
        }
        JOptionPane.showMessageDialog(null, "Producto de los primeros 10 números impares: " + producto);
    }
}

//SOLUCIÓN CLASE
/*public static void main(String[] args) {
        long producto=1;
        for(int i = 1; i <= 20; i+=2){
            producto *= i;
        }
        JOptionPane.showMessageDialog(null,"El producto de los números impares es: " + producto);
 }*/
