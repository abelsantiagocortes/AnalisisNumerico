import math
from matplotlib import pyplot
import numpy

def f( x ):
    return 5 - numpy.e ** x


def riemann( a, b, n ):
    
    it = 1
    gap = (b - a) / n
    x = a + it * gap
    area = 0
    
    while it <= n:
        area = area + f(x) * gap
        it = it + 1
        x = a + it * gap
    
    return area

def calcularArea(a, b, k, n):
    
    sum = 0
    tol = 10e-8
    x0 = riemann(a, b, n)
    x1 = 0
    sum = sum + x0
     
    a = b
    b = b + k
     
    while sum < 2:
    
        x1 = riemann(a, b, n)
        sum = sum + x1
        a = b
        b = b + k
        x0 = x1
    
    # cX = numpy.linspace( -5, 5, 50 )
    # pyplot.plot(cX, f(cX) )
    # pyplot.xlabel("X")
    # pyplot.ylabel("Y")
    # pyplot.title("Grafica de la funcion f(x) = 5 - e^x")
    # pyplot.grid()
    # pyplot.show()
    print("El valor del intervalo derecho b en la suma de Riemann fue de: ", b)

if __name__ == "__main__":
    calcularArea(0, 0.1, 0.001, 100)
