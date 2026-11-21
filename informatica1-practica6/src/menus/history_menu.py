import src.utils.util as utl
import src.utils.colors_symbols as col_sym
import src.models.history_model as his_model 

def history_menu() -> None:
    '''
    Función para desplegar el menú de históricos
    '''
    
    option = ""
    while option != "0":
        print(col_sym.GREEN + "-" * 32)
        print(f"| {'Menú Histórico Matrículas':^28} |")
        print("-" * 32 + col_sym.WHITE)
        print("-" * 32)
        print(f"|  {col_sym.RED}0.{col_sym.WHITE} Regresar                 |")
        print(f"|  {col_sym.RED}1.{col_sym.WHITE} Ver Histórico Matrículas |")
        print("-" * 32)
        option = input(f"{col_sym.YELLOW}Ingresar opción:{col_sym.WHITE} ")
        print()

        match option:
            case "0":
                pass
            case "1":
                his_model.show_historical()
            case _:
                utl.systemMessage("Opción no válida", "error")