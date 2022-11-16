//======================= CLASE 08 - MARTES-01/11/2022=======================

//Ampliando el uso de var let y const
/**
 * Con var puedes reasignar en cualquier momento, este forma pate del ambito global. Un error es que se sobreescriba
 */

var nombre = "Ariel";
nombre = "Osvaldo"
console.log(nombre)

function saludar(){
    var nombre = "Natalia";
    console.log(nombre)
}
console.log(nombre); //Aquí no lee el dato en la función

if(true){
    var edad = 34;
    console.log(edad);//En la función funcionó correctamente, en la estructura if fallí
}
console.log(edad);

/**
 * let: esta puede ser reasignada en cualquier momento la diferencia es que su ambito es de bloque, solo disponible dentro de un bloque de llaves o dentro de una función
 */

function saludar2(){
    let nombre2 = "Ariel";
    console.log(nombre2)
}
console.log(nombre2);

if(true){
    let edad2 = 33;
    console.log(edad2);
}
console.log(edad2);

/**
 * const se utiliza para valores constantes que no pueden ser reasignadas
 */

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
fechaNacimiento = 2003;
console.log(fechaNacimiento); //Solo se ejecuta el console anterior

//================== CLASE 10 - MARTES 15/11/2022=====================

//Ejercicio 1: Calcular estación del año
let mes = -1;
let estacion; //Undefined
if(mes == 1 || mes == 2 || mes == 12){
    estacion = "Verano";
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño";
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno";
}
else if(mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
}
else{
    estacion = "Valor incorrecto"
}
console.log("El valor corresponde a la estación de: "+estacion);

//Ejercicio 2: Hora del día
/*
de 6 a 11 nos saluda: Good Morning
de 12 a 16 nos saluda: Good afeternoom
de 17 a 19 nos saluda: Good evening
de 20 a 23 nos saluda: Good night
Trabajaremos con 24 horas
*/
let horaDia = 9;
let mensaje;
if(horaDia >= 6 && horaDia <= 11){
    mensaje = "Good morning"
}
else if(horaDia >= 12 && horaDia <= 16){
    mensaje = "Good afternoom";
}
else if(horaDia >= 17 && horaDia <= 19){
    mensaje = "Good evening";
}
else if(horaDia >= 20 && horaDia <= 23){
    mensaje = "Good night"
}
else{
    mensaje = "Valor incorecto";
}
console.log(mensaje)

//Estrcutura switch(la sintaxis es igual a Java)
switch(mes){ //N solo se pueden utilizar número, también cadenas
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    case 3: case 4: case 5:
        estacion = "Otoño";
        break;
    case 6: case 7: case 8:
        estacion = "Invierno";
        break;
    case 9: case 10: case 11:
        estacion = "Primavera";
        break;
    default:
        estacion = "Valor incorrecto";        
}
console.log("Bienvenido a la estación de: "+ estacion)