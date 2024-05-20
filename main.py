from interface import *
from tkinter import *

SIZE = 3

def main_calculator()->None:

    splash_root.destroy()
    
    root = Tk()
    root.title("Mátrix kalkulátor")
    root.resizable(False, False)

    control_frame = Frame(root)
    control_frame.grid(
        row=0, 
        column=0, 
        sticky="w")

    root.columnconfigure(0, weight=1)

    size_spinbox = Spinbox(
        control_frame, 
        from_=2, 
        to=5, 
        width=5)
    
    size_spinbox.grid(
        row=0, 
        column=1, 
        padx=10, 
        pady=10)
    
    size_spinbox.delete(0, "end")
    size_spinbox.insert(0, 3)  

    size_label = Label(
        control_frame, 
        text="Mátrix mérete:",
        font=('Helvetica',12))
    
    size_label.grid(
        row=0, 
        column=0, padx=10, pady=10)

    operation_frame = Frame(root)
    operation_frame.grid(
        row=1, 
        column=0, 
        sticky="nsew")
    
    root.rowconfigure(1, weight=1) 

    operations = {
        "Mátrix alapműveletek": lambda: basic_operations(operation_frame,SIZE),
        "Inverzszámítás": lambda: calculate_inverse(operation_frame,SIZE),
        "Determinánsszámítás": lambda: calculate_determinant(operation_frame,SIZE),
        "Sajátértékszámítás": lambda: calculate_eigenvalues(operation_frame,SIZE),
        "QR-felbontás": lambda: QR_decompose(operation_frame,SIZE),
        "LU-felbontás": lambda: LU_decompose(operation_frame,SIZE),
        "Cholesky-felbontás": lambda: Cholesky_decompose(operation_frame,SIZE)
    }

    def update_size(new_size:int)->None:
        global SIZE
        SIZE = int(new_size)
        if current_operation: 
            operations[current_operation]()
            
    def update_operation(operation_name)->None:
        global current_operation
        current_operation = operation_name
        operations[operation_name]()

    size_spinbox.config(
        command=lambda: 
            update_size(size_spinbox.get()))

    menubar = Menu(root)
    root.config(menu=menubar)
    
    window_menu = Menu(
        menubar, 
        tearoff=0)
    
    menubar.add_cascade(
        label="Menü", 
        menu=window_menu)

    for op_name in operations.keys():
        window_menu.add_command(
            label=op_name.replace('_', ' '), 
            command=lambda op=op_name: 
                update_operation(op))
        
    update_operation("Mátrix alapműveletek")
    
    width = root.winfo_reqwidth()
    height = root.winfo_reqheight()
    x_offset = (root.winfo_screenwidth() - width) // 2
    y_offset = (root.winfo_screenheight() - height) // 2
    x_offset -= root.winfo_rootx() - root.winfo_x()
    y_offset -= root.winfo_rooty() - root.winfo_y()
    root.geometry(f"+{x_offset}+{y_offset}")
    
    root.mainloop()
    
splash_root=Tk()
splash_root.title('Mátrix kalkulátor')
splash_root.geometry("300x200")

splash_root.overrideredirect(True)

screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()
x = int((screen_width / 2) - (300 / 2))
y = int((screen_height / 2) - (200 / 2))
splash_root.geometry(f"+{x}+{y}")

splash_frame=Frame(splash_root)
splash_frame.pack()
splash_label = Label(
    splash_frame, 
    text="Mátrix kalkulátor", 
    font=("Helvetica", 14), 
    anchor='center')

splash_label.grid(
    row=1,
    column=1,
    sticky='nsew')

left_bracket_frame=Frame(splash_frame)

left_bracket_frame.grid(
    row=1,
    column=0,
    sticky='nsew')

draw_bracket_on_frame(left_bracket_frame,'left',2)

right_bracket_frame=Frame(splash_frame)

right_bracket_frame.grid(
    row=1,
    column=2,
    sticky="nsew")

draw_bracket_on_frame(right_bracket_frame,'right',2)

splash_label = Label(
    splash_frame, 
    text="Töltés...",
    font=("Helvetica", 14),
    anchor='center')

splash_label.grid(
    row=2,
    column=1,
    sticky='nsew')

splash_frame.grid_rowconfigure(0, minsize=50)
splash_root.after(3000,main_calculator)
splash_root.mainloop()


