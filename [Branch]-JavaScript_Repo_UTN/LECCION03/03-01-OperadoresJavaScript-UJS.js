//======================= CLASE 07 - MARTES-25/10/2022=======================

//Ejercicio para encontrar números pares e imapres
let parImpar = 7;
if (parImpar % 2 == 0) {
    console.log("Es un número PAR");
} else {
    console.log("Es un número IMPAR")
}

//Ejercicio: es mayor de edad
let edad = 20, adulto = 18;
if (edad >= adulto) {
    console.log("Es una persona adulta");
} else {
    console.log("Usted es una persona menor de edad");
}

//======================= CLASE 08 - MARTES-01/11/2022=======================

//Ejercicio: Dentro de un rango
let dentroRango = 5; //Aquí vamos a ir cambiando el valor
let valMin = 0, valMax = 10;
if (dentroRango >= valMin && dentroRango <= valMax) {
    console.log("Esta dentro del rango establecido");
} else {
    console.log("Esta fuera del rango establecido");
}

//Hoy ya no se usa var, se utiliza let y const
let nombre2 = "Pedro"
console.log(nombre);

const apellido2 = "Lepes";
// apelldio2 = "Peres";  //Una constante no puede ser modificada
console.log(apellido2);

//======================= CLASE 09 - MARTES-08/11/2022=======================
// Ejercicio: Si el padre puede asistir al juego de su hijo

let vacaciones = false, diaDescanso = false;
if (vacaciones || diaDescanso) {
    console.log("El padre puede asistir al juego de su hijo")
} else {
    console.log("El padre no puede asistir al juego de su hijo")
}

//Operador ternario
let resultado2 = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado2);

let numero = 9;
resultado2 = numero % 2 == 0 ? "Es un número PAR" : "Es un número IMPAR"
console.log(resultado2);

//Convertir String a Number
let miNumero = "10"; //Es una cadena
console.log(typeof miNumero);

let edad2 = Number(miNumero)//Number es una función que convierte un String en un número
console.log(typeof edad2);

//Función isNaN
if (isNaN(edad)) { //No es número = is Not a Number (devuelve un resultado booleano)
    console.log("Esta variable no contiene solo números");
} else {
    if (edad2 >= 18) {
        console.log("Puede votar");
    }
    else {
        console.log("Muy joven para votar");
    }
}

let resultado3 = edad2 >= 18 ? "Puede votar" : "Muy joven para votar";
console.log(resultado3);
