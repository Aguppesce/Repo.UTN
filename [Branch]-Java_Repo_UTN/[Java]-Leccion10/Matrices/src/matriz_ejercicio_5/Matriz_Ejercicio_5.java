package matriz_ejercicio_5;

import javax.swing.*;
import java.util.Scanner;

/**
 * @author Aguppesce
 */
/*============CLASE 12 - VIERNES-18/11/2022============*/
//Ejercicio 5: Crear y cargar una matriz de tamaño n x m, mostrar la suma de cada fila y de cada columna

public class Matriz_Ejercicio_5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz[][], nFilas, nCol, sumaFilas, sumaCol;
        int posFila, posCol;

        nFilas = Integer.parseInt(JOptionPane.showInputDialog("Digite el número de filas: "));

        nCol = Integer.parseInt(JOptionPane.showInputDialog("Digite el número de columnas: "));

        matriz = new int[nFilas][nCol];
        int filas[] = new int[nFilas];
        int columnas[] = new int[nCol];

        System.out.println("Rellenando la matriz: ");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nCol; j++) {
                System.out.print("Matriz [" + i + "][" + j + "]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }

        System.out.println("Matriz Original: ");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nCol; j++) {
                System.out.print(matriz[j][i] + " ");
            }
            System.out.println();
        }
        System.out.println();

        //Sumando las filas
        posFila = 0;
        for (int i = 0; i < nFilas; i++) {
            sumaFilas = 0;
            for (int j = 0; j < nCol; j++) {
                sumaFilas += matriz[i][j];
            }
            filas[posFila] = sumaFilas;
            posFila++;
        }

        //Sumando las filas
        posCol = 0;
        for (int j = 0; j < nCol; j++) {
            sumaCol = 0;
            for (int i = 0; i < nFilas; i++) {
                sumaCol += matriz[i][j];
            }
            columnas[posCol] = sumaCol;
            posCol++;
        }

        System.out.println("\nLa suma de las filas es: ");
        for (int i = 0; i<nFilas;i++){
            System.out.print(filas[i]+" - ");
        }
        System.out.println();

        System.out.println("\nLa suma de las columnas es: ");
        for (int i = 0; i<nCol;i++){
            System.out.print(columnas[i]+" - ");
        }
        System.out.println();
    }
}
