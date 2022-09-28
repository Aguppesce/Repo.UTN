package Operaciones;

/**
 * @author Aguppesce
 */
public class PruebaAritmetica {
    public static void main(String[] args) {
        //PROGRAMACIÓN_II
        /*============CLASE 05 - VIERNES-23/09/2022============*/
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();

        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);

        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = " + resultado);
    }
}
