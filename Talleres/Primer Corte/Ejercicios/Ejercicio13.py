#Algoritmo que permite calcular una aproximación a la raiz n-esima de un número

def raizN( n, N, x ):
    
    tol = 10e-8
    it = 0
    xn = 1
    
    while abs(xn) > tol:
        
        it = it + 1
        xn = ((N / (x ** (n - 1))) - x ) / n
        x = x + xn

    print("La raiz", n, "-esima del numero", N, "es aproximadamente", x)
    print("Se tuvieron un total de:", it, "iteraciones. ")


if __name__ == "__main__":
    N = float(input("Digite un numero. "))
    n = float(input("Digite el valor de la raiz a calcular. "))
    x = float(input("Digite un valor inicial. "))
    raizN( n, N, x )
