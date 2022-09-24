package EjercicioCiclos09.Ciclos09;

import javax.swing.*;

/**
 * @author Aguppesce
 */
//PROGRAMACIÓN_II
/*============CLASE 05 - VIERNES-23/09/2022============*/
//Ejercicio 09 con JOptionPane: Pedir el día, mes y año de una fecha e indicar si la fecha es correcta. Suponiendo que todos los meses son de 30 días.
public class Ejercicio09 {
    public static void main(String[] args) {
        int dia, mes, anio;
        boolean bandera = false;
        JOptionPane.showMessageDialog(null, "Ingrese una fecha en el formato: DD/MM/AAAA");
        do {
            dia = Integer.parseInt(JOptionPane.showInputDialog("Ingrese día: "));
            mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese mes: "));
            anio = Integer.parseInt(JOptionPane.showInputDialog("Ingrese año: "));
            if ((dia > 0 && dia <= 30) &&
                    (mes > 0 && mes <= 12) &&
                    (anio > 0 && anio <= 2022)) {
                JOptionPane.showMessageDialog(null, "Fecha: " + dia + "/" + mes + "/" + anio);
                bandera = true;
            } else {
                System.out.println("Formato de fecha incorrecto. Intente de nuevo");
            }
        } while (bandera == false);
    }
}


/*
//SOLUCIÓN CLASE
public static void main(String[] args) {
    int dia = Integer.parseInt(JOptionPane.showInputDialog("Digite el día: "));
    int mes = Integer.parseInt(JOptionPane.showInputDialog("Digite el mes: "));
    int anio = Integer.parseInt(JOptionPane.showInputDialog("Digite el anño: "));
    if((dia != 0) && (dia <= 30)){
        if((mes != 0) && (mes <= 12)){
            if((anio !=0) && (anio <= 2022)){
                    JOptionPane.showMessageDialog(null, "La fecha ingresada es: " + dia + "/" + mes + "/" + anio);
             } else {
                JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
             }
         } else {
            JOptionPane.showMessageDialog(null, "Fecha incorrecta, mes incorrecto");
         }
     } else {
        JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto");
     }
}
*/

