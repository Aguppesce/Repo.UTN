package Operaciones;

/**
 * @author Aguppesce
 */
public class Aritmetica {
    //PROGRAMACIÓN_II
    /*============CLASE 04 - VIERNES-16/09/2022============*/
    //Atributos de la Clase
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
}
