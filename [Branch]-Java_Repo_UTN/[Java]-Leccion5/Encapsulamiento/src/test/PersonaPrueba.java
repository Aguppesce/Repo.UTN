package test;

/**
 * @author Aguppesce
 */

import dominio.Persona;

/*============CLASE 08 - VIERNES-21/10/2022============*/
public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo",57.000, false);

        //Modificar a través de los métodos
        persona1.setNombre("Juan Ignacio");
        //persona.nombre = "Juan Ignacio"; //Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre); //Error
        System.out.println("persona1 su nombre es: " + persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: " + persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: " + persona1.isEliminado());

        //Tarea: Crear otro objeto de tipo Persona, asignar valores de manera inicial y imprimir, luego modificar sus valores y volver a imprimir con los valores nuevos

        Persona persona2 = new Persona("Maria", 68.000, false);

        System.out.println(persona2);
        persona2.setNombre("Valeria");
        persona2.setSueldo(88000.00);
        persona2.setEliminado(true);
        System.out.println(persona2);

        System.out.println("persona2 = " + persona2);
    }
}
