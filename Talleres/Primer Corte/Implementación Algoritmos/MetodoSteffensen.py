#Implementación del método de Steffensen para encontrar las raices de una función dada
from matplotlib import pyplot
import numpy
import math

def f( x ):
    return math.e ** x - math.pi * x

def steffensen( x ):
    
    it = 0
    errorX = []
    errorY = []
    tol = 10e-8
    
    while abs(f(x)) > tol:
        
        if it > 0:
            errorX.append( abs(f(x)) )
        it = it + 1
        x = x - (f(x) ** 2 / (f(x + f(x)) - f(x)))
        if it > 1:
            errorY.append( abs(f(x)) )


    print("La aproximacion de la raiz de la funcion es: ", x )
    print("La cantidad de iteraciones que se tuvieron fueron: ", it )

    pol = numpy.polyfit(errorX, errorY, 2)
    pol2 = numpy.poly1d( pol )
    cX = numpy.linspace( errorX[0], errorX[len(errorX) - 1], 50 )
    cY = pol2( cX )
    pyplot.plot( cX, cY )
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Metodo de Steffensen: \n Errores en X vs. Errores en Y")
    pyplot.grid()
    pyplot.show()

#------------------------MAIN------------------------------------------

if __name__ == "__main__":
    steffensen( 1 )
    steffensen( 2 )
   
