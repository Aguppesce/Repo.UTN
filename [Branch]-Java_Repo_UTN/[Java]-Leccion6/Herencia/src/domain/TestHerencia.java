package domain;

import java.util.Date;

/**
 * @author Aguppesce
 */
/*============CLASE 09 - VIERNES-28/10/2022============*/
public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Ariel", 57000.0);
        System.out.println("empleado1 = " + empleado1);


        Date fecha1 = new Date();
        Cliente cliente1 = new Cliente(fecha1,true,"Osvaldo",'M',45,"3 de Febrero 42");

        /*Cliente cliente1 = new Cliente(new Date(),true,"Osvaldo",'M',45,"3 de Febrero 42");*/
        System.out.println(cliente1);
    }
}
