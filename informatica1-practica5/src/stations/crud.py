import src.config.database as db 
import src.utils.colors_symbols as col_sym
import src.utils.validations as valid
import src.utils.util as utl 

seq_id = ""
name = ""

def read(id = "") -> None:
    '''
    Función para mostrar uno o todos los registros
    '''
    
    print(col_sym.BLUE)
    print("-" * 60)
    print(f"| {'Código':^10} | {'Nombre':^43} |")
    print("-" * 60)
    print(col_sym.WHITE)
    if id == "":
        for stat_id, stat_data in db.stations_data.items():
            print(f"| {stat_id:<10} | {stat_data['nombre']:<43} |")
        total_records = len(db.stations_data)
    elif id in db.stations_data:
        print(f"| {id:<10} | {db.stations_data[id]['nombre']:<43} |")
        total_records = 1
    else:
        print(f"| {'Esta estación no está registrada':<56} |")
        total_records = 0
    print("-" * 60)
    print(f"| {col_sym.GREEN}Total registros: {total_records:<39}{col_sym.WHITE} |")
    print("-" * 60)
    print()

def create() -> None:
    '''
    Función para crear un nuevo registro
    '''

    global seq_id

    input_data()
    message = data_validation()
    if message == 'ok':
        # Establecer autonumérico y guardar datos
        seq_id =  \
            '1' if len(db.stations_data) == 0 \
            else str(int(list(db.stations_data.keys())[-1]) + 1)
        save()
        utl.systemMessage(f"Registro guardado {db.stations_data[seq_id]}", "success")
    else:
        utl.systemMessage(f"{message}", "error")

def update() -> None:
    '''
    Función para modificar un registro
    '''

    select_id()
    message = confirm_operation()
    if message == 'ok':
        input_data()
        message = data_validation()
        if message == 'ok':
            save('update')
            update_record = {"código": seq_id} | db.stations_data[seq_id]
            utl.systemMessage(f"Registro actualizado {update_record}", "success")
        else:
                utl.systemMessage(f"{message}", "error")
    else:
        utl.systemMessage(f"{message}", "warning")

def delete() -> None:
    '''
    Función para eliminar un registro
    '''

    select_id()
    message = confirm_operation()
    if message == 'ok':
        deleted_record = {"código": seq_id} | db.stations_data.pop(seq_id)
        update_file()
        utl.systemMessage(f"Registro eliminado {deleted_record}", "success")
    else:
        utl.systemMessage(f"{message}", "warning")

def save(type_operation = "create") -> None:
    '''
    Función para guardar la información (en diccionario y en archivos
    de forma persistente)
    '''

    # Agregar registro al diccionario
    db.stations_data.update({
        seq_id: {"nombre": name}
    })

    if type_operation == "create":
        # Agregar registro al archivo csv
        str_record = f"{seq_id},{name}\n"
        file = open("assets/data_base/estaciones.csv", "a", encoding="utf-8")
        file.write(str_record)
        file.close()
    else:
        update_file()

def update_file() -> None:
    '''
    Función para actualizar el archivo
    '''

    # Crear el contenido para el archivo
    content_file = "codigo,nombre\n"
    for seq, station_data in db.stations_data.items():
        content_file += f"{seq},{station_data['nombre']}\n"

    file = open("assets/data_base/estaciones.csv", "w", encoding="utf-8")
    file.write(content_file)
    file.close()

def input_data() -> None:
    '''
    Función para el ingreso de datos por teclado
    '''

    global name
    
    print(f"{col_sym.YELLOW}Ingresar datos de la Estación{col_sym.WHITE}")
    name = input("Nombre estación: ").strip()

def select_id() -> None:
    '''
    Función para seleccionar el identificador del archivo
    '''
    
    global seq_id

    print(f"{col_sym.YELLOW}Seleccione una estación del listado{col_sym.WHITE}")
    read()
    seq_id = input("Código: ").strip()

def data_validation() -> str:
    '''
    Función para validación de datos que usa el módulo validations
    '''

    if not valid.is_alphabetic_string(name):
        return "El nombre solo puede contener letras y espacios y no puede estar vacío"
    return 'ok'

def confirm_operation() -> str:
    '''
    Función para confirmar si es posible editar/eliminar y si está seguro de hacerlo
    '''
    
    if not seq_id in db.stations_data:
        return "El registro especificado no existe"

    resp = input("¿Está seguro de editar este registro? [S/N]: ")
    if resp.lower() == 's':
        return 'ok'
    
    return "Operación cancelada"   
