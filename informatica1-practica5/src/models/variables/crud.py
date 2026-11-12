import src.config.database as db
import src.utils.colors_symbols as col_sym
import src.utils.validations as valid
import src.utils.util as utl 


def read() -> None:
    '''
    Función para mostrar las variables
    '''
    
    print()
    print(f"{col_sym.YELLOW}Variables{col_sym.WHITE}")
    print(f"{col_sym.BLUE}", end='')
    print("-" * 62)
    print(f"| {'Variable':^13} | {'Mínimo':^12} " \
          f"| {'Máximo':^12} | {'Unidades':^12} |")
    print("-" * 62)
    print(f"{col_sym.WHITE}", end='')
    for variable, data in db.variables_data['variables'].items():
        print(f"| {variable:<14}", end='')
        for value in data.values():
            print(f"| {value:<12} ", end='')
        print("|")
        print("-" * 62)
    print("-" * 62)
    print(f"| {col_sym.GREEN}Total registros: " \
          f"{len(db.variables_data['variables']):<41}{col_sym.WHITE} |")
    print("-" * 62)
    print()
    