package EjerciciosParaPromedio;

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        /**============CLASE 11 - VIERNES-24/06/2022============*/
        //EJERCICIO 3: Leer 2 números; si son iguales que los multiplique, si el
        //primero es mayor que el segundo que los reste y si no que los sume.

        Scanner leer = new Scanner(System.in);
        System.out.print("Ingrese un número: ");
        int num1 = Integer.parseInt(leer.nextLine());
        System.out.print("Ingrese otro número: ");
        int num2 = Integer.parseInt(leer.nextLine());

        if(num1 == num2){
            System.out.println("Multiplicación: "+(num1*num2));
        }else if( num1 > num2){
            System.out.println("Resta: "+(num1-num2));
        }else{
            System.out.println("Suma: "+(num1-num2));
        }
    }
}
