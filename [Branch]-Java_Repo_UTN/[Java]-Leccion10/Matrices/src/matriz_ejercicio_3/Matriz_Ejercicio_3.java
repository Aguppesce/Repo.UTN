package matriz_ejercicio_3;

import java.util.Scanner;

/**
 * @author Aguppesce
 */
/*============CLASE 12 - VIERNES-18/11/2022============*/
public class Matriz_Ejercicio_3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz[][] = new int [3][3];

        System.out.println("Rellenar la matriz: ");
        for (int i = 0; i<3; i++){
            for (int j = 0; j<3;j++){
                System.out.print("Matriz ["+i+"]["+j+"]: ");
                matriz[i][j]=entrada.nextInt();
            }
        }
        System.out.println();

        System.out.println("Matriz Original: ");
        for (int i = 0; i<3; i++){
            for (int j = 0; j<3;j++){
                System.out.print(matriz[j][i]+" ");
            }
            System.out.println();
        }
        System.out.println();

        System.out.println("Matriz Transpuesta: ");
        for (int i = 0; i<3; i++){
            for (int j = 0; j<3;j++){
                System.out.print(matriz[j][i]+" ");
            }
            System.out.println();
        }
        System.out.println();
    }
}
