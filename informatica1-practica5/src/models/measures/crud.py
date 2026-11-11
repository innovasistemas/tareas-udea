import src.config.database as db
import src.models.stations.crud as station 
import src.utils.colors_symbols as col_sym
import src.utils.validations as valid
import src.utils.util as utl 

def read() -> None:
    '''
    Función para mostrar los registros asociados a una estación
    '''
    
    station.select_id()
    if station.seq_id in db.stations_data:
        if station.seq_id in db.measures_data:
            print(f"{col_sym.YELLOW}Estación seleccionada{col_sym.WHITE}")
            station.read(station.seq_id)
            print(f"{col_sym.YELLOW}Mediciones{col_sym.WHITE}")
            for variable, date in db.measures_data.get(station.seq_id, {}).items():
                print(f"Variable: {col_sym.YELLOW}{variable}{col_sym.WHITE}")
                for day, measure in date.items():
                    print(f"Día: {col_sym.GREEN}{day}{col_sym.WHITE}")
                    print(f"Medidas: {col_sym.BLUE}{measure}{col_sym.WHITE}")
                    print("-" * 50)

                print("-" * 50)
                print()
        else:
            utl.systemMessage("El registro especificado no tiene medidas registradas", "warning")
    else:
        utl.systemMessage("El registro especificado no existe", "warning")

