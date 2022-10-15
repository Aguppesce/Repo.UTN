package EjercicioCiclos12.Ciclos12;

import java.util.Scanner;

/**
 * @author Aguppesce
 */
//PROGRAMACIÓN_II
/*============CLASE 07 - VIERNES-14/10/2022============*/
//Ejercicio 12 con Scanner: Pedir un número y calcular su factorial.
public class Ciclos12 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int numero, factorial = 1, guardarNumero = 0;

        System.out.print("Ingrese un número: ");
        numero = Integer.parseInt(leer.nextLine());

        for (int i = 1; i <= numero; i++) {
            factorial = factorial * i;
        }
        System.out.println("Factorial del número ingresado: " + factorial);
    }
}

//SOLUCIÓN CLASE
/*public static void main(String[] args) {
        //Scanner entrada = new Scanner(System.in);
        long factorial = 1;
        //System.out.println("Digite un número: ");
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: ")
        for (int i = 1; i <= numero; i++) {
            factorial *= i;
        }
        //System.out.println("\nEl factorial del número ingresado es: "+factorial);
        JOptionPane.showMessageDialog(null,"El factorial del número ingresado es: "+factorial);
 }*/
