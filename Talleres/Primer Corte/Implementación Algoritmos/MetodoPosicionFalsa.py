#Implementación del método de Posición Falsa para encontrar las raices de una función dada
from matplotlib import pyplot
import numpy
import math

def f( x ):
    return math.e ** x - math.pi * x

def posFalsa( a, b ):
    
    it = 0
    tol = 10e-8
    errorX = []
    errorY = []
    maxIt = 7
    
    xn = (a * f(b) - b * f(a)) / (f(b) - f(a) )
    errA = xn - a
    errB = b - xn
    
    while max(errA, errB ) > tol and it < maxIt:
        
        if it > 0:
            errorX.append( max(abs(errA), abs(errB)) )
        it = it + 1
        if f(xn) * f(a) > 0:
            a = xn
        else:
            b = xn
        
        xn = (a * f(b) - b * f(a)) / (f(b) - f(a) )
        errA = xn - a
        errB = b - xn
        
        if it > 1:
            errorY.append( max(abs(errA), abs(errB)) )
        
    print("La aproximacion de la raiz de la funcion es: ", xn )
    print("La cantidad de iteraciones que se tuvieron fueron: ", it )

    cX = numpy.linspace( errorX[0], errorX[len(errorX) - 1], 50 )
    cY = numpy.linspace( errorY[0], errorY[len(errorY) - 1], 50 )
    pyplot.plot( cX, cY )
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Metodo de Posicion Falsa: \n Errores en X vs. Errores en Y")
    pyplot.grid()
    pyplot.show()
    
#------------------------MAIN------------------------------------------

if __name__ == "__main__":
    posFalsa( 0, 1 )
    posFalsa( 1, 2 )
