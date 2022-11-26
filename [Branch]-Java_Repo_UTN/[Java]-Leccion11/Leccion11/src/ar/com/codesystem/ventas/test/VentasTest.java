package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

/**
 * @author Aguppesce
 */
/*===============CLASE 13 - MARTES-25/11/2022===============*/

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);

        Orden orden1 = new Orden();
        //Agregamos proudctos al arreglo
        orden1.agregarProductos(producto1);
        orden1.agregarProductos(producto2);
        orden1.mostrarOrden();

        //Tarea:
        //Crear más objetos de tipo Producto = 10
        Producto producto3 = new Producto("Remera", 5900.00);
        Producto producto4 = new Producto("Medias", 900.00);
        Producto producto5 = new Producto("Buzo", 9900.00);
        Producto producto6 = new Producto("Zapatillas", 39900.00);
        Producto producto7 = new Producto("Sandalias", 10100.00);
        Producto producto8 = new Producto("Camisa", 18500.00);
        Producto producto9 = new Producto("Saco", 59900.00);
        Producto producto10 = new Producto("Corbata", 5900.00);

        //Crear más objetos de tipo Orden = 2
        Orden orden2 = new Orden();
        orden2.agregarProductos(producto3);
        orden2.agregarProductos(producto4);
        orden2.agregarProductos(producto5);
        orden2.agregarProductos(producto6);
        orden2.agregarProductos(producto7);
        orden2.agregarProductos(producto8);
        orden2.agregarProductos(producto9);
        orden2.agregarProductos(producto10);
        orden2.mostrarOrden();

    }

}
