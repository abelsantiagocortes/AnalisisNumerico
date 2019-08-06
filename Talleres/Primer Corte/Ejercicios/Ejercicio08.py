#Algoritmo que encuentra una aproximación a la raiz real de la ecuación: sin(x) = ln(x)
import math
import numpy
from matplotlib import pyplot

def f(x):
    return math.sin(x) - math.log(x)

def raiz( a, b ):

    cont = 0
    tol = 10e-8
    error = []    
   
    while abs( b - a ) > tol:

        c = ( a + b ) / 2
        fa = f( a )
        fc = f( c )
        error.append(abs( b - a ))
        if fc == 0:
            raiz = c
            break
        elif fa * fc < 0:
            b = c
        else:
            a = c
        raiz = c
        
        cont = cont + 1
        
    print("La aproximacion de la raiz de la funcion es: ", raiz )
    print("La cantidad de iteraciones que se tuvieron fueron: ", cont )
    
    x = numpy.linspace( 1, cont, 50 )
    y = numpy.linspace( error[0], error[len(error) - 1], 50 )
    pyplot.plot( x, y )
    pyplot.grid()
    pyplot.show()


if __name__ == "__main__":
    raiz( 2, 3 )
