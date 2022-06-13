public class Leccion1 {
        public static void main(String[] args) {
				//=====================================CLASE 1 - VIERNES-08/04/2022=====================================
				/*System.out.println("Hola mundo!");*/
                
				//=====================================CLASE 2 - MIERCOLES-13/04/2022===================================
                /*System.out.println("Hola mundo desde Java");
                int miVariable= 10;
                System.out.println(miVariable);
                miVariable=5;
                System.out.println(miVariable);

                //Tipo String
                String miVariableCadena = "Bienvenidos";
                System.out.println(miVariableCadena);
                miVariableCadena = "Sigamos creciendo en programación";
                System.out.println(miVariableCadena);*/
				
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
				
				//=====================================CLASE 5 - VIERNES-06/05/2022===================================
				//Inferencia de tipos VAR y tipos primitivos
                /*var numEntero =  20; //Las literales sin punto automáticamente son de tipo int
                System.out.println("numEntero = " + numEntero);
                var numFloat = 10.0F; //Automáticamente con el punto se transforma en tipo double
                System.out.println("numFloat = " + numFloat);
                var numDouble = 10.0;
                System.out.println("numDouble = " + numDouble);*/

                //Tipos primitivos CHAR
                /*char miVariableChar = 'a';
                System.out.println("miVariableChar = " + miVariableChar);
                
                char varCaracter = '\u0024'; //Indicamos a Java la asignación con el código unicode
                System.out.println("varCaracter = " + varCaracter);
                char varCaracterDecimal = 36; //Valor decimal del juego de caracter UNICODE
                System.out.println("varCaracterDecimal = " + varCaracterDecimal);
                char varCaracterSimbolo = '$';//Un caracter especial, podemos copiar y pegar desde unicode
                System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);

                //Var es una variable de inferencia de tipo
                var varCaracter1 = '\u0024'; //Indicamos a Java la asignación con el código unicode
                System.out.println("varCaracter = " + varCaracter1);
                var varCaracterDecimal1 = (char)36; //Valor entero y le asigna un tipo int //Con (char)36 lo convertimos a simbolo
                System.out.println("varCaracterDecimal = " + varCaracterDecimal1);
                var varCaracterSimbolo1 = '$';//Un caracter especial, podemos copiar y pegar desde unicode
                System.out.println("varCaracterSimbolo = " + varCaracterSimbolo1);

                int varEnteroChar = '$';
                System.out.println("varEnteroChar = " + varEnteroChar);
                int caracterChar = 'b';
                System.out.println("caracterChar = " + caracterChar);*/
				
				//=========================CLASE 6 - VIERNES-13/05/2022=========================*/
                //Tipos primitivos tipos booleanos
                /*boolean varBool = true;
                System.out.println("varBool = " + varBool);

                if(varBool){
                        System.out.println("La bandera es verde");
                }
                else{
                        System.out.println("La bandera es roja");
                }

                //Algoritmo ¿Es mayor de edad?
                var edad = 15; //Literal tener presente la inferencia de tipos
                //var adulto = edad >= 18; //Es es una expresión booleana

                if(edad <= 18){
                        System.out.println("Eres mayor de edad");
                }
                else{
                        System.out.println("Eres menor de edad");
                }*/
                
                //Conversión de tipos primitivos
                /*var edad = Integer.parseInt("20");
                System.out.println("edad = " + (edad+1));
                var valorPI = Double.parseDouble("3.1416");
                System.out.println("valorPI = " + valorPI);

                //Pedir un valor
                var entrada = new Scanner(System.in);
                System.out.println("Digite su edad: ");
                edad = Integer.parseInt(entrada.nextLine());
                System.out.println("edad = " + edad);*/

                //Conversión de tipos primitivos en Java Parte 2
                /*var edadTexto = String.valueOf(10);
                System.out.println("edadTexto = " + edadTexto);
                
                var fraseChar = "programadores".charAt(4);
                System.out.println("fraseChar = " + fraseChar);

                System.out.println("Digite un caracter: ");
                var entrada = new Scanner(System.in);
                fraseChar = entrada.nextLine().charAt(0);
                System.out.println("fraseChar = " + fraseChar);*/

                //Para saber que tipo de variable es
                /*var a = 0;
                System.out.println("La variable a es de tipo: " + (((Object)a).getClass().getSimpleName()));*/
				
				//=========================CLASE 7 - VIERNES-20/05/2022=========================*/
                /*int num1 = 5, num2 = 4;
                var solucion = num1 + num2;
                System.out.println("solucion de la suma = " + solucion);

                solucion = num1 - num2;
                System.out.println("solucion de la resta = " + solucion);

                solucion = num1 * num2;
                System.out.println("solucion de la multiplicación = " + solucion);

                solucion = num1 / num2;
                System.out.println("solucion de la división = " + solucion);

                var solucion2 =  3.4 / num2;
                System.out.println("solución2 resultado de la división = " + solucion2);

                solucion = num1 % num2; //Guarda el residuo entero de la división
                System.out.println("solución = " + solucion);// 5/4

                if(num1 % 2 == 0)
                        System.out.println("Es un número Par");
                else
                        System.out.println("Es un número Impar");
                
                int varNum1 = 1, varNum2 = 4;
                int varNum3 = varNum1 + 6 - varNum2; //Una operación
                System.out.println("varNum3 = " + varNum3);

                varNum1 += 1;
                System.out.println("varNum1 = " + varNum1);
                varNum2 -= 2;
                System.out.println("varNum2 = " + varNum2);
                varNum1 *= 5;
                System.out.println("varNum1 = " + varNum1);
                varNum3 /= 4;
				System.out.println("varNum3 = " + varNum3);
                varNum1 %= 6;
                System.out.println("varNum1 = " + varNum1);*/
				
				//=========================CLASE 8 - VIERNES-27/05/2022=========================*/
                //Operadores Unarios: Cambio de Signo
                /*var varA = 7;
                var varB = -varA;
                System.out.println("varA = " + varA);
                System.out.println("varB = " + varB);//El resultado será un número negativo

                //Operador de negación
                var varC = true; //Esta literal por default en Javba es de tipo boolean
                var varD = !varC;//Aquí invirtiendo el valor
                System.out.println("varC = " + varC);
                System.out.println("varD = " + varD);

                //Operadores Unarios de Incremento: Preincremento
                var varE = 9;//Se va a modificar su valor
                var varF = ++varE;//Símbolo antes de la variable
                //Primero se incrementa la variable y después se usa su valor
                System.out.println("varE = " + varE);//Se incrementa en la unidad
                System.out.println("varF = " + varF);//Va a sumar uno

                //Postincremento (el símbolo va a después de la variable)
                var varG = 3;
                var varH = varG++;//Primero el valor de la variable, luego el incremento
                System.out.println("varG = " + varG);
                System.out.println("varH = " + varH);

                //Operadores Unarios de decremento
                var varI = 4;
                var varJ = --varI;
                System.out.println("varI = " + varI);//La variable ya esta con decremento
                System.out.println("varJ = " + varJ);

                //Postdecremento
                var varK = 8;
                var varL = varK--;//Primero el valor de la variable, luego queda el decremento
                System.out.println("varK = " + varK);//Aquí va a decrementar en 1
                System.out.println("varL = " + varL);

                var aNum = 5;
                var bNum = 4;
                var cNum = (aNum == bNum);
                System.out.println("cNum = " + cNum);
                
                var dNum = aNum != bNum;
                System.out.println("dNum = " + dNum);
                
                var cadenaA = "Hello";
                var cadenaB = "bye bye";
                var cVar = cadenaA == cadenaB;
                System.out.println("cVar = " + cVar);
                
                var fVar = cadenaA.equals(cadenaB);
                System.out.println("fVar = " + fVar);

                var gVar = aNum <= bNum;
                System.out.println("gVar = " + gVar);

                if (aNum % 2 == 0){
                        System.out.println("El número es Par");
                } else {
                        System.out.println("El número es Impar");
                }

                var edad = 30;
                var adulto = 18;
                if(edad <= adulto){
                        System.out.println("Es mayor de edad");
                } else {
                        System.out.println("Es menor de edad");
                }*/

                /*var valorA = 7;
                var valorMinimo = 0;
                var valorMaximo = 10;
                var respuesta = valorA >= 0 && valorA <10;

                if(respuesta)
                        System.out.println("Esta dentro del rango establecido");
                else
                        System.out.println("Esta fuera del rango establecido");

                var vacaciones = false;
                var diaLibre = false;
                if(vacaciones || diaLibre)
                        System.out.println("Papá puede asistir al juego de su hijo");
                else
                        System.out.println("Papá no puede asistir al juego de su hijo");*/

                //Operador Ternario
                /*var resultadoT = (5>4) ? "Verdadero" : "Falso";
                System.out.println("resultadoT = " + resultadoT);

                var numeroT = 7;
                resultadoT = (numeroT % 2 == 0) ? "Es par" : "Es impar";
                System.out.println("resultadoT = " + resultadoT);

                var x = 5;
                var y = 10;
                var z = ++x + y--;
                System.out.println("x = " + x);
                System.out.println("z = " + z);
                System.out.println("y = " + y);

                var solucionAritmetica = 4 + 5 * 6 / 3;
                System.out.println("solucionAritmetica = " + solucionAritmetica);

                solucionAritmetica = (4 + 5) * 6 / 3;
                System.out.println("solucionAritmetica = " + solucionAritmetica);*/

                //=========================CLASE 9 - VIERNES-03/06/2022=========================*/
                //EJERCICIOS: 5,6 Y 7

            //=========================CLASE 10 - VIERNES-27/05/2022=========================*/

		}
}