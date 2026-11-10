import src.utils.util as utl
import src.utils.colors_symbols as col_sym
import src.users.authentication as auth
import src.users.crud as user 

def user_menu() -> None:
    '''
    Función para desplegar el submenú de gestión de usuarios 
    '''

    opt = ""
    while opt != "0":
        auth.connected_user()
        print(col_sym.GREEN + "-" * 22)
        print("|    Menú Usuarios   |")
        print("-" * 22 + col_sym.WHITE)
        print("-" * 22)
        print(f"|  {col_sym.RED}0.{col_sym.WHITE} Regresar       |")
        print(f"|  {col_sym.RED}1.{col_sym.WHITE} Nuevo          |")
        print(f"|  {col_sym.RED}2.{col_sym.WHITE} Editar         |")
        print(f"|  {col_sym.RED}3.{col_sym.WHITE} Eliminar       |")
        print(f"|  {col_sym.RED}4.{col_sym.WHITE} Buscar         |")
        print(f"|  {col_sym.RED}5.{col_sym.WHITE} Listar         |")
        print("-" * 22)
        opt = input(f"{col_sym.YELLOW}Ingresar opción:{col_sym.WHITE} ")
        print()

        match opt:
            case "0":
                pass
            case "1":
                user.create()
            case "2":
                pass
            case "3":
                pass
            case "4":
                id = input("Buscar por usuario por identificación: ")
                user.read(id)
            case "5":
                user.read()
            case _:
                utl.systemMessage("Opción no válida", "error")