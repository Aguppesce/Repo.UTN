package ProyectoCaja.caja;

import java.util.Scanner;

/**
 * @author Aguppesce
 */
//PROGRAMACIÓN_II
/*============CLASE 06 - VIERNES-30/09/2022============*/
public class Caja {
    double ancho;
    double alto;
    double profundidad;

    public Caja() {
    }

    public Caja(double ancho, double alto, double profundidad) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }

    public double volumenCaja(){
        //Fórmula: volumen = ancho * alto * profundidad
        return this.ancho * this.alto * this.profundidad;
    }



}
