#Problema 5
#Implementación del método de Horner que permite evaluar un polinomio con el número minimo de multiplicaciones y sumas
#Polinomio: 2X⁴-3X²+3X-4 -> X = -2

def horner( x ):
    
    coef = [2, 0, -3, 3, -4]
    res = 0
    
    for i in range(len(coef)):
        res = res * x + coef[i]
    
    print("El resultado del polinomio evaluado en X= ", x, " es igual a: ", res)

if __name__ == "__main__":
    horner( -2 )
