package arreglos_ejercicio_3;

import java.util.Scanner;

/**
 * @author Aguppesce
 */
/*============CLASE 11 - VIERNES-11/11/2022============*/
//Ejercicio 3: Leer 5 números por teclado, almacenarlos en un arreglo y a continuación realizar la media de los números positivos, la media de los negativos y contar el número de ceros.
public class Arreglos_Ejercicio_3 {
    public static void main(String[] args) {

        int arreglo[] = new int[5];
        Scanner leer = new Scanner(System.in);
        int numero, negativos = 0, positivos = 0, ceros = 0;

        for (int i = 0; i < arreglo.length; i++) {
            System.out.print("Ingrese un número para la posición [" + i + "]: ");
            numero = leer.nextInt();
            arreglo[i] = numero;
            if (arreglo[i] > 0) {
                positivos++;
            }
            if (arreglo[i] < 0) {
                negativos++;
            }
            if (arreglo[i] == 0) {
                ceros++;
            }
        }

        System.out.println("Media positivos: " + (5 / positivos));
        System.out.println("Media negativos: " + (5 / negativos));
        System.out.println("Cantidad de ceros: " + ceros);


    }
}

//SOLUCIÓN CLASE
//Scanner entrada = new Scanner(System.in);
//    float[] numeros = new float[5];
//    float negativos=0, positivos=0, mediaNegativos, mediaPositivos;
//    int conteo0=0,conteo_negativos=0, conteo_positivos=0;
//        System.out.println("Guardando los datos en el arreglo");
//                for (int i = 0; i < 5; i++) {
//        System.out.print((i+1)+ ". Digite un número: ");
//        numeros[i] = entrada.nextFloat();
//        if(numeros[i]>0){
//        positivos += numeros[i];
//        conteo_positivos++;
//        }
//        else if(numeros[i]<0){
//        negativos += numeros[i];
//        conteo_negativos++;
//        }
//        else{
//        conteo0++;
//        }
//        }
//        if(conteo_positivos == 0){
//        System.out.println("\nNo se puede sacar la media de los positivos");
//        }else {
//        mediaPositivos = positivos/conteo_positivos;
//        System.out.println("\nLa media de los números positivos es: "+mediaPositivos);
//        }
//
//        if(conteo_negativos == 0){
//        System.out.println("\nNo se puede sacar la media de los negativos");
//        }
//        else{
//        mediaNegativos = negativos / conteo_negativos;
//        }
//        System.out.println("La cantidad de ceros es: "+conteo0);
