'''
Parcial 2 de Matematica discreta - Binomio de Newton 

Integrantes:
- Yuriangel Perez
- Zoe Solis
- Lautaro Torres
- Kevin Zapata
- Santino Bravo

Este programa desarrolla binomios del tipo (a + b)^n usando la fórmula del binomio de Newton.
Pide dos términos y un exponente, y muestra la expansión y el resultado simplificado (si es posible).
'''

# Función para calcular el factorial de un número
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Función para calcular la combinatoria
def combinatoria(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Función para separar coeficiente y letras con validación de máximo 2 variables
def separar_coef_var(texto):
    texto = texto.strip()
    if texto == "":
        return 1, ""

    signo = -1 if texto.startswith("-") else 1
    if texto[0] in "+-":
        texto = texto[1:]

    numero = ""
    letras = ""

    for caracter in texto:
        if caracter.isdigit():
            numero += caracter
        elif caracter.isalpha():
            letras += caracter

    # se puede tomar como máximo 2 letras como variables
    letras_max = set(letras)
    if len(letras_max) > 2:
        raise ValueError("Error: Solo se permiten hasta 2 variables como máximo.")

    coef = int(numero) if numero else 1
    return signo * coef, letras

# Función para mostrar potencias correctamente
def potencia_variable(variable, exponente):
    if exponente == 0 or variable == "":
        return ""
    elif exponente == 1:
        return variable
    else:
        return variable + "^" + str(exponente)

# Generar un término completo como 3x^2y
def generar_termino(coef, var1, exp1, var2, exp2):
    letras = ""
    if exp1 > 0:
        letras += var1 * exp1
    if exp2 > 0:
        letras += var2 * exp2

    if letras == "":
        return str(coef)

    letras_contadas = {}
    for letra in letras:
        letras_contadas[letra] = letras_contadas.get(letra, 0) + 1

    texto = str(coef)
    for letra in sorted(letras_contadas):
        exp = letras_contadas[letra]
        if exp == 1:
            texto += letra
        else:
            texto += letra + "^" + str(exp)

    return texto

# Une términos en una expresión
def unir_terminos(lista):
    resultado = ""
    for i, t in enumerate(lista):
        if t.startswith('-'):
            resultado += " - " + t[1:]
        else:
            if i == 0:
                resultado += t
            else:
                resultado += " + " + t
    return resultado

# Expande binomio (a + b)^n
def expandir_binomio(a_texto, b_texto, n):
    a_coef, a_var = separar_coef_var(a_texto)
    b_coef, b_var = separar_coef_var(b_texto)

    print("\nExpresión original: (" + a_texto + " + " + b_texto + ")^" + str(n))
    print("Expansión paso a paso:")

    terminos = []
    resumen = {}

    for k in range(n + 1):
        c = combinatoria(n, k)
        coef = c * (a_coef ** (n - k)) * (b_coef ** k)
        exp1 = n - k
        exp2 = k

        termino = generar_termino(coef, a_var, exp1, b_var, exp2)
        terminos.append(termino)

        clave = ""
        if exp1 > 0:
            clave += a_var * exp1
        if exp2 > 0:
            clave += b_var * exp2

        # si no tiene exponente ni variable, es una constante
        if clave == "":
            clave = "constante"
        else:
            letras_contadas = {}
            for letra in clave:
                letras_contadas[letra] = letras_contadas.get(letra, 0) + 1

            clave_ordenada = ""
            for letra in sorted(letras_contadas):
                exp = letras_contadas[letra]
                if exp == 1:
                    clave_ordenada += letra
                else:
                    clave_ordenada += letra + "^" + str(exp)
            clave = clave_ordenada

        if clave in resumen:
            resumen[clave] += coef
        else:
            resumen[clave] = coef

    print(unir_terminos(terminos))

    print("\nResultado simplificado: ")
    final = []
    for clave in resumen:
        valor = resumen[clave]
        if clave == "constante":
            final.append(str(valor))
        else:
            if valor == 1:
                final.append(clave)
            elif valor == -1:
                final.append("-" + clave)
            else:
                final.append(str(valor) + clave)

    print(unir_terminos(final))

# Entradas del usuario, si da los datos erroneos, vuelve a pedir los datos correctos
while True:
    try:
        a = input("Ingresa el primer término (ej: 2, x, 4y, -xy):\n> ").strip()
        if not a:
            raise ValueError("Error: No puede estar vacío.")
        separar_coef_var(a)
        break
    except ValueError as e:
        print(e)

while True:
    try:
        b = input("Ingresa el segundo término (ej: 3, y, -2x, yx):\n> ").strip()
        if not b:
            raise ValueError("Error: No puede estar vacío.")
        separar_coef_var(b)
        break
    except ValueError as e:
        print(e)

while True:
    n_str = input("Ingresa el exponente (entero no negativo):\n> ").strip()
    if n_str.isdigit():
        n = int(n_str)
        break
    print("Error: El exponente debe ser un número entero no negativo.")

#ejecuta el programa
expandir_binomio(a, b, n)