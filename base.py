from tkinter import *
from tkinter import messagebox
from matrix_operations import *
from matrix_inversion import *
from QR_decomposition import *
from LU_decomposition import *
from Cholesky_decomposition import *
from eigenvalues import *
import re
from fractions import Fraction
from typing import List
from typing import Tuple

def number_check(value:str)->None:
    if not re.match(r'^-?\d*\.?\d+|\d+/\d+$', value):
        raise ValueError("Please enter a valid input")
    
def number_check_non_square(value:str)->str:
    if value.strip() == '':
        return None
    if not re.match(r'^-?\d*\.?\d+$|^[-]?\d+/\d+$', value):
        raise ValueError("Please enter a valid input")
    return value

def create_fraction_display(root: Frame, numerator: int, denominator:int, custom_font:Tuple[str,int])->None:
    text_width = max(len(numerator), len(denominator)) * 10
    canvas_width = text_width + 20
    canvas = Canvas(
        root, 
        height=30, 
        width=canvas_width)
    
    canvas.grid(
        row=0, 
        column=0, 
        sticky='nsew')
    
    canvas.create_text(
        canvas_width // 2, 
        7, 
        text=numerator, 
        font=custom_font, 
        anchor='center')
    
    canvas.create_line(
        10, 
        15, 
        canvas_width - 10, 
        15)
    
    canvas.create_text(
        canvas_width // 2,  
        22, 
        text=denominator, 
        font=custom_font, 
        anchor='center')
    
def create_number_display(root:Frame, content:str, custom_font:Tuple[str,int])->None:
    canvas_width = max(
        20, 
        len(str(content)) * 10)
    
    canvas = Canvas(
        root, 
        height=30, 
        width=canvas_width)
    
    canvas.grid(
        row=0, 
        column=0, 
        sticky='nsew')
    
    canvas.create_text(
        canvas_width // 2, 
        15, 
        text=content, 
        font=custom_font, 
        anchor='center')

def get_input_row_non_square(frame:Frame, size:int, row_number:int)->List[float]:
    found_none=False
    row = []
    
    for j in range(size):
        entry = frame.grid_slaves(row=row_number, column=j)[0]
        value=entry.get()
        value=number_check_non_square(value)
        
        if value is None:
           found_none=True
           
        else:
            if found_none:
                raise ValueError('Invalid input')
            else: row.append(float(eval(value)))
            
    return row

def get_input_row(frame:Frame, size:int, row_number:int)->List[float]:
    row = []
    
    for j in range(size):
        entry = frame.grid_slaves(row=row_number, column=j)[0]
        value = entry.get()
        number_check(value)
        row.append(float(eval(value)))
        
    return row

def get_input_from_frame_non_square(frame, size):
    matrix = []
    length=None
    found_empty_row=False
    
    for i in range(size):
        row=get_input_row_non_square(frame,size,i)
        
        if len(row)==0:
            found_empty_row=True
            
        if len(row)>0:
            if length is None:
                length=len(row)
            elif len(row)!=length or found_empty_row:
                raise ValueError('Please enter a valid input')
            matrix.append(row)
        
    if length is None:
        raise ValueError('Please enter a valid input')
    
    return matrix
        
def get_input_from_frame(frame: Frame, size: int) -> Matrix:
    matrix = []
    
    for i in range(size):
        matrixrow = get_input_row(frame, size, i)
        matrix.append(matrixrow)
        
    return matrix

def convert_to_division_format_elem(element:float)->str:
    if isinstance(element, float):
        element = Fraction(element).limit_denominator()
        
    if isinstance(element, Fraction):
        
        if element.denominator == 1:
            element=element.numerator
        else:
            sign = "-" if element < 0 else ""
            numerator = abs(element.numerator)
            denominator = element.denominator
            element=f"{sign}{numerator}/{denominator}"
    else: 
        element=str(element)
        
    return element

def convert_to_division_format(matrix: Matrix)->str:
    division_matrix = Matrix(matrix.rows(), matrix.cols())
    
    for i in range(matrix.rows()):
        for j in range(matrix.cols()):
            element = matrix.__getelem__(i, j)
            element = convert_to_division_format_elem(element)
            division_matrix.__setelem__(i, j, element)
            
    return division_matrix

def print_output_matrix(matrix: Matrix, output_label: Label, output_var: str)->None:
    
    for widget in output_label.winfo_children():
        widget.destroy()
        
    for i in range(matrix.rows()):
        for j in range(matrix.cols()):
            element = matrix.__getelem__(i,j)
            label=Label(output_label)
            
            if output_var=='Division' and str(element).find('/')!=-1:
                position=element.find('/')
                numerator=element[:position]
                denominator=element[position+1:]
                create_fraction_display(label,numerator, denominator, ('Helvetica',10))
            else:
                create_number_display(label,round(float(element),2),('Helvetica',10))
                
            label.grid(
                column=j,
                row=i,
                sticky='nsew')
            
def print_output_eigenvalues(
    list: List[float], 
    output_label: Label, 
    output_var: str)->None:
    
    lambdas=["λ₁ = ","λ₂ = ","λ₃ = ","λ₄ = ","λ₅ = "]
    
    for widget in output_label.winfo_children():
        widget.destroy()
    for j in range(len(list)):
        element = list[j]
        label_lambda=Label(output_label)
        create_number_display(label_lambda, lambdas[j], ('Helvetica',14))
        label_number=Label(output_label)
        if output_var=='Division' and str(element).find('/')!=-1:
            position=element.find('/')
            numerator=element[:position]
            denominator=element[position+1:]
            create_fraction_display(label_number,numerator, denominator,('Helvetica',12))
        else:
            create_number_display(label_number,round(float(element),2),('Helvetica',12))
        label_number.grid(
            column=1,
            row=j,
            sticky='nsew')
        
        label_lambda.grid(
            column=0,
            row=j,
            sticky='nsew')
            
def create_input_boxes(frame: Frame, size: int)->List[Entry]:
    input = []
    
    for i in range(size):
        inputrow = []
        
        for j in range(size):
            entry = Entry(
                frame, 
                width=4,
                font=("Helvetica",10),
                relief='ridge')
            
            entry.insert(0, "0")
            entry.grid(row=i, column=j)
            inputrow.append(entry)
            
        input.append(inputrow)
        
    return input

def add_matrices_visual(
    frame1: Frame, 
    frame2: Frame, 
    size: int, 
    output_label: Label,
    output_format: str)->None:
    
    try:
        input1 = get_input_from_frame_non_square(frame1, size)
        input2 = get_input_from_frame_non_square(frame2, size)
        matrix1 = Matrix(len(input1), len(input1[0]), input1)
        matrix2 = Matrix(len(input2), len(input2[0]), input2)
        output_matrix = add(matrix1,matrix2)
        if output_format == "Division":
            output_matrix = convert_to_division_format(output_matrix)
        print_output_matrix(output_matrix, output_label, output_format)
        
    except(ValueError):
        messagebox.showwarning('Hiba','Nem megfelelő inputok, ellenőrizze a következőket: \nszámokkal töltötte fel a mezőket, \nhiányzó mezők ki vannak töltve.')
        
    except(MatrixIncompatibilityError):
        messagebox.showwarning('Hiba','Nem kompatibilis a mátrixok dimenziója!')

    
def subtract_matrices_visual(
    frame1: Frame, 
    frame2: Frame, 
    size: int, 
    output_label: Label,
    output_format: str)->None:
    
    try:
        input1 = get_input_from_frame_non_square(frame1, size)
        input2 = get_input_from_frame_non_square(frame2, size)
        matrix1 = Matrix(len(input1), len(input1[0]), input1)
        matrix2 = Matrix(len(input2), len(input2[0]), input2)
        output_matrix = subtract(matrix1,matrix2)
        if output_format == "Division":
            output_matrix = convert_to_division_format(output_matrix)
        print_output_matrix(output_matrix, output_label, output_format)
        
    except(ValueError):
        messagebox.showwarning('Hiba','Nem megfelelő inputok, ellenőrizze a következőket: számokkal töltötte fel a mezőket, hiányzó mezők ki vannak töltve.')
    except(MatrixIncompatibilityError):
        messagebox.showwarning('Hiba','Nem kompatibilis a mátrixok dimenziója!')
        
def multiply_matrices_visual(
    frame1: Frame, 
    frame2: Frame, 
    size: int, 
    output_label: Label,
    output_format:str)->None:
    
    try:
        input1 = get_input_from_frame_non_square(frame1, size)
        input2 = get_input_from_frame_non_square(frame2, size)
        matrix1 = Matrix(len(input1), len(input1[0]), input1)
        matrix2 = Matrix(len(input2), len(input2[0]), input2)
        output_matrix = multiply(matrix1,matrix2)
        if output_format == "Division":
            output_matrix = convert_to_division_format(output_matrix)
        print_output_matrix(output_matrix, output_label, output_format)
        
    except(ValueError):
        messagebox.showwarning('Hiba','Nem megfelelő inputok, ellenőrizze a következőket: számokkal töltötte fel a mezőket, hiányzó mezők ki vannak töltve.')
    except(MatrixIncompatibilityError):
        messagebox.showwarning('Hiba','Nem kompatibilis a mátrixok dimenziója!')

def invert_matrices_visual(
    frame: Frame, 
    size: int, 
    output_label: Label,
    output_format: str)->None:
    
    try:
        input = get_input_from_frame(frame, size)
        matrix = Matrix(size, size, input)
        output_matrix = invert(matrix)
        if output_format == "Division":
            output_matrix = convert_to_division_format(output_matrix)
        print_output_matrix(output_matrix, output_label, output_format)
        
    except(SingularMatrixError):
        messagebox.showwarning('Hiba','Szinguláris mátrixot adott meg!')
    except(ValueError):
        messagebox.showwarning('Hiba','Nem megfelelő inputok, ellenőrizze a következőket: számokkal töltötte fel a mezőket, hiányzó mezők ki vannak töltve.')

def QR_decompose_visual(
    frame: Frame, 
    size: int, 
    output_label_Q: Label, 
    output_label_R: Label,
    output_format: str)->None:
    
    try:
        input = get_input_from_frame(frame, size)
        matrix = Matrix(size, size, input)
        Q, R = QR_decompose(matrix)
        if output_format == "Division":
            Q = convert_to_division_format(Q)
            R = convert_to_division_format(R)
        print_output_matrix(Q, output_label_Q, output_format)
        print_output_matrix(R, output_label_R, output_format)
 
    except(ValueError):
        messagebox.showwarning('Hiba','Nem megfelelő inputok, ellenőrizze a következőket: számokkal töltötte fel a mezőket, hiányzó mezők ki vannak töltve.')

def LU_decompose_visual(
    frame: Frame,
    size: int,
    output_label_L: Label,
    output_label_U: Label,
    output_format: str)->None:
    
    try:  
        input = get_input_from_frame(frame, size)
        matrix = Matrix(size, size, input)
        L, U, _ = LU_decompose(matrix,"LU")
        if output_format == "Division":
            L = convert_to_division_format(L)
            U = convert_to_division_format(U)

        print_output_matrix(L, output_label_L, output_format)
        print_output_matrix(U, output_label_U, output_format)
        
    except(SingularMatrixError):
        messagebox.showwarning('Hiba','Szinguláris mátrixot adott meg!')
    except(ValueError):
        messagebox.showwarning('Hiba','Nem megfelelő inputok, ellenőrizze a következőket: számokkal töltötte fel a mezőket, hiányzó mezők ki vannak töltve.')
    except(ZeroDivisionError):
        messagebox.showwarning('Hiba','A mátrixnak nem létezik LU-felbontása!')

def Cholesky_decompose_visual(
    frame: Frame, 
    size: int, 
    output_label_L: Label,
    output_format:str)->None:
    
    try:
        input = get_input_from_frame(frame, size)
        matrix = Matrix(size, size, input)
        L = Cholesky_decompose(matrix)
        if output_format == "Division":
            L = convert_to_division_format(L)
        print_output_matrix(L, output_label_L, output_format)
        
    except (AssymmetricMatrixError):
        messagebox.showwarning('Hiba','Aszimmetrikus mátrixot adott meg!')
    except (DefinicyError):
        messagebox.showwarning('Hiba','Nem pozitív definit mátrixot adott meg!')
    except (ValueError):
        messagebox.showwarning('Hiba', 'Nem megfelelő inputok, ellenőrizze a következőket: számokkal töltötte fel a mezőket, hiányzó mezők ki vannak töltve.')
        

def eigenvalues_calculate_visual(
    frame: Frame, 
    inputbox: Entry, 
    size: int, 
    output_label: Label,
    output_format:str)->None:
    
    try:
        input = get_input_from_frame(frame, size)
        matrix = Matrix(size, size, input)
        number_of_iterations = int(inputbox.get())
        eigenvalues = calculate_eigenvalues(matrix, number_of_iterations)
        if output_format=='Division':
            eigenvalues=list(map(lambda x: convert_to_division_format_elem(x),eigenvalues))
        print_output_eigenvalues(eigenvalues, output_label, output_format)
        
    except(ValueError):
        messagebox.showwarning('Hiba','Nem megfelelő inputok, ellenőrizze a következőket: számokkal töltötte fel a mezőket, hiányzó mezők ki vannak töltve.')
    except(ConvergenceError):
        messagebox.showwarning('Hiba','Az algoritmus nem konvergált a sajátértékekhez.')

def calculate_determinant_visual(
    frame:Frame,
    size:int,
    output_label:Label,
    output_format:str)->None:
    
    try:
        input = get_input_from_frame(frame, size)
        matrix = Matrix(size, size, input)
        _, _, determinant= LU_decompose(matrix,"LUP")
        if output_format=='Division':
            determinant=convert_to_division_format_elem(determinant)
            if str(determinant).find('/')!=-1:
                position=determinant.find('/')
                numerator=determinant[:position]
                denominator=determinant[position+1:]
                create_fraction_display(output_label,numerator, denominator,('Helvetica',12))
            else:
                create_number_display(output_label,round(determinant,2),('Helvetica',12))
        else:
            create_number_display(output_label,round(determinant,2),('Helvetica',12))
            
    except(SingularMatrixError):
        create_number_display(output_label,0.0,('Helvetica',12))
    except(ValueError):
        messagebox.showwarning('Hiba','Nem megfelelő inputok, ellenőrizze a következőket: számokkal töltötte fel a mezőket, hiányzó mezők ki vannak töltve.')
    
