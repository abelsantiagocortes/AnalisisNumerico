#Implementación del método de Secante para encontrar las raices de una función dada
from matplotlib import pyplot
import numpy
import math

def f( x ):
    return math.e ** x - math.pi * x

def secante( x0, x1 ):
    
    it = 0
    tol = 10e-8
    errorX = []
    errorY = []
    f0 = f( x0 )
    f1 = f( x1 )
    
    while abs(x1 - x0) > tol:
        
        if it > 0:
            errorX.append( abs(x1 - x0) )
        it = it + 1
        m = (f1 - f0 )/(x1 - x0)
        if m == 0:
            break
        x2 = x1 - f1 / m
        f2 = f( x2 )
        x0 = x1
        x1 = x2
        f0 = f1
        f1 = f2
        
        if it > 1:
            errorY.append( abs(x1 - x0) )
   

    print("La aproximacion de la raiz de la funcion es: ", x2 )
    print("La cantidad de iteraciones que se tuvieron fueron: ", it )

    pol = numpy.polyfit(errorX, errorY, 2)
    pol2 = numpy.poly1d( pol )
    cX = numpy.linspace( errorX[0], errorX[len(errorX) - 1], 50 )
    cY = pol2( cX )
    pyplot.plot( cX, cY )
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Metodo de Secante: \n Errores en X vs. Errores en Y")
    pyplot.grid()
    pyplot.show()

#------------------------MAIN------------------------------------------

if __name__ == "__main__":
    secante( 0, 1 )
    secante( 1, 2 )
