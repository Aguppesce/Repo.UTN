package Ejercicio7;

import java.util.Scanner;

public class Ejercicio7 {

    public static void main(String[] args) {

		//=========================CLASE 9 - VIERNES-03/06/2022=========================*/
		
        Scanner leer = new Scanner(System.in);
        final int salario = 1000;
        int auto;
        float valorAuto,autoComision, porcentajeVenta;

        System.out.print("Ingrese cantidad autos vendidos: ");
        auto = Integer.parseInt(leer.nextLine());
        System.out.print("Ingrese el valor de los autos: ");
        valorAuto = Float.parseFloat(leer.nextLine());

        autoComision=auto*150;
        porcentajeVenta=(valorAuto*auto)*0.05F;
        System.out.println("El salario es de: "+(salario+autoComision+porcentajeVenta));

    }
}
