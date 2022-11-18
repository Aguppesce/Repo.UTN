package test;

import domain.Persona;

/**
 * @author Aguppesce
 */
/*============CLASE 12 - VIERNES-18/11/2022============*/
public class TestArreglosObject {
    public static void main(String[] args) {
        Persona personas[] = new Persona[2];
        personas[0] = new Persona("Ariel");
        personas[1] = new Persona("Osvaldo");

        System.out.println("personas 0 = " + personas[0]);
        System.out.println("personas 1 = " + personas[1]);
    }
}
