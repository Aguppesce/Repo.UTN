package Ejercicio7;

import java.util.Scanner;

public class Ejercicio7 {

    public static void main(String[] args) {
		/**============CLASE 9 - VIERNES-03/06/2022============*/
		//Una compañía de venta de carros usados, paga a su personal de ventas un salario de $1000
        //mensuales más una comisión de $150 por cada carro vendido, más el 5% del valor de la venta
        //por carro. Cada mes el capturista de la empresa ingresa en la computadora los datos pertinentes.
        //Hacer un programa que calcule e imprima el salario mensual de un vendedor dado.
        //El salario de 1000 lo vamos a manejar como un dato constante, para asignarlo debemos usar la
        //palabra reservada "final"

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
