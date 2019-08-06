#Implementación del método de Aitken para encontrar las raices de una función dada

from matplotlib import pyplot
import numpy
import math

def f( x ):
    return math.e ** x / math.pi

def aitken( x ):

    it = 0
    errorX = []
    errorY = []
    tol = 10e-8
    x0 = x
    x1 = 0
    x2 = f( x0 )

    while abs(x2 - x1) > tol:
        
        if it > 0:
            errorX.append(abs(x2 - x1))
        it = it + 1
        x0 = x2
        x2 = f(x0)
        x1 = x2
        x2 = f(x1)
        x0 = x2 - (((x2 - x1) ** 2) / (x2 - 2*(x1) + x0 ))
        x2 = f(x0)
        
        if it > 1:
            errorY.append(abs(x2 - x1))
    
    print("La aproximacion de la raiz de la funcion es: ", x2 )
    print("La cantidad de iteraciones que se tuvieron fueron: ", it )

    pol = numpy.polyfit(errorX, errorY, 2)
    pol2 = numpy.poly1d( pol )
    cX = numpy.linspace( errorX[0], errorX[len(errorX) - 1], 50 )
    cY = pol2( cX )
    pyplot.plot( cX, cY )
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Metodo de Aitken: \n Errores en X vs. Errores en Y")
    pyplot.grid()
    pyplot.show()
        
#------------------------MAIN------------------------------------------

if __name__ == "__main__":
    aitken( 1 )
