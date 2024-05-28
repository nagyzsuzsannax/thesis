from matrix import *
import numpy as np

def addition_calculate(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    result = Matrix(matrix1.rows(), matrix1.cols())
    for i in range(matrix1.rows()):
        for j in range(matrix1.cols()):
            value = matrix1.__getelem__(i, j) + matrix2.__getelem__(i, j)
            result.__setelem__(i, j, value)
    return result
    
def add(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    if matrix1.cols() != matrix2.cols() or matrix1.rows() != matrix2.rows():
        raise MatrixIncompatibilityError("Incompatible dimensions")
    return addition_calculate(matrix1,matrix2)  

def subtraction_calculate(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    result = Matrix(matrix1.rows(), matrix1.cols())

    for i in range(matrix1.rows()):
        for j in range(matrix1.cols()):
            value = matrix1.__getelem__(i, j) - matrix2.__getelem__(i, j)
            result.__setelem__(i, j, value)
    return result

def subtract(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    if matrix1.cols() != matrix2.cols() or matrix1.rows() != matrix2.rows():
        raise MatrixIncompatibilityError("Incompatible dimensions")
    return subtraction_calculate(matrix1,matrix2)

def multiplication_calculate(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    result = Matrix(matrix1.rows(), matrix2.cols())
    for row in range(matrix1.row_number):
        for column in range(matrix2.cols()):
            element = 0
            for index in range(matrix1.cols()):
                element += matrix1.__getelem__(row, index) * matrix2.__getelem__(index, column)
            result.__setelem__(row, column, element)
    return result   

def multiply(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    if matrix1.cols() != matrix2.rows():
        raise MatrixIncompatibilityError("Incompatible dimensions")
    return multiplication_calculate(matrix1,matrix2)

def is_singular(input:Matrix)->bool:
    is_singular=np.linalg.matrix_rank(input.matrix)!=input.cols()
    return is_singular
    