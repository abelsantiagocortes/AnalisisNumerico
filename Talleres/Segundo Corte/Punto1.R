library(pracma)
library(Matrix)

A <- matrix(c(-8.1, -7, 6.123, -2, -1, 4, -3, -1, 0, -1, -5, 0.6, -1, 0.33, 6, 1/2), nrow=4, byrow=TRUE)

diagonal <- function(M){
    M[col(M) != row(M)] <- 0
    return (M)
}

#-----------------------Parte a. Matriz Identidad, de unos y de ceros.

mat_Ones <- ones(4)
mat_Id <- eye(4)
mat_Zeros <- zeros(4)

print("Matriz de Unos.")
print(mat_Ones)
print("Matriz de Ceros.")
print(mat_Zeros)
print("Matriz Identidad.")
print(mat_Id)

#-----------------------Parte b. Metodo SOR

#-> Se comprueba que el determinante de la matriz no sea igual a 0.

if( det(A) == 0 ){
    print("No hay solucion para el problema. Determinante de A igual a 0. ")
}else{
    D <- diagonal(A)
    U <- D - triu(A)
    L <- D - tril(A)
    w <- 1 #Factor de Relajacion

    T <- solve((D - w * L)) * ((1 - w) * D + w * U)
    print("Matriz de Transicion con el metodo SOR. ")
    print(T)
}
