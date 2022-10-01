package ProyectoCaja.caja;

/**
 * @author Aguppesce
 */

//PROGRAMACIÓN_II
/*============CLASE 06 - VIERNES-30/09/2022============*/
/*Ejercicio 1: Crear un proyecto según las especificaciones mostradas a continuación.
La fórmula es: volumen = ancho * alto * profundidad
* */

public class PruebaCaja {
    public static void main(String[] args) {

        Caja caja1 = new Caja();
        caja1.alto = 2;
        caja1.ancho = 3;
        caja1.profundidad = 4;
        System.out.println(caja1.volumenCaja()); //Constructor vacío


        Caja caja2 = new Caja(8,2,9);
        System.out.println(caja2.volumenCaja()); //Constructor con parámetros
    }
}
