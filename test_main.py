import pytest
from matrix import *
from matrix_operations import *
from matrix_inversion import *
from LU_decomposition import *
from eigenvalues import *
from QR_decomposition import *
from Cholesky_decomposition import *

def matrix_equals(matrix1:Matrix,matrix2:Matrix):
    if matrix1.cols()!=matrix2.cols() or matrix1.rows()!=matrix2.rows():
        return False
    for row in range(matrix1.rows()):
        for column in range(matrix1.cols()):
            if matrix1.__getelem__(row,column)!=matrix2.__getelem__(row,column):
                return False
    return True
            

#OPERATIONS

matrix1_elements=[[1,3,4],[2,2,3],[1,1,2]]
matrix1=Matrix(3,3,matrix1_elements)
matrix2_elements=[[4,5,6],[7,8,9],[1,2,1]]
matrix2=Matrix(3,3,matrix2_elements)
matrix3_elements=[[1,1],[2,2],[3,3]]
matrix3=Matrix(3,2,matrix3_elements)


#ADDITION

add_1_2_elements=[[5,8,10],[9,10,12],[2,3,3]]
add_1_2_matrix=Matrix(3,3,add_1_2_elements)

def test_add_positive():
    assert matrix_equals(add(matrix1,matrix2),add_1_2_matrix)

def test_add_negative():
    with pytest.raises(MatrixIncompatibilityError):
        add(matrix1,matrix3)
        
#SUBTRACTION
subtract_1_2_elements=[[-3,-2,-2],[-5,-6,-6],[0,-1,1]]
subtract_1_2_matrix=Matrix(3,3,subtract_1_2_elements)
        
def test_subtract_positive():
    assert matrix_equals(subtract(matrix1,matrix2),subtract_1_2_matrix)

def test_subtract_negative():
    with pytest.raises(MatrixIncompatibilityError):
        subtract(matrix1,matrix3)
        
#MULTIPLICATION
multiply_2_3_elements=[[32,32],[50,50],[8,8]]
multiply_2_3_matrix=Matrix(3,2,multiply_2_3_elements)

def test_multiply_positive():
    assert matrix_equals(multiply(matrix2,matrix3),multiply_2_3_matrix)

def test_multiply_negative():
    with pytest.raises(MatrixIncompatibilityError):
        multiply(matrix3,matrix1)
        
#INVERSION
inverse_1_elements=[[-0.5,1,-0.5],[0.5,1,-2.5],[0,-1,2]]
inverse_1_matrix=Matrix(3,3,inverse_1_elements)

def test_inverse_positive():
    assert matrix_equals(invert(matrix1),inverse_1_matrix)
    
singular_matrix_elements=[[1,2,3],[0,0,0],[4,5,6]]
singular_matrix=Matrix(3,3,singular_matrix_elements)
    
def test_inverse_negative():
    with pytest.raises(SingularMatrixError):
        invert(singular_matrix)
        
#LU, DETEMINANT

matrix4_elements=[[2,1,1],[4,3,3],[8,7,9]]
matrix4=Matrix(3,3,matrix4_elements)

L_elements=[[1,0,0],[2,1,0],[4,3,1]]
L=Matrix(3,3,L_elements)

U_elements=[[2,1,1],[0,1,1],[0,0,2]]
U=Matrix(3,3,U_elements)

def test_LU_positive():
    L_test,U_test,_=LU_decompose(matrix4,"LU")
    assert matrix_equals(L_test,L)
    assert matrix_equals(U_test,U)

def test_determ_positive():
    _,_,deter=LU_decompose(matrix4,'LUP')
    assert deter==4
    _,_,deter=LU_decompose(matrix5,'LUP')
    assert deter==-1
    
singular_matrix=Matrix(3,3)
matrix5_elements=[[0,0,1],[0,1,0],[1,0,0]]
matrix5=Matrix(3,3,matrix5_elements)

def test_LU_negative():
    with pytest.raises(SingularMatrixError):
        LU_decompose(singular_matrix,'LU')
    with pytest.raises(ZeroDivisionError):
        LU_decompose(matrix5,'LU')
        
def test_determ_negative():
    with pytest.raises(SingularMatrixError):
        LU_decompose(singular_matrix,'LUP')
    
#EIGENVALUES
def test_eigenvalues_positive():
    eigenvalues=[5.80232,-1.11223,0.30991]
    eigenvalues_matrix_1=calculate_eigenvalues(matrix1,100)
    assert [round(elem,5) for elem in eigenvalues_matrix_1]==eigenvalues
    
def test_eigenvalues_negative():
    with pytest.raises(ConvergenceError):
        calculate_eigenvalues(matrix2,10000)
    
#QR

Q_elements=[[0.40825,0.91287,0.0],[0.8165,-0.36515,-0.44721],[0.40825,-0.18257,0.89443]]
R_elements=[[2.44949,3.26599,4.89898],[0,1.82574,2.19089],[0,0,0.44721]]

Q_test=Matrix(3,3,Q_elements)
R_test=Matrix(3,3,R_elements)
def test_QR_positive():
    Q,R=QR_decompose(matrix1)
    for i in range(Q.cols()):
        for j in range(Q.cols()):
            Q.__setelem__(i,j,round(Q.__getelem__(i,j),5))
            R.__setelem__(i,j,round(R.__getelem__(i,j),5))
       
    assert matrix_equals(R_test,R)
    assert matrix_equals(Q_test,Q)
    
#CHOLESKY
L_elements=[[2,0,0],[6,1,0],[-8,5,3]]
L_test=Matrix(3,3,L_elements)

matrix6_elements=[[4,12,-16],[12,37,-43],[-16,-43,98]]
matrix6=Matrix(3,3,matrix6_elements)

def test_Cholesky_positive():
    L=Cholesky_decompose(matrix6)
    for i in range(L.cols()):
        for j in range(L.cols()):
            L.__setelem__(i,j,round(L.__getelem__(i,j),5))
    
    assert matrix_equals(L,L_test) 
    
matrix7_elements=[[9,12,15],[12,25,30],[15,30,36]]  
matrix7=Matrix(3,3,matrix7_elements)    

def test_Cholesky_negative():
    with pytest.raises(AssymmetricMatrixError):
        Cholesky_decompose(matrix1)
    with pytest.raises(DefinicyError):
        Cholesky_decompose(matrix7)

