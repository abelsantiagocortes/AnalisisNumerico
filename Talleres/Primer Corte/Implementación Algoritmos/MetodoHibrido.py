#Implementación del método Hibrido (Biseccion-Newton) para encontrar las raices de una función dada
import matplotlib
from matplotlib import pyplot
import numpy
import math

def f( x ):
    return math.e ** x - math.pi * x

def fd( x ):
    return math.e ** x - math.pi

def hibrido( a, b ):
    
    it = 0
    tol = 10e-8
    errorX = []
    errorY = []
    c = (a + b) / 2
    
    if c - f(c) / fd(c) > a and c - f(c) / fd(c) < b:
        x = c - f(c) / fd(c)
    else:
        x = (a + b) / 2
    
    while abs(f(x)) > tol:
        
        if it > 0:
            errorX.append( abs(f(x)) )
        it = it + 1
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        
        c = (a + b) / 2
        if c - f(c) / fd(c) > a and c - f(c) / fd(c) < b:
            x = c - f(c) / fd(c)
        else:
            x = (a + b) / 2
        
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
    pyplot.title("Metodo Hibrido Newton-Biseccion: \n Errores en X vs. Errores en Y")
    pyplot.grid()
    pyplot.show()

    cY = numpy.linspace( errorY[0], errorY[len(errorY) - 1], 50 )
    matplotlib.pyplot.plot(cX, cY)
    matplotlib.pyplot.xlabel("Errores X ")
    matplotlib.pyplot.ylabel("Errores Y ")
    matplotlib.pyplot.title("Metodo Hibrido Newton-Biseccion: \n Errores en X vs. Errores en Y")
    matplotlib.pyplot.grid()
    matplotlib.pyplot.show()

#------------------------MAIN------------------------------------------

if __name__ == "__main__":
    hibrido( 0, 1 )
    hibrido( 1, 2 )
