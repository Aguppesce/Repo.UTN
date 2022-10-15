package Operaciones;

/**
 * @author Aguppesce
 */
public class PruebaAritmetica {
    public static void main(String[] args) {
        //PROGRAMACIÓN_II
        /*============CLASE 05 - VIERNES-23/09/2022============*/

        var a = 10; //Variable local
        int b = 7;
        miMetodo(); //Llamamos al nuevo método
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1 = null; //No se debe utilizar
        aritmetica1.sumarNumeros();
        //Para almacenar un objeto o los atributos se utiliza la memoria heap

        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);

        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = " + resultado);

        /*============CLASE 06 - VIERNES-30/09/2022============*/
        System.out.println("airtmetica1 a: " +aritmetica1.a);
        System.out.println("airtmetica1 b: " +aritmetica1.b);

        Aritmetica aritmetica2 = new Aritmetica(5,8);
        System.out.println("aritmetica2.a = " + aritmetica2.a);

        //aritmetica1 = null; //Estamos limpiando el objeto para que no deje residuos. Esto no se utiliza ya que lo hace automáticamente el garbage collector (recolector de basura) al compilar.

        //System.gc(); //Garbage collector, sirve para limpiar (quitar los residuos del programa). Es innecesario ya que el garbage es muy pesado y no se debe utilizar.

        /*============CLASE 07 - VIERNES-14/10/2022============*/
        Persona persona = new Persona("Ariel","Betancud");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: " + persona.nombre);
        System.out.println("Persona apellido: " + persona.apellido);

    }

    //Modularidad creamos un nuevo método
    public static void miMetodo(){
        /*============CLASE 06 - VIERNES-30/09/2022============*/
        // a = 10;//Una variable esta limitada
        System.out.println("Aquí hay otro método");
    }
}

//Creamos una nueva clase
class Persona {
    /*============CLASE 07 - VIERNES-14/10/2022============*/
    String nombre;
    String apellido;

    Persona (String nombre, String apellido){ //Constructor
        super(); //Llamada al constructor de la clase Padre object
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: " + this);
    }
}

class Imprimir {
    /*============CLASE 07 - VIERNES-14/10/2022============*/
    public Imprimir(){
        super(); //El constructor de la clase padre, para reservar memoria
    }

    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: " + persona);
        System.out.println("Impresión del objeto actual (this): " + this);
    }
}


