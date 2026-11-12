from datetime import date, datetime, timedelta
import src.utils.util as utl
import src.utils.colors_symbols as col_sym
import src.config.database as db
import src.models.users.authentication as auth
import src.models.variables.crud as var 

variable = ""
start_date = ""
end_date = ""

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

    global variable

    opt = ""
    while opt != "0":
        auth.connected_user()
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
                select_period()
                print(f"Fecha inicial: {col_sym.GREEN}{start_date}{col_sym.WHITE}")
                print(f"Fecha final: {col_sym.GREEN}{end_date}{col_sym.WHITE}")
            case "2":
                var.read()
                variable = input(f"{col_sym.YELLOW}Seleccione una variable: {col_sym.WHITE}").strip()
                if variable in db.variables_data['variables']:
                    print(f"Variable: {col_sym.GREEN}{variable}{col_sym.WHITE}")
                else:
                    utl.systemMessage("Variable especificada no válida", "warning")
            case "3":
                pass
            case _:
                utl.systemMessage("Opción no válida", "error")
        print()

def select_period() -> None:
    
    global start_date, end_date

    print(col_sym.GREEN + "-" * 28)
    print("|     Seleccionar Periodo    |")
    print("-" * 28 + col_sym.WHITE)
    print("-" * 28)
    print(f"|  {col_sym.RED}0.{col_sym.WHITE} Regresar             |")
    print(f"|  {col_sym.RED}1.{col_sym.WHITE} Últimos 7 días       |")
    print(f"|  {col_sym.RED}2.{col_sym.WHITE} Últimos 30 días      |")
    print(f"|  {col_sym.RED}3.{col_sym.WHITE} Fechas manualmente   |")
    print("-" * 28)
    period = input(f"{col_sym.YELLOW}Seleccione el periodo:{col_sym.WHITE} ")
    match period:
        case '0':
            pass
        case '1':
            end_date = date.today()
            start_date = end_date - timedelta(days=7)
        case '2':
            end_date = date.today()
            start_date = end_date - timedelta(days=30)
        case '3':
            start_date = input("Fecha inicio [yyyy-mm-dd]: ")
            end_date = input("Fecha fin [yyyy-mm-dd]: ")
        case _:
            utl.systemMessage("Periodo no válida", "warning")