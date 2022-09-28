package EjercicioCiclos09.Ciclos09;

import java.util.Scanner;

/**
 * @author Aguppesce
 */
//PROGRAMACIÓN_II
/*============CLASE 05 - VIERNES-23/09/2022============*/
//Ejercicio 09 con Scanner: Pedir el día, mes y año de una fecha e indicar si la fecha es correcta. Suponiendo que todos los meses son de 30 días.
public class Ciclos09 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int dia, mes, anio;
        boolean bandera = false;
        System.out.println("Ingrese una fecha en el formato: DD/MM/AAAA");
        do {
            System.out.print("Ingrese día: ");
            dia = leer.nextInt();
            System.out.print("Ingrese mes: ");
            mes = leer.nextInt();
            System.out.print("Ingrese año: ");
            anio = leer.nextInt();
            if ((dia > 0 && dia <= 30) &&
                (mes > 0 && mes <= 12) &&
                (anio > 0 && anio <= 2022)) {
                System.out.println("Fecha: " + dia + "/" + mes + "/" + anio);
                bandera = true;
            } else {
                System.out.println("Formato de fecha incorrecto. Intente de nuevo");
            }
        } while (bandera == false);
    }
}

//SOLUCIÓN CLASE
/*
public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    System.out.println("Digite el día");
    int dia = Integer.parseInt(entrada.nextLine());
    System.out.println("Digite el mes");
    int mes = Integer.parseInt(entrada.nextLine());
    System.out.println("Digite el año");
    int año = Integer.parseInt(entrada.nextLine());
    if((dia != 0) && (dia <= 30)){
        if((mes != 0) && (mes <= 12)){
            if((anio !=0) && (anio <= 2022)){
                    System.out.println("La fecha ingresada es: " + dia + "/" + mes + "/" + anio);
             } else {
                System.out.println("Fecha incorrecta, año incorrecto");
             }
         } else {
            System.out.println("Fecha incorrecta, mes incorrecto");
         }
     } else {
        System.out.println("Fecha incorrecta, dia incorrecto");
     }
}
*/