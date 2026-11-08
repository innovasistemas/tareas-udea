import src.config.database as db 
import src.utils.colors_symbols as col_sym

def list() -> None:
    print(col_sym.BLUE)
    print("-" * 60)
    print(f"| {'Identificación':<15} | {'Nombre':<21} | {'Rol':<14} |")
    print("-" * 60)
    print(col_sym.WHITE)
    for user_id, user_data in db.users_data.items():
        print(f"| {user_id:<15} |  {user_data['nombre']:<21}" \
              f"| {user_data['rol']:<14} |")

    print("-" * 60)
    print(f"| {col_sym.GREEN}Total registros: {len(db.users_data):<39}{col_sym.WHITE} |")
    print("-" * 60)
    print()