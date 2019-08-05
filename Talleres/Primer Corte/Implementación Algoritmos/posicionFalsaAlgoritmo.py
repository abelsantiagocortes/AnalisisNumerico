
import numpy as np
import math



# Definición de la Función f(x)
def f(x):
    y = math.e**x - math.pi * x
    return y
#Definición formula Posicion falsa
def formuPosicionFalsa(x0,x1,iterr):
    x = x0 - ((x1-x0)/(f(x1)-f(x0)))*f(x0)
    iterr+=1
    #Impresion iteraciones
    print('#',iterr,'. X:',x)
    return x,iterr


def PosicionFalsa(x0,x1,numIter,tol):
    iterr=0
    x,iterr = formuPosicionFalsa(x0,x1,iterr)
    while iterr<numIter:
        if f(x)*f(x0) < 0:
            x0 = x
        else:
            x1 = x
        x3,iterr = formuPosicionFalsa(x0,x1,iterr)
        if abs(x3-x) < tol:

            # Resultado Raices
            print(" ")
            print("Existe raiz en: ", x3)
            print("Número de Iteraciones", iterr)
            print(" ")

            break
        x=x3
    if iterr == numIter:
        print('Result not found.\nTry again with more iterations.')
#Main
print("Algortimo Posicion Falsa")
print("---------------------------------")
PosicionFalsa(0,1,100,10e-8)
PosicionFalsa(1,2,100,10e-8)



