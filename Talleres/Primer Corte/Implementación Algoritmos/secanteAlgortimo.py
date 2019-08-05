import math

# Definición de la Función f(x)
def f(x):
    return math.e ** x - math.pi * x


# Definición de Algoritmo Secante

print("Algortimo Secante")
print("---------------------------------")


def secante(x0, x1):
    dx = abs(x1 - x0)
    iteracion = 0
    tolerancia = 10 ** (-8)

    while dx > tolerancia:
        iteracion = iteracion + 1
        temporal = x1
        x1 = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))
        x0 = temporal
        dx = abs(x1 - x0)
        # Impresión de Iteraciones
        print("#", iteracion, " X= ", x1, "                       F(x)= ", f(x1))

    # Resultado Raices
    print(" ")
    print("Existe raiz en ", x0)
    print("Número de Iteraciones", iteracion)
    print(" ")


# Llamado por intervalos
secante(0, 1)
secante(1, 2)
