#Encontrar en que instante dos coordenadas seran iguales en el intervalo [0, PI/2]

from matplotlib import pyplot
import numpy

def x( t ):
    return 3 * numpy.sin(t)**3 - 1

def y( t ):
    return 4 * numpy.sin(t) * numpy.cos(t)

def h( t ):
    return (3 * numpy.sin(t)**3 - 1) - (4 * numpy.sin(t) * numpy.cos(t))

def interseccion( a, b ):
    
    c = (a + b) / 2
    it = 0
    error = []
    tol = 10e-5
    
    
    while abs( b - a ) > tol:
        
        c = ( a + b ) / 2
        fa = h( a )
        fc = h( c )
        error.append(abs( b - a ))
        if fc == 0:
            raiz = c
            break
        elif fa * fc < 0:
            b = c
        else:
            a = c
        raiz = c
        
        it = it + 1
        
    print("La aproximacion de la raiz de la funcion es: ", raiz )
    print("La cantidad de iteraciones que se tuvieron fueron: ", it )
    
    t = numpy.linspace( 0, numpy.pi/2, 1000 )
    fig = pyplot.figure()
    f = fig.add_subplot(111, projection="polar")
    g = fig.add_subplot(111, projection="polar")
    z = fig.add_subplot(111, projection="polar")
    f.plot(t, x(t), label='Funcion F' )
    g.plot(t, y(t), label='Funcion G' )
    z.plot(t, h(t), label='Funcion H' )
    pyplot.legend(prop = {'size':10}, loc = 'lower right')
    pyplot.show()
    
if __name__ == "__main__":
    interseccion( 0, numpy.pi/2 )
    
