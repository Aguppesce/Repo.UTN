package Operaciones;

/**
 * @author Aguppesce
 */

//PROGRAMACIÓN_II
/*============CLASE 04 - VIERNES-16/09/2022============*/

public class Aritmetica {

    //Atributos de la Clase. Tienen un alcance superior a una variable local.
    int a;
    int b;

    //Método
    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }

    /*============CLASE 05 - VIERNES-23/09/2022============*/
    public int sumarConRetorno() {
        return this.a + this.b;
    }

    public int sumarConArgumentos(int a, int b){
        this.a = a; //El argumento a se asigna al atributo this.a
        this.b = b; //
        //return a + b;
        return this.sumarConRetorno();
    }

    /*============CLASE 06 - VIERNES-30/09/2022============*/
    //El constructor es un método especial
    public Aritmetica(){ //Constructor 1 vacío. Se genera automáticamente
        System.out.println("Se esta ejecutando este constructor número uno");
    }


    //Estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a, int b){ //Constructor 2. SI creamos un segundo constructor entonces el primero (constructor vacío) deja de existir, por lo que debemos crearlo manualmente
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando este constructor número dos");
    }

    /*Stack y heat es una clasificación de la memoria.
    * Stack tiene que ver con las variables locales, solo almacena la referencia de objeto
    * Heath Trabaja con los objetos y atributos */

}
