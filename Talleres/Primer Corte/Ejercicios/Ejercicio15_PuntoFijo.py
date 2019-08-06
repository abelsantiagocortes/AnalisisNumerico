#Resolver un f(x) = 0 que se obtuvo de una integral mediante el método de punto fijo
import math
from matplotlib import pyplot
import numpy

def f( x ):
    return - math.e ** x + 5 * x - 1

def g( x ):
    return (math.e ** x + 1 ) / 5

def puntoFijo( a, b ):
    
    it = 0
    itMax = 5
    tol = 10e-8
    error = []
    x = (a + b) / 2
    
    while abs(g(x) - x) > tol and it < itMax:
        error.append( abs(g(x) - x) )
        x = g(x)
        it = it + 1
    
    print("La raiz que se encuentra en el intervalo ", a, ", ", b, "es aproximadamente: ", x )
    print("El numero de iteraciones que se obtuvieron: ", it )
    
    cX = numpy.linspace( 1, it, 50 )
    y = numpy.linspace( error[0], error[len(error) - 1], 50)
    pyplot.plot(cX, y )
    pyplot.xlabel("Iteraciones")
    pyplot.ylabel("Error")
    pyplot.grid()
    pyplot.show()

if __name__ == "__main__":
    puntoFijo( 0, 1 )
