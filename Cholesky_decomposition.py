
from matrix_operations import *
from eigenvalues import *


def check_symmetry(H:Matrix):
    if not Matrix.is_symmetric(H):
        raise AssymmetricMatrixError("Assymmetric matrix")
    
##positive check
def check_positive_deficiency(H:Matrix):
    try:
        eigenvalues=calculate_eigenvalues(H,10000)
    except(ConvergenceError):
        raise DefinicyError('Matrix is not positive definite')
    if any([is_close_to_zero(elem) for elem in eigenvalues]) or not all([elem>0 for elem in eigenvalues]):
        raise DefinicyError('Matrix not positive definite')
    
def update_elements(row:int, column:int, L:Matrix,H:Matrix,newelement:float):
    if row == column:
        for index in range(column):
            elem=L.__getelem__(row, index) 
            newelement += elem*elem

        newelement=math.sqrt(H.__getelem__(column,column)-newelement)
        L.__setelem__(row, column, newelement)
        
    else:
        for index in range(column):
            elem1=L.__getelem__(row, index)
            elem2=L.__getelem__(column, index)
            newelement += elem1 * elem2
            
        l_elem=L.__getelem__(column, column)
        h_elem=H.__getelem__(row, column)
        newelement=(1 / l_elem) * (h_elem - newelement) 
        L.__setelem__(row,column,newelement)
        
def Cholesky_decompose(input_matrix: Matrix):
        check_symmetry(input_matrix)
        check_positive_deficiency(input_matrix)

        L = Matrix(input_matrix.rows(), input_matrix.cols())
        H = input_matrix.copy()
        
        for row in range(L.rows()):
            for column in range(row+1):
                newelement = 0.0
                update_elements(row,column,L,H,newelement)
        return L