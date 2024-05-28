from matrix_operations import *
from matrix import *
from QR_decomposition import *
    
def singularity_check(self: Matrix)->None:
    if is_singular(self):
        raise SingularMatrixError('Singular matrix')

def swap_diagonal_zeros(self:Matrix ,row: int, inverse:Matrix)->None:
    if self.__getelem__(row, row) == 0:
        for next_row in range(self.rows()):
            if self.__getelem__(next_row, row) != 0 and next_row != row:
                self.swap_rows(row, next_row)
                inverse.swap_rows(row, next_row)
                break

def division_by_pivot(self: Matrix,pivot: int,row:int,inverse: Matrix)->None:  
    for column in range(self.cols()):
            inverse_newelem = inverse.__getelem__(row, column) / pivot
            inverse.__setelem__(row, column, inverse_newelem)
            newelem = self.__getelem__(row, column) / pivot
            self.__setelem__(row, column, newelem)

def inverse_new_element(row: int, column:int,index:int,self:Matrix,factor:float)->None:
    newelem = (self.__getelem__(column, index) - self.__getelem__(row, index) * factor)
    self.__setelem__(column, index, newelem)
            
def row_subtraction(self:Matrix,row:int,inverse:Matrix)->None:
        for column in range(self.cols()):
            factor = self.__getelem__(column, row)
            if column != row:
                for index in range(self.rows()):
                    inverse_new_element(row,column,index,self,factor)
                    inverse_new_element(row,column,index,inverse,factor)
    
def invert(self:Matrix) -> Matrix:

    singularity_check(self)
    input_matrix = self.copy()
    inverse = Matrix(self.rows(), self.cols())
    inverse.set_to_I()

    for row in range(input_matrix.rows()):
        swap_diagonal_zeros(input_matrix,row,inverse)
        pivot = input_matrix.__getelem__(row, row)
        division_by_pivot(input_matrix,pivot,row,inverse)
        row_subtraction(input_matrix,row,inverse)
    return inverse
