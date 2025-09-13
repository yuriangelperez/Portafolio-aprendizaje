// funciones básicas

// -------------------------------
// Arrays (listas en JS)
// -------------------------------

// Ya no se usa var ya que puede traer errores
// Es mejor usar let si queremos cambiar las variables, o const si no queremos que se modifique

const suma = 4 + 5;

// funciones matemáticas
let numero = 15;
numero++ // ingrementa en 1
numero-- // disminuye 1
numero += 5 // es igual a decir numero = numero + 5

let amigos = ["Zoe", "Lau", "Elias"];
console.log("Amigos:", amigos);

// Agregar al final
amigos.push("Santi");

// Insertar al principio
amigos.unshift("Kevin");

// Eliminar el último
let ultimo = amigos.pop();
console.log("Amigos:", amigos, " (eliminado:", ultimo, ")");

// Eliminar el primero
let primero = amigos.shift();
console.log("Amigos:", amigos, " (eliminado:", primero, ")");

// Acceder a un elemento
console.log("Primer amigo:", amigos[0]);

// -------------------------------
// Objetos (diccionarios en JS)
// -------------------------------

let persona = {
  nombre: "Yuri",
  edad: 20,
  ciudad: "Buenos Aires"
};

console.log("Objeto de persona:", persona);

// Acceder a un valor
console.log("Nombre:", persona.nombre);

// Agregar nueva propiedad
persona.profesion = "Programadora";
console.log("Persona:", persona);

// Modificar un valor
persona.edad = 21;
console.log("Persona:", persona);

// Eliminar una propiedad
delete persona.ciudad;
console.log("Persona:", persona);

// -------------------------------
// Funciones
// -------------------------------
function saludar(nombre) {
  return `¡Hola, ${nombre}!`;
}

console.log("Saludo:", saludar(persona.nombre));

// -------------------------------
// Funciones arrow
// -------------------------------
const sumar = (a, b) => a + b;
console.log("Suma 5 + 3:", sumar(5, 3));

// -------------------------------
// Set (no permite duplicados)
// -------------------------------
let numeros = new Set([1, 2, 2, 3]);
console.log("Set de números:", numeros);

numeros.add(4);
console.log("Después de add:", numeros);

numeros.delete(2);
console.log("Después de delete:", numeros);

// -------------------------------
// Map (diccionario clave-valor)
// -------------------------------
let capitales = new Map();
capitales.set("España", "Madrid");
capitales.set("Argentina", "Buenos Aires");

console.log("Map capitales:", capitales);
console.log("Capital de España:", capitales.get("España"));