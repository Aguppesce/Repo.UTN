import org.w3c.dom.ls.LSOutput;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class HolaMundo {
        public static void main(String[] args) {
				//=====================================CLASE 1 - VIERNES-08/04/2022=====================================
				/*System.out.println("Hola mundo!");*/
                
				//=====================================CLASE 2 - MIERCOLES-13/04/2022===================================
				/*
                System.out.println("Hola mundo desde Java");
                int miVariable= 10;
                System.out.println(miVariable);
                miVariable=5;
                System.out.println(miVariable);

                //Tipo String
                String miVariableCadena = "Bienvenidos";
                System.out.println(miVariableCadena);
                miVariableCadena = "Sigamos creciendo en programación";
                System.out.println(miVariableCadena);
				*/				
				
				//=====================================CLASE 3 - VIERNES-22/04/2022===================================
				//Var - inferencia de tipos en Java
                /*var miVariableEntera2 = 10;
                var miVariableCadena2 = "Seguimos estudiando";
                System.out.println("miVariableEntera2 = "+miVariableEntera2);
                System.out.println("miVariableCadena2 = "+miVariableCadena2);
                //soutv + tab
                //Para ejecutar Shift + F6 es la tecla máyuscula
                //Reglas para definir una variable en Java

                var usuario="Osvaldo";
                var titulo="Ingeniero";
                var union=titulo + " " + usuario;
                System.out.println("union = " + union);

                var a = 8;
                var b = 4;
                System.out.println(usuario + (a+b));
                //Ejercicio: Caracteres Especiales con Java
                var nombre = "Natalia";
                System.out.println("\nNuevo linea: \n"+nombre);//Diagonal inversa y letra n
                System.out.println("\t\t.:MENU:.");
                System.out.println("Retroseso: \b\b"+nombre);//Caracteres de Retroseso
                System.out.println("Comillas simples: \'"+nombre+"\'");
                System.out.println("Comillas Dobles: \""+nombre+"\"");*/

                //Clase Scanner
                /*Scanner entrada = new Scanner(System.in);
                System.out.println("Digite su nombre: ");
                var usuario2 = entrada.nextLine();
                System.out.println("usuario2 = " + usuario2);
                System.out.println("Escriba el titulo: ");
                var titulo2 = entrada.nextLine();
                System.out.println("Resultado: "+titulo2+" "usuario2);
				
				Scanner entrada = new Scanner(System.in);
				System.out.println("Proporciona el titulo: ");
				String titulo = scanner.nextLine();
				System.out.println("Proporciona el autor: ");
				String autor = scanner.nextLine();
				System.out.println(titulo + " fue escrito por " + autor);
				*/
				
				//=====================================CLASE 4 - VIERNES-29/04/2022===================================
				
				/*byte numEnteroByte = 127; //byte(129) puede superar el límite
                System.out.println("numEnteroByte = " + numEnteroByte);
                System.out.println("Valor mínimo del Byte: "+Byte.MIN_VALUE);
                System.out.println("Valor máximo del Byte: "+Byte.MAX_VALUE);

                short numEnteroShort = (short)32768;
                System.out.println("numEnteroShort = " + numEnteroShort);
                System.out.println("Valor mínimo del Short: "+Short.MIN_VALUE);
                System.out.println("Valor máximo del Short: "+Short.MAX_VALUE);

                int numEnteroInt= 2147483647;//No puede superar el límmite (int)2147483648, pero agregando una L al final lo pasamos a LONG
                System.out.println("numEnteroInt= "+numEnteroInt);
                System.out.println("Valor mínimo del int: "+ Integer.MIN_VALUE);
                System.out.println("Valor máximo del int: "+ Integer.MAX_VALUE);

                long numEnteroLong = 9223372036854775807L
                System.out.println("numEnteroLong: "+numEnteroLong);
                System.out.println("Valor mínimo del long: "+Long.MIN_VALUE);
                System.out.println("Valor máximo del long: "+Long.MAX_VALUE);

                float numFloat = (float)3.4028236E38D;//también se puede usar (float)10,0;
                    //numFloat = 3.4028235E38F
                System.out.println("numFloat = "+numFloat);
                System.out.println("Valor mínimo de float: "+Float.MIN_VALUE);
                System.out.println("Valor mánimo de float: "+Float.MAX_VALUE);

                double numDouble = 1.7976931348623158E308D; //Es el número más grande en JAVA
                     //numDouble = 10;
                System.out.println("numDouble = "+numDouble);
                System.out.println("Valor mínimo de double: "+Double.MIN_VALUE);
                System.out.println("Valor máximo de double: "+Double.MAX_VALUE);*/
		}
}