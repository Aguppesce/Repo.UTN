package pasoPorValor;

/**
 * @author Aguppesce
 */
//PROGRAMACIÓN_II
/*============CLASE 06 - VIERNES-30/09/2022============*/
public class PasoPorValor {
    public static void main(String[] args) {
        var valorX = 20;
        System.out.println("valorX = " + valorX);
        cambioValor(valorX);//Solo le enviamos una copia
        System.out.println("valorX = " + valorX);
    }

    public static void cambioValor(int arg1){ //Paramétros por valor
        System.out.println("arg1 = " + arg1);
        arg1 = 15;
    }

}
