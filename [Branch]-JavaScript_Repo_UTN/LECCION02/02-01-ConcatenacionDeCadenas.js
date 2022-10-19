//===============CLASE 06 - MARTES-18/10/2022===============

var nombre = "Jose";
var apellido = "Montes";
var nombreCompleto = nombre + ' ' + apellido; //Primera Concatenación
console.log(nombreCompleto);
var nombreCompleto2 = "Ariel" + " " + "Betancud"; //Segunda Concatenación
console.log(nombreCompleto2);
var juntos = nombre + 219; // Lee de izq a der siguiendo la cadena lee el número como str
console.log(juntos);
juntos = nombre + (78 + 17); // Aquí se puede diferencias a través de los paréntesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido;
console.log(nombre)

