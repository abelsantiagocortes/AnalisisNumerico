#Problema 2
#Algoritmo que permite calcular una aproximación de la raiz cuadrada de un número N

def calculoRaiz( N ):
    x = 0.1
    E = 10e-8
    y = (1/2) * (x + (N/x))
    while abs(x - y) > E:
        x = y
        y = (1/2) * (x + (N/x)) 
    print("La raiz cuadrada aproximada del numero ", N, "es: ", y)

if __name__ == "__main__":
    calculoRaiz( 7 )
