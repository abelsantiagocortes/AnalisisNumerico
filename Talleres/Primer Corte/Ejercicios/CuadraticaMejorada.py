#Implementacion de una ecuación que mejora la ecuación cuadratica original
import math

def calculoOriginal( a, b, c ):
    
    x0 = (-b - math.sqrt( b**2 - 4*a*c )) / (2*a)
    x1 = (-b + math.sqrt( b**2 - 4*a*c )) / (2*a)
    
    print("Los valores de las raices con la formula original son: Xo -> ", x0, " X1 -> ", x1) 


def calculoMejorado( a, b, c ):
    
    x0 = (2*c) / (-b - math.sqrt( b**2 - 4*a*c ))
    x1 = (2*c) / (-b + math.sqrt( b**2 - 4*a*c ))
    
    print("Los valores de las raices con la formula mejorada son: Xo -> ", x0, " X1 -> ", x1)


if __name__ == "__main__":
    calculoOriginal( 3, 9 ** 12, -3 )
    calculoMejorado( 3, 9 ** 12, -3 )
