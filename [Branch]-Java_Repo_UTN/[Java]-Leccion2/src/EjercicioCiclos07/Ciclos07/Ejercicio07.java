package EjercicioCiclos07.Ciclos07;

import javax.swing.*;

/**
 * @author Aguppesce
 */
//PROGRAMACIÓN_II
/*============CLASE 04 - VIERNES-16/09/2022============*/
//Ejercicio 07 con JOptionPane: Pedir números hasta que se introduzca uno negativo calcular la media.
public class Ejercicio07 {
    public static void main(String[] args) {
        double media = 0;
        boolean bandera = false;
        Integer numero = 0, contador = 0, acumulador = 0;
        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número"));
            if(numero < 0){
                break;
            }
            acumulador += numero;
            contador++;
        } while (numero > 0);
        media = acumulador / contador;
        JOptionPane.showMessageDialog(null, "Suma de los números ingresados " + acumulador + "\nCantidad de números ingresados: " + contador + "\nMedia: " + media);
    }

}


/*
//SOLUCIÓN CLASE
public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero = 0, conteo = 0, suma = 0;
        float promedio = 0;

        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: ");
        while (numero >= 0) { //Mientras el número no sea negativo
            suma += numero;
            conteo ++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: ");
        }
        if(conteo == 0){
            JOptionPane.showMessageDialog(null, "Error, la división entre cero no existe");
        }else{
            promedio = (float)suma/conteo;
            JOptionPane.showMessageDialog(null, "El promedio es: " + promedio);
        }
    }
 */