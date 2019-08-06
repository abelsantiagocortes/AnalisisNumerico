#Problema 3
#Algoritmo que aproxima el resultado de un polinomio usando el teorema de taylor
#En este ejercicio se utiliza la función f(x)=e^0.5
import math

def aproximacionTaylor():
    
    resReal = math.e ** 0.5
    resAprox = 0.0
    grado = int(input("Digite el grado del polinomio de Taylor. "))
    #x = float(input("Digite el valor de Xo. "))
    x = 0
    
    for i in range(grado):
        resAprox = resAprox + (((math.e ** x) * (0.5 ** i)) / math.factorial(i))
        
    print("El resultado real es igual a: ", round(resReal, 4))
    print("El resultado aproximado es igual a: ", round(resAprox, 4))

if __name__ == "__main__":
    aproximacionTaylor()
