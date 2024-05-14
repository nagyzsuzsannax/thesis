from matrix import *
from matrix_operations import *
from QR_decomposition import *
    

def swap_rows_LU(column: int, U: Matrix, L: Matrix,permutations:int):
    max_absolute_value=abs(U.__getelem__(column,column))
    pivot_row=column
    for i in range(column + 1, U.rows()):
        if abs(U.__getelem__(i, column)) > max_absolute_value:
            max_absolute_value = abs(U.__getelem__(i, column))
            pivot_row = i
            
    if pivot_row != column:
        U=U.swap_rows(column,pivot_row)
        L=L.swap_rows(column,pivot_row)
        permutations+=1
    return permutations

        
def singularity_check(self: Matrix):
    if is_singular(self):
        raise SingularMatrixError('Singular matrix')      
        
        
def update_elements_LU(column: int, U: Matrix, L:Matrix):
    for row in range(column + 1, U.rows()):
        multiplier = U.__getelem__(row, column) / U.__getelem__(column, column)
        L.__setelem__(row, column, multiplier)
        for col in range(column, U.cols()):
            U.__setelem__(row, col, U.__getelem__(row, col) - multiplier * U.__getelem__(column, col))
        
def calculate_determinant(U: Matrix,permutation:int):
    determinant=1.0
    for i in range(U.rows()):
        determinant *= U.__getelem__(i, i)
    determinant*=(-1)**(permutation)
    return determinant

def LU_decompose(input_matrix: Matrix,usage:str):
    singularity_check(input_matrix)
    U = input_matrix.copy()
    L = Matrix(input_matrix.rows(), input_matrix.cols())
    L.set_to_I()
    permutations=0

    for column in range(U.cols() - 1):
        if usage=='LUP':
            permutations=swap_rows_LU(column, U, L,permutations)
        L.__setelem__(column,column,1)
        L.__setelem__(column+1,column+1,1)
        update_elements_LU(column, U, L)
        for i in range(column + 1):
            for j in range(i + 1, L.cols()):
                L.__setelem__(i, j, 0)
    
    determinant=calculate_determinant(U,permutations)

    return L, U, determinant
    

    