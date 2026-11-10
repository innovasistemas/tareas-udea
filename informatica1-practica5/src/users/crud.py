import getpass
import src.config.database as db 
import src.utils.colors_symbols as col_sym
import src.utils.validations as valid
import src.utils.util as utl 

user_id = ""
name = ""
rol= ""
password = ""
confirm_password = ""

def read(id = "") -> None:
    print(col_sym.BLUE)
    print("-" * 70)
    print(f"| {'Identificación':^15} | {'Nombre':^31} | {'Rol':^14} |")
    print("-" * 70)
    print(col_sym.WHITE)
    if id == "":
        for user_id, user_data in db.users_data.items():
            print(f"| {user_id:<15} | {user_data['nombre']:<31} " \
                  f"| {user_data['rol']:<14} |")
        total_records = len(db.users_data)
    elif id in db.users_data:
        print(f"| {id:<15} | {db.users_data[id]['nombre']:<31} " \
              f"| {db.users_data[id]['rol']:<14} |")
        total_records = 1
    else:
        print(f"| {'Este usuario no está registrado':<56} |")
        total_records = 0
    print("-" * 70)
    print(f"| {col_sym.GREEN}Total registros: {total_records:<49}{col_sym.WHITE} |")
    print("-" * 70)
    print()

def create() -> None:
    input_data()
    message = validate_data()
    if message == 'ok':
        save()
        utl.systemMessage(f"Registro guardado {db.users_data[user_id]}", "success")
    else:
        utl.systemMessage(f"{message}", "error")

def input_data() -> None:
    '''
    Función para el ingreso de datos
    '''

    global user_id, name, rol, password, confirm_password

    print(f"{col_sym.YELLOW}Nuevo Usuario{col_sym.WHITE}")
    user_id = input("Identificación: ").strip()
    name = input("Nombre: ").strip()
    rol = input("Rol (Perfil) [1 -> Administrador | 2 -> Operador]: ").strip()
    password = getpass.getpass("Contraseña: ")
    confirm_password = getpass.getpass("Confirmar contraseña: ")

def save() -> None:
    '''
    Función para guardar la información (en diccionario y en archivos
    de forma persistente)
    '''

    # Agregar registro al diccionario
    db.users_data.update({
        user_id: {"nombre": name, "clave": password, "rol": rol}
    })

    # Agregar registro al archivo csv
    str_record = f"{user_id},{name},{password},{rol}\n"
    file = open("assets/data_base/usuarios.csv", "a", encoding="utf-8")
    file.write(str_record)
    file.close()

def validate_data() -> str:
    '''
    Función para validación de datos que usa el módulo validations
    '''

    global rol

    if len(user_id) != 10:
        return "La identificación debe contener exactamante 10 dígitos"   

    if not valid.is_number(user_id):
        return "La identificación solo puede contener caracteres numéricos"
    
    if user_id[0] == '0':
        return "La identificación no puede comenzar con 0"

    if user_id in db.users_data:
        return "Este usuario ya se encuentra registrado"
            
    if not valid.is_alphabetic_string(name):
        return "El nombre solo puede contener letras y espacios y no puede estar vacío"

    if rol == "1":
        rol = "Administrador"
    elif rol == "2":
        rol = "Operador"
    else:
        return "Rol no válido, debe indicar: [1 -> Administrador | 2 -> Operador]"

    if len(password.strip()) < 4:
        return "La contraseña debe contener al menos 4 caracteres"

    if password != confirm_password:
        return "La contraseña y su confirmación no coinciden"
        
    return 'ok'
