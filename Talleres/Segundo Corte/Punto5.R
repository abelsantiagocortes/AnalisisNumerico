#2x +0y - z = 1                                                                                
#Bx +2y - z = 2                                                                         
#-x + y +Az = 1

library(pracma)
library(Matrix)

x0 <- c(1, 2, 3)

#-----------------------Parte a. Valores de A y B para garantizar convergencia.

#Segun el teorema de convergencia, si una matriz es diagonalmente dominante, entonces es convergente
#Para la primera fila 2 > |0| + |-1|
#Para la segunda fila 2 > |B| + |-1|
#Para la tercera fila A > |-1| + |1|
#Por lo tanto B = 0 y A > 2 para garantizar convergencia

A <- 3
B <- 0

#-----------------------Parte b. 10 iteraciones con el metodo de Jacobi

M <- matrix(c(2, 0, -1, B, 2, -1, -1, 1, A), nrow=3, byrow=TRUE)
b <- matrix(c(1, 2, 1), nrow=3, byrow=TRUE)
it <- 1

while(it <= 10){
    x1 <- itersolve(M, b, x0, nmax=it, method="Jacobi")
    cat("\nIteracion: ", it, "\tResultado: ", x1$x)
    it <- it + 1
}