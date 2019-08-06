#Implementación del método de Bisección para encontrar las raices de una función dada

from matplotlib import pyplot
import numpy
import math

def f( x ):
    return math.e ** x - math.pi * x

def biseccion( a, b ):

    it = 0
    tol = 10e-8
    c = ( a + b ) / 2
    errorX = []
    errorY = []
    
    if( f(a) * f(c) > 0 ):
        print("El intervalo no sirve para encontrar la raiz. ")
        

    while abs( b - a ) > tol:
        
        c = ( a + b ) / 2
        fa = f( a )
        fc = f( c )
        
        if it > 0:
            errorX.append(abs( b - a ))
            
        it = it + 1
        
        if fc == 0:
            raiz = c
            break
        elif fa * fc < 0:
            b = c
        else:
            a = c
        raiz = c
        
        if it > 1:
            errorY.append(abs( b - a ))
        
    print("La aproximacion de la raiz de la funcion es: ", raiz )
    print("La cantidad de iteraciones que se tuvieron fueron: ", it )

    x = numpy.linspace( errorX[0], errorX[len(errorX) - 1], 50 )
    y = numpy.linspace( errorY[0], errorY[len(errorY) - 1], 50 )
    pyplot.plot( x, y )
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Metodo de Biseccion: \n Errores en X vs. Errores en Y")
    pyplot.grid()
    pyplot.show()


#------------------------MAIN------------------------------------------

if __name__ == "__main__":
    biseccion( 0, 1 )
    biseccion( 1, 2 )
