//======================= CLASE 08 - MARTES-01/11/2022=======================

//Ampliando el uso de var let y const
/**
 * Con var puedes reasignar en cualquier momento, este forma pate del ambito global. Un error es que se sobreescriba
 */

var nombre = "Ariel";
nombre = "Osvaldo"
console.log(nombre)

function saludar() {
    var nombre = "Natalia";
    console.log(nombre)
}
console.log(nombre); //Aquí no lee el dato en la función

if (true) {
    var edad = 34;
    console.log(edad);//En la función funcionó correctamente, en la estructura if fallí
}
console.log(edad);

/**
 * let: esta puede ser reasignada en cualquier momento la diferencia es que su ambito es de bloque, solo disponible dentro de un bloque de llaves o dentro de una función
 */

function saludar2() {
    let nombre2 = "Ariel";
    console.log(nombre2)
}
console.log(nombre2);

if (true) {
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
if (mes == 1 || mes == 2 || mes == 12) {
    estacion = "Verano";
}
else if (mes == 3 || mes == 4 || mes == 5) {
    estacion = "Otoño";
}
else if (mes == 6 || mes == 7 || mes == 8) {
    estacion = "Invierno";
}
else if (mes == 9 || mes == 10 || mes == 11) {
    estacion = "Primavera";
}
else {
    estacion = "Valor incorrecto"
}
console.log("El valor corresponde a la estación de: " + estacion);

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
if (horaDia >= 6 && horaDia <= 11) {
    mensaje = "Good morning"
}
else if (horaDia >= 12 && horaDia <= 16) {
    mensaje = "Good afternoom";
}
else if (horaDia >= 17 && horaDia <= 19) {
    mensaje = "Good evening";
}
else if (horaDia >= 20 && horaDia <= 23) {
    mensaje = "Good night"
}
else {
    mensaje = "Valor incorecto";
}
console.log(mensaje)

//Estrcutura switch(la sintaxis es igual a Java)
switch (mes) { //N solo se pueden utilizar número, también cadenas
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
console.log("Bienvenido a la estación de: " + estacion)

//================== CLASE 11 - MARTES 22/11/2022=====================

//Evitar repetir tu código
//Dry don't repeat yourself
//let days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"];
let days = "Sábado";
switch (days) {
    case "Lunes":
        console.log("Hoy es: " + days);
        break;
    case "Martes":
        console.log("Hoy es: " + days);
        break;
    case "Miércoles":
        console.log("Hoy es: " + days);
        break;
    case "Jueves":
        console.log("Hoy es: " + days);
        break;
    case "Viernes":
        console.log("Hoy es: " + days);
        break;
    case "Sábado":
        console.log("Hoy es: " + days);
        break;
    case "Domingo":
        console.log("Hoy es: " + days);
        break;
    default:
        console.log("error en el ingreso del día de la semana");
        break;
}

//Esta es la versión mejorada
let days2 = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"];

function getDay(n) {
    if (n < 1 || n > 7) {
        throw new Error("out of range");
    }
    return days2[n - 1]
}
console.log(getDay(5))

//Hacer un ejercicio similar al que esta hecho, pero ahora con los meses del año, debes hacerlo con la estructura switch y luego con la función en la opción mejorada

let month = 11;
switch (month) {
    case 1:
        console.log("Es Enero")
        break;
    case 2:
        console.log("Es Febrero")
        break;
    case 3:
        console.log("Es Marzo")
        break;
    case 4:
        console.log("Es Abril")
        break;
    case 5:
        console.log("Es Mayo")
        break;
    case 6:
        console.log("Es Junio")
        break;
    case 7:
        console.log("Es Julio")
        break;
    case 8:
        console.log("Es Agosto")
        break;
    case 9:
        console.log("Es Septiembre")
        break;
    case 10:
        console.log("Es Octubre")
        break;
    case 11:
        console.log("Es Noviembre")
        break;
    case 12:
        console.log("Es Diciembre")
        break;
    default:
        console.log("Error en el ingreso del mes del año")
        break;
}


let month2 = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Octubre", "Septiembre", "Noviembre", "Diciembre"]

function getMonth(n){
    if(n<1 || n>12){
        throw new Error("out of range")
    }
    return month[n-1]
}
console.log(getMonth(1));