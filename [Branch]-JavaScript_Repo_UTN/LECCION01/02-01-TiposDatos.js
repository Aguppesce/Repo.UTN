//===============CLASE 03 - MARTES-27/09/2022===============

//Tipos de datos en JavaScript
/**
 * La sintaxis en lo que es comentarios es muy similar a la de Java realmente diriamos que es identica
 */


//Tipo String
var nombre = "Ariel"; 
console.log(nombre);
nombre=7;
console.log(nombre);
nombre = 12.3;
console.log(nombre);

//Tipo numérico
var numero = 3000; 
console.log(numero);

//Tipo Object
var objeto = { 
    nombre : "Ariel",
    apellido : "Betancud",
    telefono : "26145678933" 
}

console.log(objeto)

//===============CLASE 04 - MARTES-04/10/2022===============
console.log(typeof nombre)

console.log(typeof numero)

console.log(typeof objeto)

//Tipo de dato boolean
var bandera = true;
console.log(bandera);
console.log(typeof bandera);

//Tipo de dato función
function miFuncion(){    
}

console.log(miFuncion)
console.log(typeof miFuncion)

//Tipo de dato symbol
var simbolo = Symbol("Mi símbolo") //Dentro de este tipo de datos podemos ingresar una cadena
console.log(simbolo);
console.log(typeof simbolo);

//Tipo de dato clase
class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;        
    }
}

console.log(Persona)
console.log(typeof Persona);