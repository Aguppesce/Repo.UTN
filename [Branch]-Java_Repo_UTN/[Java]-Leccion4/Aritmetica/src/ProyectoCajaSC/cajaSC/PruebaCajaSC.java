package ProyectoCajaSC.cajaSC;


import ProyectoCajaSC.cajaSC.CajaSC;

/**
 * @author Aguppesce
 */
//PROGRAMACIÓN_II
/*============CLASE 06 - VIERNES-30/09/2022============*/
//SOLUCIÓN CLASE

public class PruebaCajaSC {
    public static void main(String[] args) {

        //Variables locales
        int medidaAncho = 3; //Valores ingresados en código duro
        int medidaAlto = 2;
        int medidaProf = 6;

        CajaSC caja1 = new CajaSC(); //Instanciamos el objeto, constructor vacío
        caja1.ancho = medidaAncho; //Le pasamos los valores al objeto
        caja1.alto = medidaAlto;
        caja1.profundo = medidaProf;
        int resultado = caja1.calcularVolumen(); //Llamamos al método

        //Primer resultado
        System.out.println("Resultado volumen de caja 1: " + resultado);

        CajaSC caja2 = new CajaSC(2,4,6);//Llamams al constructor 2 con nuevos argumentos

        //Llamamos con el nuevo objeto al método para un nuevo cálculo
        System.out.println("resultado volumen de caja 2: " +caja2.calcularVolumen());
    }
}
