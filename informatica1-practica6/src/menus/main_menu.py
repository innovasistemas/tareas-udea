import src.utils.util as utl
import src.utils.colors_symbols as col_sym
import src.menus.student_menu as std_menu
import src.menus.history_menu as his_menu
import src.menus.analysis_menu as anl_menu

def main_menu() -> None:
    '''
    Función para desplegar el menú principal
    '''
    
    option = ""
    while option != "0":
        print(col_sym.GREEN + "-" * 32)
        print(f"| {'Menú Principal':^28} |")
        print("-" * 32 + col_sym.WHITE)
        print("-" * 32)
        print(f"|  {col_sym.RED}0.{col_sym.WHITE} Salir del sistema        |")
        print(f"|  {col_sym.RED}1.{col_sym.WHITE} Estudiantes              |")
        print(f"|  {col_sym.RED}2.{col_sym.WHITE} Análisis Algoritmos      |")
        print(f"|  {col_sym.RED}3.{col_sym.WHITE} Histórico Matrículas     |")
        print("-" * 32)
        option = input(f"{col_sym.YELLOW}Ingresar opción:{col_sym.WHITE} ")
        print()

        match option:
            case "0":
                utl.systemMessage("Programa finalizado")
            case "1":
                std_menu.student_menu()
            case "2":
                anl_menu.analysis_menu()
            case "3":
                his_menu.history_menu()
            case _:
                utl.systemMessage("Opción no válida", "error")