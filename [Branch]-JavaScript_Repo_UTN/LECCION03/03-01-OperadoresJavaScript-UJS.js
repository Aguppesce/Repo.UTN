//======================= CLASE 07 - MARTES-25/10/2022=======================

//Ejercicio para encontrar números pares e imapres
let parImpar = 7;
if(parImpar % 2 == 0){
    console.log("Es un número PAR");    
}else{
    console.log("Es un número IMPAR")
}

//Ejercicio: es mayor de edad
let edad = 20, adulto = 18;
if(edad >= adulto){
    console.log("Es una persona adulta");
} else{
    console.log("Usted es una persona menor de edad");
}

//======================= CLASE 08 - MARTES-01/11/2022=======================

//Ejercicio: Dentro de un rango
let dentroRango = 5; //Aquí vamos a ir cambiando el valor
let valMin = 0, valMax = 10;
if(dentroRango >= valMin && dentroRango <= valMax){
    console.log("Esta dentro del rango establecido");
}else{
    console.log("Esta fuera del rango establecido");
}

//Hoy ya no se usa var, se utiliza let y const
let nombre2 = "Pedro"
console.log(nombre);

const apellido2 = "Lepes";
// apelldio2 = "Peres";  //Una constante no puede ser modificada
console.log(apellido2);
