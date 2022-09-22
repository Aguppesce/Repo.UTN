package EjercicioCiclos07.Ciclos07;

import java.util.Scanner;

/**
 * @author Aguppesce
 */
public class Ciclos07 {
    //PROGRAMACIÓN_II
    /*============CLASE 04 - VIERNES-16/09/2022============*/
    //Ejercicio 07: Pedir números hasta que se introduzca uno negativo calcular la media.
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        double media = 0.0000D;
        boolean bandera = false;
        Integer numero = 0, contador = 0, acumulador = 0;
        do {
            System.out.printf("Ingrese un número: ");
            numero = leer.nextInt();
            if(numero < 0){
                break;
            }
            acumulador += numero;
            contador++;
        } while (numero > 0);
        System.out.println("Cantidad de números ingresados: " + contador);
        System.out.println("Suma de todos los números ingresados: " + acumulador);
        media = acumulador / contador;
        System.out.println("Media: " + media);
    }
}

//SOLUCIÓN CLASE
/*
public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero = 0, conteo = 0, suma = 0;

        float promedio = 0;
        System.out.printf("Digite un número: ");
        numero = Integer.parseInt(entrada.nextInt());
        while (numero >= 0) { //Mientras el número no sea negativo
            suma += numero;
            conteo ++;
            System.out.printf("Digite otro número: ");
            numero = Integer.parseInt(entrada.nextInt());
        }
        if(conteo == 0){
            System.out.printf("\nError, la división entre cero no existe");
        }else{
            promedio = (float)suma/conteo;
            System.out.println("El promedio es: " + promedio);
        }
    }
 */
