package matriz_ejercicio_4;

import java.util.Scanner;

/**
 * @author Aguppesce
 */
/*============CLASE 12 - VIERNES-18/11/2022============*/
public class Matriz_Ejercicio_4 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz[][] = new int [7][7];

        //Llamando a la matriz
        for (int i = 0; i<7; i++){
            for (int j = 0; j<7;j++){
                if(i == j){
                    matriz[i][j] = 1;
                }
                else{
                    matriz[i][j] = 0;
                }
            }
        }

        System.out.println("Matriz Original: ");
        for (int i = 0; i<7; i++){
            for (int j = 0; j<7;j++){
                System.out.print(matriz[j][i]+" ");
            }
            System.out.println();
        }
        System.out.println();
    }
}
