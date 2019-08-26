library(pracma)
library(Matrix)

A <- matrix(c(-8.1, -7, 6.123, -2, -1, 4, -3, -1, 0, -1, -5, 0.6, -1, 0.33, 6, 1/2), nrow=4, byrow=TRUE)

tril1 <- function(M, k = 0) {
    if (k != 0) {
        M[upper.tri(M, diag = FALSE)] <- 0
    } else {
        M[col(M) >= row(M) + k + 1] <- 0
        M[col(M) == row(M)] <- 0
    }
    return(M)
}

diagonal <- function( M ){
    M[col(M) != row(M)] <- 0
    return (M)
}

#-----------------------Parte a. Modificacion Funcion
print("Matriz Original A.")
print(A)
print("Matriz Modificada.")
X <- tril1(A)
print(X)

#-----------------------Parte b. Obtener la diagonal de una matriz

print("Matriz Original A.")
print(A)
X <- diagonal( A )
print("Matriz Diagonal.")
print(X)




