package EjerciciosParaPromedio;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        /**============CLASE 11 - VIERNES-24/06/2022============*/
        //EJERCICIO 1: Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si
        //su proomedio de tres calificaciones es mayor o igual a 70 reprueba en caso contrario.

        Scanner leer = new Scanner(System.in);
        System.out.print("Ingrese nota 1: ");
        float nota1 = Float.parseFloat(leer.nextLine());
        System.out.print("Ingrese nota 2: ");
        float nota2 = Float.parseFloat(leer.nextLine());
        System.out.print("Ingrese nota 3: ");
        float nota3 = Float.parseFloat(leer.nextLine());

        if(((nota1 + nota2 + nota3)/3) <= 70){
            System.out.println("El alumno esta desaprobado con: " + ((nota1 + nota2 + nota3)/3));
        }else{
            System.out.println("El alumno esta aprobado con: " + ((nota1 + nota2 + nota3)/3));
        }
    }
}
