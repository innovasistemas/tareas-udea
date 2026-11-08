import src.utils.util as utl
import src.utils.colors_symbols as col_sym
import src.users.authentication as auth 
import src.menus.admin_menu as adm_mnu
import src.menus.operator_menu as oper_mnu
import src.menus.guest_menu as gue_mnu

def main_menu() -> None:
    '''
    Función para desplegar el menú principal
    '''
    
    option = ""
    while option != "0":
        print(col_sym.GREEN + "-" * 27)
        print("|      Menú Principal     |")
        print("-" * 27 + col_sym.WHITE)
        print("-" * 27)
        print(f"|  {col_sym.RED}0.{col_sym.WHITE} Salir del sistema   |")
        print(f"|  {col_sym.RED}1.{col_sym.WHITE} Usuario registrado  |")
        print(f"|  {col_sym.RED}2.{col_sym.WHITE} Usuario visitante   |")
        print("-" * 27)
        option = input(f"{col_sym.YELLOW}Ingresar opción:{col_sym.WHITE} ")
        print()

        match option:
            case "0":
                utl.systemMessage("Programa finalizado")
            case "1":
                auth.authentication()
                if 'rol' in auth.user_auth and auth.user_auth['rol'].lower() == "administrador":
                    utl.systemMessage("Ingreso concedido para Administrador", "success")
                    adm_mnu.admin_menu()
                elif 'rol' in auth.user_auth and auth.user_auth['rol'].lower() == "operador":
                    utl.systemMessage("Ingreso concedido para Operador", "success")
                    oper_mnu.operator_menu()
                else:
                    utl.systemMessage(auth.user_auth['message']['error'], "error")
            case "2":
                auth.validate_credentials()
                gue_mnu.guest_menu()
            case _:
                utl.systemMessage("Opción no válida", "error")