package ProyectoCajaSC.cajaSC;

/**
 * @author Aguppesce
 */
//PROGRAMACIÓN_II
/*============CLASE 06 - VIERNES-30/09/2022============*/
//SOLUCIÓN CLASE

public class CajaSC { //Clase pública caja
    //Atributos (características)
    int ancho;
    int alto;
    int profundo;

    //Métodos y constructores (acciones)
    public CajaSC(){ //Constructor 1 = vacío

    }

    //Constructor con parámetros
    public CajaSC(int ancho, int alto, int profundo) { //Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }

    public int calcularVolumen(){ //Método para calcular
        return ancho * alto * profundo;
    }
}
