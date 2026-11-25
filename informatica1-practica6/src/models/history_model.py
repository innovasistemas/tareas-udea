import src.utils.colors_symbols as col_sym
import src.config.database as db

def show_data(y: list, title) -> None:
    # Encabezado
    print("-" * 25)
    print(f"| {col_sym.BRIGHT_CYAN}{title:^20} {col_sym.WHITE} |")
    print("-" * 25)
    print(col_sym.BLUE, end="")
    print("-" * 25, col_sym.WHITE)
    print(f"| {col_sym.YELLOW}{'Año':^7}{col_sym.WHITE} ", end="")
    print(f"| {col_sym.YELLOW}{'Estudiantes':^11}{col_sym.WHITE}", end="")
    print(" |")
    print(col_sym.BLUE, end="")
    print("-" * 25, col_sym.WHITE)

    # Cuerpo
    for i in range(db.h):
        print(f"| {db.years[i]:^7} | {round(y[i], 2):^11} |")
    print("-" * 25, col_sym.WHITE)

    # Pie
    footer = f"{col_sym.BRIGHT_CYAN}Total registros: {db.h}{col_sym.WHITE} "
    print(f"| {footer:<20}  |")
    print("-" * 25)
    print()

def linear_regression(x: list, a: float, b: float) -> list:
    y = []
    for datum in x:
        y.append(a * datum + b)
    return y

def MAE(y: list) -> float:
    s_mae = 0
    for i in range(db.h):
        s_mae += abs(db.enrolled_students[i] - y[i])
    return s_mae / db.h

def calculation_a() -> float:
    '''
    Calcular pendiente
    '''
    return (max(db.enrolled_students) - min(db.enrolled_students))  / (max(db.years) - min(db.years))

def calculation_b(a: float) -> float:
    '''
    Calcular intercepto
    '''
    return (min(db.enrolled_students) - a * min(db.years))

def estimating_students(x: int, a: float, b: float) -> float: 
    return a * x + b