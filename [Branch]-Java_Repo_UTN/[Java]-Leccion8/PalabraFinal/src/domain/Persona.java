package domain;

/**
 * @author Aguppesce
 */
/*============CLASE 10 - VIERNES-04/11/2022============*/
public  class Persona {
    public final static int CONSTANTE_AQUI = 15; //Se recomienda que las constantes se escriban en mayúsculas
    private String nombre;
    public void imprimir(){
        System.out.println("Método para imprimir");
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }


}
