import src.config.database as db 
import src.utils.colors_symbols as col_sym
import src.utils.validations as valid
import src.utils.util as utl 

seq_id = ""
name = ""

def read(id = "") -> None:
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
    if input_data():
        save()
        utl.systemMessage(f"Registro guardado {db.stations_data[seq_id]}", "success")

def input_data() -> bool:
    '''
    Función para el ingreso de datos
    '''

    global name, seq_id
    
    print(f"{col_sym.YELLOW}Nueva Estación{col_sym.WHITE}")
    name = input("Nombre estación: ").strip()

    if validate_data():
        seq_id = '1' if len(db.stations_data) == 0 else str(len(db.stations_data) + 1)
        return True
    return False

def save() -> None:
    '''
    Función para guardar la información (en diccionario y en archivos
    de forma persistente)
    '''

    # Agregar registro al diccionario
    db.stations_data.update({
        seq_id: {"nombre": name}
    })

    # Agregar registro al archivo csv
    str_record = f"{seq_id},{name}\n"
    file = open("assets/data_base/estaciones.csv", "a", encoding="utf-8")
    file.write(str_record)
    file.close()

def validate_data() -> bool:
    '''
    Función para validación de datos que usa el módulo validations
    '''
    if valid.is_alphabetic_string(name):
        return True
    utl.systemMessage(f"El nombre solo puede contener letras y espacios " +
                    f"y no puede estar vacío", "error")   
    return False

    

    