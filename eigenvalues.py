from QR_decomposition import *

def calculate_eigenvalues(input_matrix: Matrix, number_of_iterations: int):
    A=input_matrix.copy()
    for i in range(number_of_iterations):
        Q,R=QR_decompose(A)
        A=multiply(R,Q)
    
    is_converged=True
    for i in range(A.cols()):
        for j in range(i):
            if not is_close_to_zero(A.__getelem__(i,j)):
                raise ConvergenceError('The eigenvalues did not converge')

    eigenvalues=[]   
    for i in range(A.cols()):
        eigenvalues.append(A.__getelem__(i,i))
    print(A.__str__('Decimal'))
    return eigenvalues
    