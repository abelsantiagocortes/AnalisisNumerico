#Pag. 142 libro Python
library(pracma)
library(Matrix)
library(base)

diagonal <- function(M){
    M[row(M) != col(M)] <- 0
    return (M)
}
A <- matrix(c(8, 9, 2, 2, 7, 2, 2, 8, 6), nrow=3, byrow=TRUE)
b <- c(69, 47, 68)

D <- diagonal(A)
L <- D - tril(A)
U <- D - triu(A)
I <- eye(3)

#-----------------------Parte a. Determinar Convergencias en los metodos

#Matriz transicion SOR con w = 1
w <- 1
T_sor <- solve((D - w * L)) *((1 - w) * D + w * U)
if( norm(T_sor) > 1 ){
    print("El metodo de SOR no puede asegurar convergencia. ")
}else{
    print("El metodo de SOR puede asegurar convergencia. ")
}

#Matriz transicion Jacobi
T_jac <- -(solve(D)) %*% (L + U)
if( norm(T_jac) > 1 ){
    print("El metodo de Jacobi no puede asegurar convergencia. ")
}else{
    print("El metodo de Jacobi puede asegurar convergencia. ")
}

#Matriz de transicion Gauss-Seidel
T_gs <- (-(solve(D)) %*% U) %*% solve(I + L %*% solve(D))
if( norm(T_gs) > 1 ){
    print("El metodo de Gauss-Seidel no puede asegurar convergencia. ")
}else{
    print("El metodo de Gauss-Seidel puede asegurar convergencia. ")
}

#-----------------------Parte b. Comparar Soluciones
sol_def <- solve(A, b)
sol_opt_gs <- itersolve(A, b, method="Gauss-Seidel")
sol_opt_jac <- itersolve(A, b, method="Jacobi")

print("Solucion del Sistema con solucion por defecto.")
print(sol_def)
cat("Solucion del sistema con solucion G-S con un total de ", sol_opt_gs$iter, " iteraciones.")
print(sol_opt_gs$x)
cat("Solucion del sistema con solucion Jacobi con un total de ", sol_opt_jac$iter, " iteraciones.")
print(sol_opt_jac$x)