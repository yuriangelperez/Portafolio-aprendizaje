# abs(numero) da el valor absoluto de un numero
numero_absoluto = -5
print(abs(numero_absoluto))
# round(numero) regresa el redondeo

from math import * 

print(floor(3.7)) # regresa el numero más bajo
print(sqrt(36)) # da la raiz cuadrada de un numero


# LISTAS #

amigos = ["Zoe", "Elias", "Lau", "Kevin", "Santi", "Zoe"] #El indice comienza en 0, "Lau" tiene la posición 2 de la lista
amigos[4] = "Shayen" #si quiero actualizar la 5ta posición
print(amigos[0]) #solo va a imprimir a "Zoe"
print(amigos(-1)) # da desde la ultima parte de la lista, por ejemplo aqui da "Shayen"
print(amigos[1:]) # da los demas datos posteriores a 0, regresa "Elias", "Lau", "Kevin", "Santi"
print(amigos[1:3]) # agarra solo a "Elias" y "Lau"

numeros_de_suerte = [4, 8, 15, 16, 23, 42]

amigos.extend(numeros_de_suerte) # agrega la lista "numeros_de_suerte" al final de la lista "amigos"
amigos.append("Santi") # agrega un elemento al final de la lista
amigos.insert(1, "Cande") # el elemento se va a agregar en la posición 2
amigos.remove("Cande") # elimina el elemento
amigos.clear() # regresa una lisfa vacia
amigos.pop() #elimina el ultimo elemento de la lista
amigos.sort() # ordena la lista en orden alfabético
numeros_de_suerte.reverse() # va a invertir el orden de la lista
print(numeros_de_suerte)

print(amigos.index("Zoe")) # me dice que indice de la lista está "Zoe".
# También se puede usar para saber si un elemento esta en la lista o no

print(amigos.count("Zoe")) # me dice cuantas veces aparece "Zoe" en la lista

amigos2 = amigos.copy() # copia la lista amigos

# DUPLAS #  
coordenadas = (4, 5) # las duplas no pueden ser cambiadas ni modificadas o dará error
print(coordenadas[0])

coordenadas2 = [(4, 5), (6, 7), (80, 34)]

