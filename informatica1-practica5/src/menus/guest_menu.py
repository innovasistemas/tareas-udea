import src.utils.util as utl
import src.utils.colors_symbols as col_sym
import src.users.authentication as auth

def guest_menu() -> None:
    '''
    Función para desplegar el menú del usuario visitante
    '''

    opt = ""
    while opt != "0":
        auth.connected_user()
        print(col_sym.GREEN + "-" * 26)
        print("|     Menú Visitante     |")
        print("-" * 26 + col_sym.WHITE)
        print("-" * 26)
        print(f"|  {col_sym.RED}0.{col_sym.WHITE} Regresar           |")
        print(f"|  {col_sym.RED}1.{col_sym.WHITE} Ver Estadísticas   |")
        print("-" * 26)
        opt = input(f"{col_sym.YELLOW}Ingresar opción:{col_sym.WHITE} ")
        print()

        match opt:
            case "0":
                pass
            case "1":
                statistics_submenu()
            case _:
                utl.systemMessage("Opción no válida", "error")


def statistics_submenu() -> None:
    '''
    Función para desplegar el submenú de visualización de estadísticas
    '''

    opt = ""
    while opt != "0":
        print(col_sym.GREEN + "-" * 28)
        print("|     Menú Estadísticas    |")
        print("-" * 28 + col_sym.WHITE)
        print("-" * 28)
        print(f"|  {col_sym.RED}0.{col_sym.WHITE} Regresar             |")
        print(f"|  {col_sym.RED}1.{col_sym.WHITE} Elegir Periodo       |")
        print(f"|  {col_sym.RED}2.{col_sym.WHITE} Elegir Variables     |")
        print(f"|  {col_sym.RED}3.{col_sym.WHITE} Modo Visualización   |")
        print("-" * 28)
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