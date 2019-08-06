#Implementación del método de Newton para encontrar las raices de una función dada
from matplotlib import pyplot
import numpy
import math

def f( x ):
    return math.e ** x - math.pi * x

def fd( x ):
    return math.e ** x - math.pi

def newton( a, b ):

    x = (a + b) / 2
    it = 0
    tol = 10e-8
    errorX = []
    errorY = []
    
    raiz = x - ( f(x) / fd(x) ) 

    while abs( raiz - x ) > tol:
        if it > 0:
            errorX.append( abs( raiz - x ) )
        it = it + 1
        x = raiz
        raiz = x - ( f(x) / fd(x) ) 
        if it > 1:
            errorY.append( abs( raiz - x ) )
    
    print("La raiz que se encuentra en el intervalo ", a, ", ", b, " es aproximadamente: ", raiz )
    print("El numero de iteraciones que se obtuvieron: ", it )
    
    pol = numpy.polyfit(errorX, errorY, 2)
    pol2 = numpy.poly1d( pol )
    cX = numpy.linspace( errorX[0], errorX[len(errorX) - 1], 50 )
    cY = pol2( cX )
    pyplot.plot( cX, cY )
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Metodo de Newton: \n Errores en X vs. Errores en Y")
    pyplot.grid()
    pyplot.show()
    
#------------------------MAIN------------------------------------------

if __name__ == "__main__":
    newton( 0, 1 )
    newton( 1, 2 )
