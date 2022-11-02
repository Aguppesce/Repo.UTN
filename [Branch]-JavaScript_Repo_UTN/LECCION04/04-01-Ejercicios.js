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




