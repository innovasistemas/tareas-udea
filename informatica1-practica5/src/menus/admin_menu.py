import src.utils.util as utl
import src.utils.colors_symbols as col_sym
import src.menus.station_menu as st_mnu
import src.menus.user_menu as usr_mnu
import src.models.users.authentication as auth

def admin_menu() -> None:
    '''
    Función para desplegar el menú del usuario administrador
    '''

    opt = ""
    while opt != "0":
        auth.connected_user()
        print(col_sym.GREEN + "-" * 31)
        print("|      Menú Administrador     |")
        print("-" * 31 + col_sym.WHITE)
        print("-" * 31)
        print(f"|  {col_sym.RED}0.{col_sym.WHITE} Regresar                |")
        print(f"|  {col_sym.RED}1.{col_sym.WHITE} Gestionar Estaciones    |")
        print(f"|  {col_sym.RED}2.{col_sym.WHITE} Gestionar Usuarios      |")
        print(f"|  {col_sym.RED}3.{col_sym.WHITE} Depurar registros       |")
        print("-" * 31)
        opt = input(f"{col_sym.YELLOW}Ingresar opción:{col_sym.WHITE} ")
        print()

        match opt:
            case "0":
                pass
            case "1":
                st_mnu.station_menu()
            case "2":
                usr_mnu.user_menu()
                pass
            case "3":
                pass
            case _:
                utl.systemMessage("Opción no válida", "error")