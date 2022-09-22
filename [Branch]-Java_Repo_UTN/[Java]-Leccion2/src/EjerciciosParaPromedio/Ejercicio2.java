package EjerciciosParaPromedio;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        /**============CLASE 11 - VIERNES-24/06/2022============*/
        //EJERCICIO 2: En un almacén se hace un 20% de descuento a los clientes
        //cuya compra supere los $100. ¿Cuál será la cantidad que pagará una persona
        //por su compra?

        Scanner leer = new Scanner(System.in);

        System.out.print("Digite cantidad a pagar: ");
        float compra = Float.parseFloat(leer.nextLine());


        if(compra >= 100){
            float descuento = (compra*0.2F);
            System.out.println("Tiene un descuento de: $" + descuento);
            System.out.println("Total a pagar: $" +(compra - descuento));
        }else{
            System.out.println("No ha obtenido ningún descuento");
        }
    }
}
