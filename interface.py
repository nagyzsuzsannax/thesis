from tkinter import *
from base import *
from matrix import *
from tkinter import ttk
from descriptions import *
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

custom_font=('Helvetica',12)
custom_font_explanations=('Helvetica',10)
button_bg_color="#53a0ad"
button_active_color="#3287a1"

def draw_bracket(canvas: Frame, direction: str, size: int)->None:
    
    if direction=='left':
        x_start, y_start = 5, 10
        line_length = 10
        bracket_height = size*40
        canvas.create_line(x_start, y_start, x_start + line_length, y_start)
        canvas.create_line(x_start, y_start, x_start, y_start + bracket_height)
        canvas.create_line(x_start, y_start + bracket_height, x_start + line_length, y_start + bracket_height)
    elif direction=='right':
        x_start, y_start = 10, 10
        line_length = 10
        bracket_height = size*40
        canvas.create_line(x_start, y_start, x_start - line_length, y_start)
        canvas.create_line(x_start, y_start, x_start, y_start + bracket_height)
        canvas.create_line(x_start, y_start + bracket_height, x_start - line_length, y_start + bracket_height)

def draw_bracket_on_frame(root: Frame, direction: str, size: int)->None:
    canvas = Canvas(root, width=12, height=size*40+10)
    canvas.grid(column=0,row=0)
    draw_bracket(canvas, direction, size)

def hide_windows(root:Frame)->None: 
    for widget in root.winfo_children():
        if isinstance(widget, (Frame, Label, Button)):
            widget.destroy()

def toggle_format(format_var:StringVar)->None:
    global output_format
    if format_var.get()=="Tizedestört":
        output_format='Decimal'
    elif format_var.get()=="Hagyományos tört":
        output_format='Division'
        
def basic_operations(root:Frame, SIZE:int)->None:
    hide_windows(root)
    
    root.rowconfigure(1,minsize=10)
    root.columnconfigure(2,minsize=10)
    
    description_frame=Frame(
        root,
        relief='flat', 
        background='white')
    
    description_frame.grid(
        row=0,
        column=1,
        sticky='n')
    
    description_text_1=Text(
        description_frame,
        wrap='word',
        width=50,
        height=10,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_1.grid(
        row=0,
        column=0)
    
    description_text_1.tag_configure(
        'margins', 
        lmargin1=20, 
        lmargin2=20, 
        rmargin=20, 
        background='white')
    
    description=get_basic_operations_explanation()
    description_text_1.insert(
        END,
        description[0],
        'margins')
    
    description_text_2=Text(
        description_frame,
        wrap='word',
        width=50,
        height=2,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_2.grid(
        row=2,
        column=0)
    
    description_text_2.tag_configure(
        'margins', 
        lmargin1=20, 
        lmargin2=20, 
        rmargin=20, 
        background='white')
    
    description_text_2.insert(
        END,
        description[1],
        'margins')
    
    description_text_3=Text(
        description_frame,
        wrap='word',
        width=50,
        height=5,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_3.grid(
        row=4,
        column=0)
    
    description_text_3.tag_configure(
        'margins', 
        lmargin1=20, 
        lmargin2=20, 
        rmargin=20, 
        background='white')
    
    description_text_3.insert(
        END,
        description[2],
        'margins')
    
    matrix_multiplication_image=PhotoImage(file=resource_path("images/matrix_multiplication.png"))
    matrix_addition_image=PhotoImage(file=resource_path("images/matrix_addition.png"))
    matrix_subtraction_image=PhotoImage(file=resource_path("images/matrix_subtraction.png"))
    
    operations_images=[matrix_addition_image,matrix_subtraction_image,matrix_multiplication_image]
    
    description_frame.images = operations_images
    
    addition_label=Label(
        description_frame,
        image=matrix_addition_image, 
        background="white")
    
    addition_label.grid(
        row=1,
        column=0)
    
    subtraction_label=Label(
        description_frame,
        image=matrix_subtraction_image, 
        background="white")
    
    subtraction_label.grid(
        row=3,
        column=0)
    
    multiplication_label=Label(
        description_frame,
        image=matrix_multiplication_image, 
        background="white")
    
    multiplication_label.grid(
        row=5,
        column=0)
    
    calculation_frame=Frame(root)
    calculation_frame.grid(
        row=0,
        column=0,
        sticky='w')
    
    calculation_frame.grid_rowconfigure(0,minsize=10)
    calculation_frame.grid_rowconfigure(2,minsize=10)
    calculation_frame.grid_rowconfigure(6,minsize=10)
    calculation_frame.grid_rowconfigure(8,minsize=10)
    calculation_frame.grid_columnconfigure(0,minsize=10)
    calculation_frame.grid_columnconfigure(7,minsize=10)

    input_frame_1 = Frame(
        calculation_frame,
        padx=10,
        pady=10,
        background=button_bg_color)
    
    input_frame_1.grid(
        row=1, 
        column=1,
        columnspan=3,
        sticky='w')

    input_frame_2 = Frame(
        calculation_frame,
        padx=10,
        pady=10,
        background=button_bg_color)
    
    input_frame_2.grid(
        row=1, 
        column=4,
        columnspan=3,
        sticky='w')

    create_input_boxes(input_frame_1, size=SIZE)
    create_input_boxes(input_frame_2, size=SIZE)

    output_label_format=Frame(
        calculation_frame)
    
    output_label_format.grid(
        row=5, 
        column=1,
        columnspan=6)
    
    output_label = Label(
        output_label_format,
        padx=10,
        pady=10,
        width=20,
        height=10)
    
    bracket_frame_left=Frame(output_label_format)
    bracket_frame_right=Frame(output_label_format)
    
    bracket_frame_left.grid(
        row=0,
        column=0)
    
    bracket_frame_right.grid(
        row=0,
        column=2)
    
    draw_bracket_on_frame(bracket_frame_left,'left',SIZE)
    draw_bracket_on_frame(bracket_frame_right,'right',SIZE)
    
    output_label.grid(
        row=0, 
        column=1)

    calculateButton_addition = Button(
        calculation_frame, 
        text="+", 
        command=lambda: 
            add_matrices_visual(
                input_frame_1,
                input_frame_2,
                SIZE,
                output_label,
                output_format), 
        width=6,
        pady=1,
        font=custom_font,
        bg=button_bg_color,
        fg="white",
        activebackground=button_active_color,
        activeforeground="white")
    
    calculateButton_subtraction = Button(
        calculation_frame, 
        text="-", 
        command=lambda: 
            subtract_matrices_visual(
                input_frame_1,
                input_frame_2,
                SIZE,
                output_label,
                output_format), 
        width=6,
        pady=1,
        font=custom_font,
        bg=button_bg_color,
        fg="white",
        activebackground=button_active_color,
        activeforeground="white")
    
    calculateButton_multiplication = Button(
        calculation_frame, 
        text="x", 
        command=lambda: 
            multiply_matrices_visual(
                input_frame_1,
                input_frame_2,
                SIZE,
                output_label,
                output_format), 
        width=6,
        pady=1,
        font=custom_font,
        bg=button_bg_color,
        fg="white",
        activebackground=button_active_color,
        activeforeground="white")
    
    calculateButton_addition.grid(
        row=3, 
        column=1,
        columnspan=2,
        sticky="w")    
    
    calculateButton_subtraction.grid(
        row=3, 
        column=3,
        columnspan=2)
    
    calculateButton_multiplication.grid(
        row=3, 
        column=5,
        columnspan=2,
        sticky='e')
    

    format_frame = Frame(calculation_frame)
    
    format_frame.grid(
        row=4, 
        column=1, 
        columnspan=6,
        sticky='w')
    
    division_button_label=Label(
        format_frame,
        text="Az eredmény mátrix alakja:",
        font=custom_font)

    division_button_label.grid(
        row=0,
        column=1,
        columnspan=2,
        sticky='w')
    
    format_var=StringVar(value='Tizedestört')

    dropdown_style=ttk.Style()
    dropdown_style.theme_use('clam')
    dropdown_style.configure(
        'TCombobox', 
        fieldbackground=button_bg_color,
        background=button_bg_color,
        foreground='white', 
        arrowcolor='white', 
        borderwidth=2, 
        relief='flat')
    
    format_dropdown = ttk.Combobox(
        format_frame, 
        width=18, 
        textvariable=format_var,
        font=custom_font,
        state="readonly")
    
    format_dropdown['values'] = ("Tizedestört", "Hagyományos tört")
    format_dropdown.grid(
        row=1, 
        column=1, 
        padx=10, 
        pady=10, 
        sticky='w')
    
    format_dropdown.current(0)
    format_dropdown.bind(
        '<<ComboboxSelected>>', 
        lambda event: 
            toggle_format(format_var))
    
    toggle_format(format_var)

    start_output_matrix=Matrix(SIZE,SIZE)
    print_output_matrix(start_output_matrix,output_label,output_format)
    
def LU_decompose(root:Frame, SIZE:int)->None:
    hide_windows(root)
    
    description_frame=Frame(
        root,
        relief='flat', 
        background='white')
    
    description_frame.grid(
        row=0,
        column=1,
        sticky='n')
    
    description_text_1=Text(
        description_frame,
        wrap='word',
        width=50,
        height=5,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_1.grid(
        row=0,
        column=0)
    
    description_text_1.tag_configure(
        'margins', 
        lmargin1=20, 
        lmargin2=20, 
        rmargin=20, 
        background='white')
    
    description=get_explanation_LU()
    description_text_1.insert(
        END,
        description[0],
        'margins')
    
    QR_image=PhotoImage(file=resource_path("images/LU.png"))
    
    inverse_label=Label(
        description_frame,
        image=QR_image, 
        background="white")
    
    inverse_label.grid(
        row=1,
        column=0)
    
    description_text_2=Text(
        description_frame,
        wrap='word',
        width=50,
        height=12,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_2.grid(
        row=2,
        column=0)
    
    description_text_2.tag_configure(
        'margins', 
        lmargin1=20, 
        lmargin2=20, 
        rmargin=20, 
        background='white')
    
    description_text_2.insert(
        END,
        description[1],
        'margins')
    
    description_frame.images = QR_image
    
    description_text_3=Text(
        description_frame,
        wrap='word',
        width=50,
        height=4,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_3.grid(
        row=3,
        column=0)
    
    description_text_3.tag_configure(
        'margins', 
        lmargin1=20, 
        lmargin2=20, 
        rmargin=20, 
        background='white')
    
    description_text_3.insert(
        END,
        description[2],
        'margins')
    
    calculation_frame=Frame(root)
    
    calculation_frame.grid(
        row=0,
        column=0, 
        sticky='w')

    calculation_frame.grid_rowconfigure(0,minsize=10)
    calculation_frame.grid_rowconfigure(3,minsize=10)
    calculation_frame.grid_rowconfigure(9,minsize=10)
    calculation_frame.grid_columnconfigure(0,minsize=10)
    calculation_frame.grid_columnconfigure(6,minsize=10)
    
    inputFrame1 = Frame(
        calculation_frame,
        padx=10,
        pady=10,
        background=button_bg_color)
    
    inputFrame1.grid(
        row=1,
        column=1,
        sticky='w')

    create_input_boxes(inputFrame1, size=SIZE)
    
    format_frame = Frame(calculation_frame)
    
    format_frame.grid(
        row=2, 
        column=1, 
        sticky='w')
    
    division_button_label=Label(
        format_frame,
        text="Az eredmény mátrix alakja:",
        font=custom_font,
        anchor='w')

    division_button_label.grid(
        row=0,
        column=0,
        sticky='w')
    
    format_var=StringVar(value='Tizedestört')
    dropdown_style=ttk.Style()
    dropdown_style.theme_use('clam')
    
    dropdown_style.configure(
        'TCombobox', 
        fieldbackground=button_bg_color,
        background=button_bg_color,
        foreground='white', 
        arrowcolor='white', 
        borderwidth=2, 
        relief='flat')
    
    format_dropdown = ttk.Combobox(
        format_frame, 
        width=18, 
        textvariable=format_var,
        font=custom_font,
        state="readonly")
    
    format_dropdown['values'] = ("Tizedestört", "Hagyományos tört")
    
    format_dropdown.grid(
        row=1, 
        column=0, 
        sticky='w')
    
    format_dropdown.current(0)
    format_dropdown.bind(
        '<<ComboboxSelected>>', 
        lambda event: 
            toggle_format(format_var))
    
    toggle_format(format_var)

    calculateButton = Button(
        calculation_frame, 
        text="LU-felbontás", 
        command=lambda: 
            LU_decompose_visual(
                inputFrame1,
                SIZE,
                outputLabel_L,
                outputLabel_U,
                output_format), 
        padx=10, 
        font=custom_font,
        pady=10,
        bg=button_bg_color,
        fg="white",
        activebackground=button_active_color,
        activeforeground="white")
    
    calculateButton.grid(
        row=4, 
        column=1,
        sticky='nsew')
    
    L_title_label=Label(
        calculation_frame,
        text='L mátrix:',
        font=custom_font,
        anchor='w')
    
    L_title_label.grid(
        row=5,
        column=1,
        sticky='w')
    
    output_label_L_format=Frame(calculation_frame)
    
    output_label_L_format.grid(
        row=6,
        column=1,
        sticky='w')

    outputLabel_L = Label(
        output_label_L_format,
        padx=5, 
        pady=5, 
        height=10,
        width=20)
    
    U_title_label=Label(
        calculation_frame,
        text='U mátrix:',
        font=custom_font,
        anchor='w')
    
    U_title_label.grid(
        row=7,
        column=1,
        sticky='w')
    
    output_label_U_format=Frame(calculation_frame)
    
    output_label_U_format.grid(
        row=8,
        column=1, 
        sticky='w')
    
    outputLabel_U = Label(
        output_label_U_format,
        padx=5, 
        pady=5, 
        height=10,
        width=20)

    outputLabel_L.grid(
        row=0, 
        column=1)
    
    outputLabel_U.grid(
        row=0, 
        column=1)
    
    bracket_frame_L_left=Frame(output_label_L_format)
    bracket_frame_L_right=Frame(output_label_L_format)
    
    bracket_frame_L_left.grid(
        row=0,
        column=0)
    
    bracket_frame_L_right.grid(
        row=0,
        column=2)
    
    draw_bracket_on_frame(bracket_frame_L_left,'left',SIZE)
    draw_bracket_on_frame(bracket_frame_L_right,'right',SIZE)
    
    bracket_frame_U_left=Frame(output_label_U_format)
    bracket_frame_U_right=Frame(output_label_U_format)
    
    bracket_frame_U_left.grid(
        row=0,
        column=0)
    
    bracket_frame_U_right.grid(
        row=0,
        column=2)
    
    draw_bracket_on_frame(bracket_frame_U_left,'left',SIZE)
    draw_bracket_on_frame(bracket_frame_U_right,'right',SIZE)
    
    start_output_matrix=Matrix(SIZE,SIZE)
    print_output_matrix(start_output_matrix,outputLabel_L,output_format)
    print_output_matrix(start_output_matrix,outputLabel_U,output_format)
   
def QR_decompose(root:Frame, SIZE:int)->None:

    hide_windows(root)
    
    description_frame=Frame(
        root,
        relief='flat', 
        background='white')
    
    description_frame.grid(
        row=0,
        column=1,
        sticky='n')
    
    description_text_1=Text(
        description_frame,
        wrap='word',
        width=50,
        height=12,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_1.grid(
        row=0,
        column=0)
    
    description_text_1.tag_configure(
        'margins', 
        lmargin1=20,
        lmargin2=20, 
        rmargin=20, 
        background='white')
    
    description=get_explanation_QR()
    
    description_text_1.insert(
        END,
        description[0],
        'margins')
    
    QR_image=PhotoImage(file=resource_path("images/QR.png"))
    
    inverse_label=Label(
        description_frame,
        image=QR_image, 
        background="white")
    
    inverse_label.grid(
        row=1,
        column=0)
    
    description_text_2=Text(
        description_frame,
        wrap='word',
        width=50,
        height=2,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_2.grid(
        row=2,
        column=0)
    
    description_text_2.tag_configure(
        'margins', 
        lmargin1=20, 
        lmargin2=20, 
        rmargin=20, 
        background='white')
    
    description_text_2.insert(
        END,
        description[1],
        'margins')
    
    description_frame.images = QR_image
    
    description_text_3=Text(
        description_frame,
        wrap='word',
        width=50,
        height=12,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_3.grid(
        row=3,
        column=0)
    
    description_text_3.tag_configure(
        'margins', 
        lmargin1=20, 
        lmargin2=20, 
        rmargin=20, 
        background='white')
    
    description_text_3.insert(
        END,
        description[2],
        'margins')
    
    calculation_frame=Frame(root)
    calculation_frame.grid(
        row=0,
        column=0, 
        sticky='w')

    calculation_frame.grid_rowconfigure(0,minsize=10)
    calculation_frame.grid_rowconfigure(3,minsize=10)
    calculation_frame.grid_rowconfigure(9,minsize=10)
    calculation_frame.grid_columnconfigure(0,minsize=10)
    calculation_frame.grid_columnconfigure(6,minsize=10)
    
    inputFrame1 = Frame(
        calculation_frame,
        padx=10,
        pady=10,
        background=button_bg_color)
    
    inputFrame1.grid(
        row=1,
        column=1,
        sticky='w')

    create_input_boxes(inputFrame1, size=SIZE)
    
    format_frame = Frame(calculation_frame)
    
    format_frame.grid(
        row=2, 
        column=1, 
        sticky='w')
    
    division_button_label=Label(
        format_frame,
        text="Az eredmény mátrix alakja:",
        font=custom_font,
        anchor='w')

    division_button_label.grid(
        row=0,
        column=0,
        sticky='w')
    
    format_var=StringVar(value='Tizedestört')

    dropdown_style=ttk.Style()
    dropdown_style.theme_use('clam')
    dropdown_style.configure(
        'TCombobox', 
        fieldbackground=button_bg_color,
        background=button_bg_color,
        foreground='white', 
        arrowcolor='white', 
        borderwidth=2, 
        relief='flat')
    
    format_dropdown = ttk.Combobox(
        format_frame, 
        width=18, 
        textvariable=format_var,
        font=custom_font,
        state="readonly")
    
    format_dropdown['values'] = ("Tizedestört", "Hagyományos tört")
    format_dropdown.grid(
        row=1, 
        column=0, 
        sticky='w')
    
    format_dropdown.current(0)
    format_dropdown.bind('<<ComboboxSelected>>', lambda event: toggle_format(format_var))
    
    toggle_format(format_var)

    calculateButton = Button(
        calculation_frame, 
        text="QR-felbontás", 
        command=lambda: 
            QR_decompose_visual(
                inputFrame1,
                SIZE,
                output_label_Q,
                outputLabel_R,
                output_format), 
        padx=10, 
        font=custom_font,
        pady=10,
        bg=button_bg_color,
        fg="white",
        activebackground=button_active_color,
        activeforeground="white")
    
    calculateButton.grid(
        row=4, 
        column=1,
        sticky='nsew')
    
    Q_title_label=Label(
        calculation_frame,
        text='Q mátrix:',
        font=custom_font,
        anchor='w')
    
    Q_title_label.grid(
        row=5,
        column=1,
        sticky='w')
    
    output_label_Q_format=Frame(calculation_frame)
    output_label_Q_format.grid(
        row=6,
        column=1,
        sticky='w')

    output_label_Q = Label(
        output_label_Q_format,
        padx=5, 
        pady=5, 
        height=10,
        width=20)
    
    R_title_label=Label(
        calculation_frame,
        text='R mátrix:',
        font=custom_font,
        anchor='w')
    
    R_title_label.grid(
        row=7,
        column=1,
        sticky='w')
    
    output_label_R_format=Frame(calculation_frame)
    output_label_R_format.grid(
        row=8,
        column=1, 
        sticky='w')
    
    outputLabel_R = Label(
        output_label_R_format,
        padx=5, 
        pady=5, 
        height=10,
        width=20)

    output_label_Q.grid(
        row=0, 
        column=1)
    
    outputLabel_R.grid(
        row=0, 
        column=1)
    
    bracket_frame_Q_left=Frame(output_label_Q_format)
    bracket_frame_Q_right=Frame(output_label_Q_format)
    
    bracket_frame_Q_left.grid(
        row=0,
        column=0)
    
    bracket_frame_Q_right.grid(
        row=0,
        column=2)
    
    draw_bracket_on_frame(bracket_frame_Q_left,'left',SIZE)
    draw_bracket_on_frame(bracket_frame_Q_right,'right',SIZE)
    
    bracket_frame_R_left=Frame(output_label_R_format)
    bracket_frame_R_right=Frame(output_label_R_format)
    
    bracket_frame_R_left.grid(
        row=0,
        column=0)
    
    bracket_frame_R_right.grid(
        row=0,
        column=2)
    
    draw_bracket_on_frame(bracket_frame_R_left,'left',SIZE)
    draw_bracket_on_frame(bracket_frame_R_right,'right',SIZE)
    
    start_output_matrix=Matrix(SIZE,SIZE)
    print_output_matrix(start_output_matrix,output_label_Q,output_format)
    print_output_matrix(start_output_matrix,outputLabel_R,output_format)   

def Cholesky_decompose(root:Frame, SIZE:int)->None:
    
    hide_windows(root)
    
    description_frame=Frame(
        root,
        relief='flat',
        background='white')
    
    description_frame.grid(
        row=0,
        column=1,
        sticky='n')
    
    description_text_1=Text(
        description_frame,
        wrap='word',
        width=50,
        height=9,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_1.grid(
        row=0,
        column=0)
    
    description_text_1.tag_configure(
        'margins', 
        lmargin1=20, 
        lmargin2=20, 
        rmargin=20, 
        background='white')
    
    description=get_explanation_Cholesky()
    description_text_1.insert(
        END,
        description[0],
        'margins')
    
    inverse_image=PhotoImage(file=resource_path("images/Cholesky.png"))
    
    inverse_label=Label(
        description_frame,
        image=inverse_image, 
        background="white")
    
    inverse_label.grid(
        row=1,
        column=0)
    
    description_text_2=Text(
        description_frame,
        wrap='word',
        width=50,
        height=4,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_2.grid(
        row=2,
        column=0)
    
    description_text_2.tag_configure(
        'margins', 
        lmargin1=20, 
        lmargin2=20, 
        rmargin=20, 
        background='white')
    
    description_text_2.insert(
        END,
        description[1],
        'margins')
    
    description_frame.images = inverse_image
    
    description_text_3=Text(
        description_frame,
        wrap='word',
        width=50,
        height=5,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_3.grid(
        row=3,
        column=0)
    
    description_text_3.tag_configure(
        'margins',
        lmargin1=20,
        lmargin2=20,
        rmargin=20, 
        background='white')
    
    description_text_3.insert(
        END,
        description[2],
        'margins')
    
    calculation_frame=Frame(root)
    
    calculation_frame.grid(
        row=0,
        column=0,
        sticky='w')
    
    calculation_frame.grid_rowconfigure(0,minsize=10)
    calculation_frame.grid_rowconfigure(3,minsize=10)
    calculation_frame.grid_rowconfigure(9,minsize=10)
    calculation_frame.grid_columnconfigure(0,minsize=10)
    calculation_frame.grid_columnconfigure(6,minsize=10)
    
    inputFrame1 = Frame(
        calculation_frame,
        padx=10,
        pady=10,
        background=button_bg_color)
    
    inputFrame1.grid(
        row=1,
        column=1,
        sticky="w")

    create_input_boxes(inputFrame1, size=SIZE)
    
    format_frame = Frame(calculation_frame)
    
    format_frame.grid(
        row=2, 
        column=1, 
        sticky='w')
    
    division_button_label=Label(
        format_frame,
        text="Az eredmény mátrix alakja:",
        font=custom_font,
        anchor='w')

    division_button_label.grid(
        row=0,
        column=0,
        sticky='w')
    
    format_var=StringVar(value='Tizedestört')  # Default format

    dropdown_style=ttk.Style()
    dropdown_style.theme_use('clam')
    dropdown_style.configure(
        'TCombobox', 
        fieldbackground=button_bg_color,
        background=button_bg_color,
        foreground='white', 
        arrowcolor='white', 
        borderwidth=2, 
        relief='flat')
    
    format_dropdown = ttk.Combobox(
        format_frame, 
        width=18, 
        textvariable=format_var,
        font=custom_font,
        state="readonly")
    
    format_dropdown['values'] = ("Tizedestört", "Hagyományos tört")
    format_dropdown.grid(
        row=1, 
        column=0, 
        sticky='w')
    
    format_dropdown.current(0)
    format_dropdown.bind(
        '<<ComboboxSelected>>',
        lambda event: 
            toggle_format(format_var))
    
    toggle_format(format_var)

    calculateButton = Button(
        calculation_frame, 
        text="Cholesky-felbontás", 
        command=lambda: 
            Cholesky_decompose_visual(
                inputFrame1,
                SIZE,
                output_label_L,
                output_format), 
        padx=10, 
        font=custom_font,
        pady=10,
        bg=button_bg_color,
        fg="white",
        activebackground=button_active_color,
        activeforeground="white")
    
    calculateButton.grid(
        row=4, 
        column=1,
        sticky='nsew')
    
    L_title_label=Label(
        calculation_frame,
        text='L mátrix:',
        font=custom_font,
        anchor='w')
    
    L_title_label.grid(
        row=5,
        column=1,
        sticky='w')
    
    output_label_L_format=Frame(calculation_frame)
    output_label_L_format.grid(
        row=6,
        column=1,
        sticky='w')

    output_label_L = Label(
        output_label_L_format,
        padx=5, 
        pady=5, 
        height=10,
        width=20)

    output_label_L.grid(
        row=0, 
        column=1)
    
    bracket_frame_L_left=Frame(output_label_L_format)
    bracket_frame_L_right=Frame(output_label_L_format)
    
    bracket_frame_L_left.grid(
        row=0,
        column=0)
    
    bracket_frame_L_right.grid(
        row=0,
        column=2)
    
    draw_bracket_on_frame(bracket_frame_L_left,'left',SIZE)
    draw_bracket_on_frame(bracket_frame_L_right,'right',SIZE)
    
    start_output_matrix=Matrix(SIZE,SIZE)
    print_output_matrix(start_output_matrix,output_label_L,output_format)   
    
def calculate_eigenvalues(root:Frame, SIZE:int)->None:
    
    hide_windows(root)
    
    description_frame=Frame(
        root,
        relief='flat', 
        background='white')
    
    description_frame.grid(
        row=0,
        column=1,
        sticky='n')
    
    description_text_1=Text(
        description_frame,
        wrap='word',
        width=50,
        height=6,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_1.grid(
        row=0,
        column=0)
    
    description_text_1.tag_configure(
        'margins', 
        lmargin1=20,
        lmargin2=20,
        rmargin=20,
        background='white')
    
    description=get_eigenvalues_explanation()
    description_text_1.insert(
        END,
        description[0],
        'margins')
    
    eigenvalue_image_1=PhotoImage(file=resource_path("images/eigenvalue_1.png"))
    eigenvalue_image_2=PhotoImage(file=resource_path("images/eigenvalue_2.png"))
        
    description_text_2=Text(
        description_frame,
        wrap='word',
        width=50,
        height=5,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_2.grid(
        row=1,
        column=0)
    
    description_text_2.tag_configure(
        'margins', 
        lmargin1=20, 
        lmargin2=20, 
        rmargin=20, 
        background='white')
    
    description_text_2.insert(
        END,
        description[1],
        'margins')

    eigenvalue_label_1_label=Label(
        description_frame,
        image=eigenvalue_image_1, 
        background="white")
    
    eigenvalue_label_1_label.grid(
        row=2,
        column=0)

    eigenvalue_label_2_label=Label(
        description_frame,
        image=eigenvalue_image_2,
        background="white")
    
    eigenvalue_label_2_label.grid(
        row=4,
        column=0)
    
    description_frame.images = [eigenvalue_image_1,eigenvalue_image_2]
    
    description_text_3=Text(
        description_frame,
        wrap='word',
        width=50,
        height=7,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_3.grid(
        row=3,
        column=0)
    
    description_text_3.tag_configure(
        'margins', 
        lmargin1=20, 
        lmargin2=20, 
        rmargin=20, 
        background='white')
    
    description_text_3.insert(
        END,
        description[2],
        'margins')
    
    calculation_frame=Frame(root)
    
    calculation_frame.grid(
        row=0,
        column=0,
        sticky='w')
    
    calculation_frame.grid_rowconfigure(0,minsize=10)
    calculation_frame.grid_rowconfigure(2,minsize=10)
    calculation_frame.grid_rowconfigure(5,minsize=10)
    calculation_frame.grid_rowconfigure(9,minsize=10)
    calculation_frame.grid_columnconfigure(0,minsize=10)
    calculation_frame.grid_columnconfigure(3,minsize=10)
    
    input_frame = Frame(
        calculation_frame,
        padx=10,
        pady=10,
        bg=button_bg_color)
    
    input_frame.grid(
        row=1, 
        column=1,
        sticky='w')
    
    create_input_boxes(input_frame, size=SIZE)
    
    input_frame_iterations_format=Frame(calculation_frame)
    
    input_frame_iterations_format.grid(
        row=3,
        column=1)
    
    input_label_iterations=Label(
        input_frame_iterations_format,
        text="QR iterációk száma:",
        font=custom_font,
        anchor='w')
    
    input_label_iterations.grid(
        row=0,
        column=0,
        sticky='w')

    input_frame_iterations=Frame(
        input_frame_iterations_format,
        padx=10,
        pady=10,
        bg=button_bg_color)
    
    input_entry_iterations=Entry(
        input_frame_iterations,
        width=4) 
    
    input_entry_iterations.insert(1,"1")
    
    input_entry_iterations.grid(
        row=0,
        column=0)   
    
    input_frame_iterations.grid(
        row=0,
        column=1,
        sticky='w')
        
    format_frame = Frame(calculation_frame)
    
    format_frame.grid(
        row=4, 
        column=1, 
        sticky='w')
    
    division_button_label=Label(
        format_frame,
        text="Az eredmény alakja:",
        font=custom_font,
        anchor='w')

    division_button_label.grid(
        row=0,
        column=0,
        sticky='w')
    
    format_var=StringVar(value='Tizedestört')  # Default format

    dropdown_style=ttk.Style()
    dropdown_style.theme_use('clam')
    dropdown_style.configure(
        'TCombobox', 
        fieldbackground=button_bg_color,
        background=button_bg_color,
        foreground='white', 
        arrowcolor='white', 
        borderwidth=2, 
        relief='flat')
    
    format_dropdown = ttk.Combobox(
        format_frame, 
        width=18, 
        textvariable=format_var,
        font=custom_font,
        state="readonly")
    
    format_dropdown['values'] = ("Tizedestört", "Hagyományos tört")
    format_dropdown.grid(
        row=1, 
        column=0, 
        sticky='w')
    
    format_dropdown.current(0)
    format_dropdown.bind(
        '<<ComboboxSelected>>', 
        lambda event: 
            toggle_format(format_var))
    
    toggle_format(format_var)
     
    calculateButton = Button(
        calculation_frame, 
        text="Sajátértékek számítása", 
        command=lambda: 
            eigenvalues_calculate_visual(
                input_frame,
                input_entry_iterations,
                SIZE,
                output_label,
                output_format), 
        font=custom_font,
        padx=20, 
        pady=5,
        bg=button_bg_color,
        fg="white",
        activebackground=button_active_color,
        activeforeground="white")
    
    calculateButton.grid(
        row=6, 
        column=1,
        sticky='w')
    
    output_label_title=Label(
        calculation_frame,
        text='A mátrix sajátértékei:',
        font=custom_font,
        anchor='w')
    
    output_label_title.grid(
        row=7,
        column=1,
        sticky='w')
    
    output_label = Label(
        calculation_frame, 
        padx=10, 
        pady=10, 
        width=20)
    
    output_label.grid(
        row=8, 
        column=1)
    
    output_list_start=SIZE*[0.0]
    print_output_eigenvalues(output_list_start,output_label,output_format)
        
def calculate_inverse(root:Frame, SIZE:int)->None:
    
    hide_windows(root)
    
    description_frame=Frame(
        root,
        relief='flat', 
        background='white')
    
    description_frame.grid(
        row=0,
        column=1,
        sticky='n')
    
    description_text_1=Text(
        description_frame,
        wrap='word',
        width=50,
        height=5,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_1.grid(
        row=0,
        column=0)
    
    description_text_1.tag_configure(
        'margins', 
        lmargin1=20, 
        lmargin2=20, 
        rmargin=20, 
        background='white')
    
    description=get_inverse_explanation()
    
    description_text_1.insert(
        END,
        description[0],
        'margins')
    
    inverse_image=PhotoImage(file=resource_path("images/inverse.png"))
    
    inverse_label=Label(
        description_frame,
        image=inverse_image, 
        background="white")
    
    inverse_label.grid(
        row=1,
        column=0)
    
    description_text_2=Text(
        description_frame,
        wrap='word',
        width=50,
        height=2,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_2.grid(
        row=2,
        column=0)
    
    description_text_2.tag_configure(
        'margins',
        lmargin1=20, 
        lmargin2=20, 
        rmargin=20, 
        background='white')
    
    description_text_2.insert(
        END,
        description[1],
        'margins')
    
    description_frame.images = inverse_image
    
    description_text_3=Text(
        description_frame,
        wrap='word',
        width=50,
        height=10,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_3.grid(
        row=3,
        column=0)
    
    description_text_3.tag_configure(
        'margins',
        lmargin1=20,
        lmargin2=20,
        rmargin=20, 
        background='white')
    
    description_text_3.insert(
        END,
        description[2],
        'margins')
    
    calculation_frame=Frame(root)
    calculation_frame.grid(
        row=0,
        column=0, 
        sticky='w')

    calculation_frame.grid_rowconfigure(0,minsize=10)
    calculation_frame.grid_rowconfigure(3,minsize=10)
    calculation_frame.grid_rowconfigure(9,minsize=10)
    calculation_frame.grid_columnconfigure(0,minsize=10)
    calculation_frame.grid_columnconfigure(6,minsize=10)
    
    inputFrame1 = Frame(
        calculation_frame,
        padx=10,
        pady=10,
        background=button_bg_color)
    
    inputFrame1.grid(
        row=1,
        column=1,
        sticky="w")

    create_input_boxes(inputFrame1, size=SIZE)
    
    format_frame = Frame(calculation_frame)
    
    format_frame.grid(
        row=2, 
        column=1, 
        sticky='w')
    
    division_button_label=Label(
        format_frame,
        text="Az eredmény mátrix alakja:",
        font=custom_font,
        anchor='w')

    division_button_label.grid(
        row=0,
        column=0,
        sticky='w')
    
    format_var=StringVar(value='Tizedestört')  # Default format

    dropdown_style=ttk.Style()
    dropdown_style.theme_use('clam')
    dropdown_style.configure(
        'TCombobox', 
        fieldbackground=button_bg_color,
        background=button_bg_color,
        foreground='white', 
        arrowcolor='white', 
        borderwidth=2, 
        relief='flat')
    
    format_dropdown = ttk.Combobox(
        format_frame, 
        width=18, 
        textvariable=format_var,
        font=custom_font,
        state="readonly")
    
    format_dropdown['values'] = ("Tizedestört", "Hagyományos tört")
    format_dropdown.grid(
        row=1, 
        column=0, 
        sticky='w')
    
    format_dropdown.current(0)
    format_dropdown.bind(
        '<<ComboboxSelected>>', 
        lambda event: 
            toggle_format(format_var))
    
    toggle_format(format_var)

    calculateButton = Button(
        calculation_frame, 
        text="Mátrix invertálás", 
        command=lambda: 
            invert_matrices_visual(
                inputFrame1,
                SIZE,
                output_label,
                output_format), 
        padx=10, 
        font=custom_font,
        pady=10,
        bg=button_bg_color,
        fg="white",
        activebackground=button_active_color,
        activeforeground="white")
    
    calculateButton.grid(
        row=4, 
        column=1,
        sticky='nsew')
    
    title_label=Label(
        calculation_frame,
        text='A mátrix inverze:',
        font=custom_font,
        anchor='w')
    
    title_label.grid(
        row=5,
        column=1,
        sticky='w')
    
    output_label_format=Frame(calculation_frame)
    output_label_format.grid(
        row=6,
        column=1,
        sticky='w')

    output_label = Label(
        output_label_format,
        padx=5, 
        pady=5, 
        height=10,
        width=20)

    output_label.grid(
        row=0, 
        column=1)
    
    bracket_frame_left=Frame(output_label_format)
    bracket_frame_right=Frame(output_label_format)
    
    bracket_frame_left.grid(
        row=0,
        column=0)
    
    bracket_frame_right.grid(
        row=0,
        column=2)
    
    draw_bracket_on_frame(bracket_frame_left,'left',SIZE)
    draw_bracket_on_frame(bracket_frame_right,'right',SIZE)
    
    start_output_matrix=Matrix(SIZE,SIZE)
    print_output_matrix(start_output_matrix,output_label,output_format)
    
def calculate_determinant(root:Frame, SIZE:int)->None:
    
    hide_windows(root)
    
    calculation_frame=Frame(root)
    calculation_frame.grid(
        row=0,
        column=0,
        sticky='nw')
        
    description_frame=Frame(
        root,
        relief='flat', 
        background='white')
    
    description_frame.grid(
        row=0,
        column=1,
        sticky='n')
    
    description_text_1=Text(
        description_frame,
        wrap='word',
        width=50,
        height=5,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_1.grid(
        row=0,
        column=0)
    
    description_text_1.tag_configure(
        'margins', 
        lmargin1=20, 
        lmargin2=20, 
        rmargin=20, 
        background='white')
    
    description=get_determinant_explanation()
    description_text_1.insert(
        END,
        description[0],
        'margins')
    
    determinant_image_1=PhotoImage(file=resource_path("images/determinant_laplace.png"))
    determinant_image_2=PhotoImage(file=resource_path("images/determinant_lu_1.png"))
    determinant_image_3=PhotoImage(file=resource_path("images/determinant_lu_2.png"))
    
    addition_label_1=Label(
        description_frame,
        image=determinant_image_1,
        background="white")
    
    addition_label_1.grid(
        row=1,
        column=0)
    
    description_text_2=Text(
        description_frame,
        wrap='word',
        width=50,
        height=2,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_2.grid(
        row=2,
        column=0)
    
    description_text_2.tag_configure(
        'margins', 
        lmargin1=20,
        lmargin2=20,
        rmargin=20,
        background='white')
    
    description_text_2.insert(
        END,
        description[1],
        'margins')
    
    addition_label_2=Label(
        description_frame,
        image=determinant_image_2, 
        background="white")
    
    addition_label_2.grid(
        row=4,
        column=0)
    
    addition_label_3=Label(
        description_frame,
        image=determinant_image_3, 
        background="white")
    
    addition_label_3.grid(
        row=5,
        column=0)
    
    description_frame.images = [determinant_image_1,determinant_image_2,determinant_image_3]
    
    description_text_3=Text(
        description_frame,
        wrap='word',
        width=50,
        height=10,
        font=custom_font_explanations,
        relief='flat')
    
    description_text_3.grid(
        row=3,
        column=0)
    description_text_3.tag_configure(
        'margins', 
        lmargin1=20, 
        lmargin2=20, 
        rmargin=20, 
        background='white')
    
    description_text_3.insert(
        END,
        description[2],
        'margins')
    
    calculation_frame.grid_rowconfigure(0,minsize=10)
    calculation_frame.grid_rowconfigure(3,minsize=10)
    calculation_frame.grid_rowconfigure(8,minsize=10)
    calculation_frame.grid_columnconfigure(0,minsize=10)
    calculation_frame.grid_columnconfigure(2,minsize=10)
    
    inputFrame1 = Frame(
        calculation_frame, 
        padx=10, 
        pady=10, 
        bg=button_bg_color)
    
    inputFrame1.grid(
        row=1, 
        column=1, 
        sticky='nw')

    create_input_boxes(inputFrame1, size=SIZE)
    
    format_frame = Frame(calculation_frame)
    
    format_frame.grid(
        row=2, 
        column=1, 
        sticky='w')
    
    division_button_label=Label(
        format_frame,
        text="Az eredmény alakja:",
        font=custom_font,
        anchor='w')

    division_button_label.grid(
        row=0,
        column=0,
        sticky='w')
    
    format_var=StringVar(value='Tizedestört')  # Default format

    dropdown_style=ttk.Style()
    dropdown_style.theme_use('clam')
    dropdown_style.configure(
        'TCombobox', 
        fieldbackground=button_bg_color,
        background=button_bg_color,
        foreground='white', 
        arrowcolor='white', 
        borderwidth=2, 
        relief='flat')
    
    format_dropdown = ttk.Combobox(
        format_frame, 
        width=18, 
        textvariable=format_var,
        font=custom_font,
        state="readonly")
    
    format_dropdown['values'] = ("Tizedestört", "Hagyományos tört")
    format_dropdown.grid(
        row=1, 
        column=0, 
        sticky='w')
    
    format_dropdown.current(0)
    format_dropdown.bind(
        '<<ComboboxSelected>>', 
        lambda event: 
            toggle_format(format_var))
    
    toggle_format(format_var)

    calculate_button = Button(
        calculation_frame, 
        text="Determináns számítása", 
        command=lambda: 
            calculate_determinant_visual(
                inputFrame1,
                SIZE,
                output_label,
                output_format), 
        padx=10, 
        pady=10,
        bg=button_bg_color,
        font=custom_font,
        fg="white",
        activebackground=button_active_color,
        activeforeground="white")
    
    calculate_button.grid(
        row=4, 
        column=1,
        sticky='w')
    
    
    output_frame=Frame(calculation_frame)
    output_frame.grid(
        row=5,
        column=1)
    
    output_title_label=Label(
        output_frame,
        text='A mátrix determinánsa:',
        font=custom_font)
    
    output_title_label.grid(
        row=0,
        column=0)
    
    output_label = Label(
        output_frame, 
        width=10)
    
    output_label.grid(
        row=0, 
        column=1)


   

        
    
    


