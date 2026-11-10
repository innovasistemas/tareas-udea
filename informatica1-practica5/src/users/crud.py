import getpass
import src.config.database as db 
import src.utils.colors_symbols as col_sym
import src.utils.validations as valid
import src.utils.util as utl 
import src.users.authentication as auth

user_id = ""
name = ""
rol= ""
password = ""
confirm_password = ""

def read(id = "") -> None:
    '''
    Función para mostrar uno o todos los registros
    '''

    print(col_sym.BLUE)
    print("-" * 70)
    print(f"| {'Documento':^15} | {'Nombre':^31} | {'Rol':^14} |")
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
    '''
    Función para crear un nuevo registro
    '''
    
    input_data()
    message = data_validation()
    if message == 'ok':
        save()
        utl.systemMessage(f"Registro guardado {db.users_data[user_id]}", "success")
    else:
        utl.systemMessage(f"{message}", "error")

def delete() -> None:
    '''
    Función para eliminar un registro
    '''

    global user_id

    print(f"{col_sym.YELLOW}Seleccione un usuario del listado{col_sym.WHITE}")
    read()
    user_id = input("Documento: ").strip()
    message = confirm_deletion()
    if message == 'ok':
        deleted_record = {"documento": user_id} | db.users_data.pop(user_id)
        update_file()
        utl.systemMessage(f"Registro eliminado {deleted_record}", "success")
    else:
        utl.systemMessage(f"{message}", "warning")

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

def update_file() -> None:
    '''
    Función para actualizar el archivo
    '''

    # Crear el contenido para el archivo
    content_file = "codigo,nombre,clave,rol\n"
    for user, user_data in db.users_data.items():
        content_file += \
            f"{user},{user_data['nombre']},{user_data['clave']},{user_data['rol']}\n"

    file = open("assets/data_base/usuarios.csv", "w", encoding="utf-8")
    file.write(content_file)
    file.close()

def input_data() -> None:
    '''
    Función para el ingreso de datos por teclado
    '''

    global user_id, name, rol, password, confirm_password

    print(f"{col_sym.YELLOW}Nuevo Usuario{col_sym.WHITE}")
    user_id = input("Documento: ").strip()
    name = input("Nombre: ").strip()
    rol = input("Rol (Perfil) [1 -> Administrador | 2 -> Operador]: ").strip()
    password = getpass.getpass("Contraseña: ")
    confirm_password = getpass.getpass("Confirmar contraseña: ")

def data_validation() -> str:
    '''
    Función para validación de datos que usa el módulo validations
    '''

    global rol

    if len(user_id) != 10:
        return "El documento debe contener exactamante 10 dígitos"   

    if not valid.is_number(user_id):
        return "El documento solo puede contener caracteres numéricos"
    
    if user_id[0] == '0':
        return "El documento no puede comenzar con 0"

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

def confirm_deletion() -> str:
    '''
    Función para confirmar si es posible eliminar y si está seguro de eliminar
    '''
    
    if not user_id in db.users_data:
        return "El registro especificado no existe"

    if user_id == auth.user_auth["id"]:
        return "No puede autoeliminarse del sistema"

    resp = input("¿Está seguro de eliminar este registro? [S/N]: ")
    if resp.lower() == 's':
        return 'ok'
    
    return "Operación cancelada"
