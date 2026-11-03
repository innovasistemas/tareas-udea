import src.utils.util as utl
import src.utils.colors_symbols as col_sym


def operator_menu() -> None:
    '''
    Función para desplegar el menú del usuario operador
    '''

    opt = ""
    while opt != "0":
        print(col_sym.GREEN + "-" * 26)
        print("|      Menú Operador     |")
        print("-" * 26 + col_sym.WHITE)
        print("-" * 26)
        print(f"|  {col_sym.RED}0.{col_sym.WHITE} Regresar           |")
        print(f"|  {col_sym.RED}1.{col_sym.WHITE} Ingresar Medidas   |")
        print(f"|  {col_sym.RED}2.{col_sym.WHITE} Mostrar Medidas    |")
        print("-" * 26)
        opt = input(f"{col_sym.YELLOW}Ingresar opción:{col_sym.WHITE} ")

        match opt:
            case "0":
                pass
            case "1":
                pass
            case "2":
                pass
            case _:
                utl.systemMessage("Opción no válida", "error")