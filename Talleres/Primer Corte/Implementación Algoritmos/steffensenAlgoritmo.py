import math

# Definición de la Función f(x)
def f(x):
    return math.e ** x - math.pi * x


# Definición de Algoritmo Steffensen

print("Algortimo Steffensen")
print("---------------------------------")


def steffensen(p0):
    tolerancia = 0.000001
    r = 10000
    iteracion=0

    for iteracion in range(1, r):
        p1 = p0 + f(p0)
        p2 = p1 + f(p1)

        p = p2 - (pow((p2 - p1), 2) / (p2 - (2 * p1) + p0))

        # Impresión de Iteraciones
        print("#", iteracion, " X= ", p0, "                       F(x)= ", f(p0))

        if abs(p - p0) < tolerancia:
            # Resultado Raices
            print(" ")
            print("Existe raiz en ", p)
            print("Número de Iteraciones", iteracion)
            print(" ")
            return
        p0 = p

# Llamado por intervalos
steffensen(1)
steffensen(2)





