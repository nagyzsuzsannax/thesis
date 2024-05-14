import math 

class MatrixError(Exception):
    pass

class MatrixIncompatibilityError(MatrixError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
class ConvergenceError(MatrixError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NonSquareMatrixError(MatrixError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
class AssymmetricMatrixError(MatrixError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)   
            
class DefinicyError(MatrixError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)   
        
class SingularMatrixError(MatrixError):
    def __init__(self, message):
        self.message=message
        super().__init__(self.message)
     
class Matrix:
    def __init__(self, number_of_rows: int, number_of_columns: int, matrix=None):

        self.row_number = number_of_rows
        self.column_number = number_of_columns
        self.matrix = []
        if matrix is None:
            for i in range(number_of_rows):
                number_of_rows = [0.0] * number_of_columns
                self.matrix.append(number_of_rows)
        else:
            if len(matrix) != number_of_rows or any(
                len(row) != number_of_columns for row in matrix
            ):
                raise ValueError("Invalid dimensions for the initial array")
            self.matrix = matrix

    def __getelem__(self, number_of_rows: int, number_of_columns: int) -> int:
        return self.matrix[number_of_rows][number_of_columns]

    def __setelem__(self, row: int, column: int, value):
        self.matrix[row][column] = value

    def __str__(self, output_format: str) -> str:
        mstr = ""
        for row in self.matrix:
            for elem in row:
                if output_format=="Division":
                    mstr += " " + str(elem)
                else:
                    mstr += " " + str(round(elem,5))
            mstr += "\n"
        return mstr
    
    def rows(self):
        return self.row_number
    
    def cols(self):
        return self.column_number

    def copy(self):
        copy = Matrix(self.row_number, self.column_number)
        for row in range(self.row_number):
            for column in range(self.column_number):
                copy.__setelem__(row, column, self.__getelem__(row, column))
        return copy

    def swap_rows(self, i, j):
        for column in range(self.row_number):
            tmp = self.__getelem__(i, column)
            self.__setelem__(i, column, self.__getelem__(j, column))
            self.__setelem__(j, column, tmp)

    def transpose(self):
        transposed_matrix = Matrix(self.column_number, self.row_number)
        for row in range(self.row_number):
            for col in range(self.column_number):
                transposed_matrix.__setelem__(row, col, self.__getelem__(col, row))
        return transposed_matrix

    def is_symmetric(self):
        symmetry = True
        for row in range(self.row_number):
            for column in range(self.row_number):
                if symmetry:
                    symmetry = self.__getelem__(row, column) == self.__getelem__(
                        column, row
                    )
        return symmetry
    
    def set_to_I(self):
        for index in range(self.rows()):
            self.__setelem__(index, index, 1)
            
