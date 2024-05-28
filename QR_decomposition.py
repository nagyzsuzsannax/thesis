from matrix_operations import *
from typing import Tuple

def calculate_column_norm(input_matrix: Matrix, column: int)->int:
    norm=0.0
    for row in range(input_matrix.rows()):
        elem=input_matrix.__getelem__(row, column)
        norm += elem*elem
    norm = math.sqrt(norm)
    return norm

def normalize_column_inplace(input_matrix: Matrix, column: int, norm: float)->None:
    for row in range(input_matrix.rows()):
        elem=input_matrix.__getelem__(row, column)
        normalized_newelem = elem / norm
        input_matrix.__setelem__(row, column, normalized_newelem)
        
def update_elements(column:int, input_matrix: Matrix)->None:
    for next_column in range(column+1, input_matrix.rows()):
        scalar = 0
        for index in range(input_matrix.rows()):
            a1=input_matrix.__getelem__(index, column)
            a2=input_matrix.__getelem__(index, next_column)
            scalar += a1*a2

        for index in range(input_matrix.rows()):
            b1=input_matrix.__getelem__(index, next_column)
            b2=input_matrix.__getelem__(index, column)
            newelem = b1 - scalar * b2
            input_matrix.__setelem__(index, next_column, newelem)
        
def is_close_to_zero(value, tolerance=1e-9)->bool:
    return abs(value) < tolerance     

def QR_decompose(matrix: Matrix)->Tuple[Matrix,Matrix]:
    Q = matrix.copy()
    tmp = matrix.copy()
    for column in range(matrix.cols()):

        norm=calculate_column_norm(Q,column)
        
        if is_close_to_zero(norm):
            continue
            
        normalize_column_inplace(Q,column,norm)
        update_elements(column, Q)

    inverse_Q = Q.transpose()
    R = multiply(inverse_Q,tmp)
    return Q,R


