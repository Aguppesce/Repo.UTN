package Clases;

/**
 * @author Aguppesce
 */
public class PruebaPersona {
    //PROGRAMACIÓN_II
    /*============CLASE 04 - VIERNES-16/09/2022============*/
    public static void main(String[] args) {
        Persona persona1 = new Persona(); // Llamamos al constructor
        persona1.nombre = "Ariel"; //El valor hexadecimal normlamente comienza con 0x
        persona1.apellido = "Betancud";
        persona1.obtenerInformacion();

        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.nombre = "Osvaldo";
        persona2.apellido = "Giordanini";
        persona2.obtenerInformacion();
    }
}
