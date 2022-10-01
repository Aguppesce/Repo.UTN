package pasoPorReferencia;

import Clases.Persona;

/**
 * @author Aguppesce
 */
//PROGRAMACIÓN_II
/*============CLASE 06 - VIERNES-30/09/2022============*/
public class PasoPorReferencia {
    //Paso por referencia
    public static void main(String[] args) {
        Persona persona1 = new Persona();

        persona1.nombre = "Ester";

        System.out.println("persona1.nombre = " + persona1.nombre);

        cambiarValor(persona1);

        System.out.println("El cambio que hicimos en el nombre es: " + persona1); //Memoria heap en donde se esta almacenando (persona1)

        System.out.println("El cambio que hicimos en el nombre es: " + persona1.nombre); //Actuamos sobre la memoria heap cambiando el nombre del objeto

        Persona persona2 = new Persona();
        persona2 = cambiarElValor(persona2);
        //Persona persona2 = null;
        System.out.println("El nuevo valor del objeto es: "+persona2.nombre);
    }

    public static void cambiarValor(Persona persona){ //Parámetro por referencia
        persona.nombre = "Maria";
    }

    public static Persona cambiarElValor(Persona persona){
        if(persona == null){
            System.out.println("Valor de persona es inválido: Null");
            return null;
        }else {
            persona.nombre = "Monica";
            return persona;
        }
    }
}
