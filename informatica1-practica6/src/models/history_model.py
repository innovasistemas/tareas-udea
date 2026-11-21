import src.utils.colors_symbols as col_sym
import src.config.database as db

def show_historical() -> None:
    # Encabezado
    print("-" * 25)
    print(f"| {col_sym.BRIGHT_CYAN}{'Histórico Matrículas':^20} {col_sym.WHITE} |")
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
        print(f"| {db.years[i]:^7} | {db.enrolled_students[i]:^11} |")
    print("-" * 25, col_sym.WHITE)

    # Pie
    footer = f"{col_sym.BRIGHT_CYAN}Total registros: {db.h}{col_sym.WHITE} "
    print(f"| {footer:<20}  |")
    print("-" * 25)
    print()