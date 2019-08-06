#Problema 1
#Algoritmo que permite calcular el error de redondeo de un número
import math

def truncar( N, dec ):
    return math.floor( N * 10 ** dec ) / 10 ** dec

def error( N, dec ):
    
    it = 0
    NReal = N
    NM = 3 - dec
    
    while NReal > 1:
        NReal = NReal / 10
        it = it + 1
    
    NAprox = truncar( NReal, dec )
    err = (NReal - NAprox) * 10 ** 3
    
    print("El error de redondeo es igual a:", round(err, 2), "* 10 ^", NM )  
  
if __name__ == "__main__":
    error( 536.78, 4 )