#Matriz 6x6 con numeros aleatorios entre [0, 20] y enteros.
#Condicion > 1000 ------> norm(A) * norm(A^-1)
#Determinar si el metodo converge ------> Radio Espectral : max(valores propios de la matriz de transicion de A)
#Si el radio espectral es menor a 1 entonces el metodo converge

library(pracma)
library(Matrix)
library(base)

diagonal <- function(M){
    M[row(M) != col(M)] <- 0
    return (M)
}
condi <- 0
A <- matrix(c(sample(0:20, 36, replace=T)), nrow=6, byrow=TRUE)
condi <- norm(A) * norm(solve(A))

while( condi < 1000 ){
    A <- matrix(c(sample(0:20, 36, replace=T)), nrow=6, byrow=TRUE)
    condi <- norm(A) * norm(solve(A))
}

print(A)
print(condi)

D <- diagonal(A)
L <- D - tril(A)
U <- D - triu(A)
I <- eye(6)

#Matriz transicion SOR con w = 0
w <- 0
T_sor <- solve((D - w * L)) *((1 - w) * D + w * U)
eigen_sor <- eigen(T_sor)
RE_sor <- max(abs(eigen_sor$values))
if(RE_sor < 1){
    print("El metodo de SOR con w = 0 tiene convergencia. ")
}else{
    print("El metodo de SOR con w = 0 no tiene convergencia. ")
}

#Matriz transicion Jacobi
T_jac <- -(solve(D)) %*% (L + U)
eigen_jac <- eigen(T_jac)
RE_jac <- max(abs(eigen_jac$values))
if(RE_jac < 1){
    print("El metodo de Jacobi tiene convergencia. ")
}else{
    print("El metodo Jacobi no tiene convergencia. ")
}

#Matriz de transicion Gauss-Seidel
T_gs <- (-(solve(D)) %*% U) %*% solve(I + L %*% solve(D))
eigen_gs <- eigen(T_gs)
RE_gs <- max(abs(eigen_gs$values))
if(RE_gs < 1){
    print("El metodo de Gauss-Seidel tiene convergencia. ")
}else{
    print("El metodo de Gauss-Seidel no tiene convergencia. ")
}