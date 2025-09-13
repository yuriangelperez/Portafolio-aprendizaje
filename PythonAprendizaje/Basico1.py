# funciones_basicas.py

"""
-------------------------------
 Listas
-------------------------------
"""
amigos = ["Zoe", "Lau", "Elias", "Kevin", "Santi", "Zoe"] # El primer indice es 0, luego 1 es el 2do,...etc
print(amigos)

# Acceder a un elemento
print(amigos[2]) # Me devuelve a "Elias"
print(amigos[-1]) # Me devuelve a "Zoe"
print(amigos[1:]) # Agarra al elemento de esa posición y a los posteriores
print(amigos[1:4]) # Agarra todos los elementos desde el 1 sin incluir el 4

# Cambiar elemento
amigos[4] = "Santino" # Cambia a "Santi" por "Santino"

# Agregar un elemento al final
amigos.append("Shayen")

# Insertar en una posición
amigos.insert(1, "Cande")

# Eliminar por valor
amigos.remove("Cande")

# Eliminar el último (o por índice)
ultimo = amigos.pop() # Elimina a Santi

# Contar elementos de la lista
print(amigos.count("Zoe")) # Me devolverá 2

# Ordenar la lista en orden ascendente
amigos.sort()

# Invierte el orden de la lista
amigos.reverse()

# Buscar indice
print(amigos.index("Elias")) # Me devolverá 2. Tambien sirve para saber si un elemento no está en la lista

# Copiar lista
amigos2 = amigos.copy()

# Eliminar lista
amigos2.clear()

# Extender lista
numeros_suerte = [2, 5, 6, 19, 3, 24]
amigos.extend(numeros_suerte)
print(amigos) # me devuelve la lista de amigos + la de numeros_suerte

"""
-------------------------------
 Duplas (no se pueden modificar)
-------------------------------
"""
colores = ("rojo", "verde", "azul")
print("Tupla de colores:", colores)
print("Primer color:", colores[0])
# colores[1] = "amarillo"  # Esto daría error, no se pueden cambiar

"""
-------------------------------
Conjuntos (sets, no permiten duplicados)
-------------------------------
"""

numeros = {1, 2, 3, 3, 2, 1}
print(numeros) # devuelve los numeros sin duplicados

numeros.add(4) # Añade el 4 a la lista
print(numeros)

numeros.discard(2)
print(numeros) # Quita el numero 2

"""
-------------------------------
Diccionarios
-------------------------------
"""

persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

print("Diccionario de persona:", persona)

# Acceder a un valor
print("Nombre:", persona["nombre"])

# Agregar nueva clave:valor
persona["profesion"] = "Ingeniero"
print("Profesion:", persona)

# Modificar un valor
persona["edad"] = 26
print("Edad:", persona)

# Eliminar una clave
del persona["ciudad"]
print("Ciudad:", persona)

"""
-------------------------------
Funciones propias
-------------------------------
"""

def saludar(nombre):
    return f"¡Hola, {nombre}!"

print(f"Saludo: {saludar(persona['nombre'])}")

def saludo():
    print("Holis")
saludo()

import os
def limpiar():
    os.system("cls")


