import src.utils.util as utl
import src.utils.colors_symbols as col_sym
import src.models.analysis_model as anl_model

def analysis_menu() -> None:
    '''
    Función para desplegar el menú de históricos
    '''
    
    option = ""
    while option != "0":
        print(col_sym.GREEN + "-" * 32)
        print(f"| {'Menú Análisis Algoritmos':^28} |")
        print("-" * 32 + col_sym.WHITE)
        print("-" * 32)
        print(f"|  {col_sym.RED}0.{col_sym.WHITE} Regresar                 |")
        print(f"|  {col_sym.RED}1.{col_sym.WHITE} Llenar arreglo aleatorio |")
        print(f"|  {col_sym.RED}2.{col_sym.WHITE} Mostrar arreglo          |")
        print(f"|  {col_sym.RED}3.{col_sym.WHITE} Ordenación Burbuja       |")
        print(f"|  {col_sym.RED}4.{col_sym.WHITE} Ordenación Selección     |")
        print(f"|  {col_sym.RED}5.{col_sym.WHITE} Ordenación Inserción     |")
        print(f"|  {col_sym.RED}6.{col_sym.WHITE} Ordenación Fusión        |")
        print(f"|  {col_sym.RED}7.{col_sym.WHITE} Ordenación aleatoria     |")
        print("-" * 32)
        option = input(f"{col_sym.YELLOW}Ingresar opción:{col_sym.WHITE} ")
        print()

        match option:
            case "0":
                pass
            case "1":
                try:
                    n = int(input("Valor de n: "))
                    if n > 0:
                        anl_model.n = int(n)
                        anl_model.fill_vector()
                        utl.systemMessage(f"Arreglo llenado con {n} datos")
                    else:
                        utl.systemMessage("Debe ingresar un entero positivo", "warning")
                except ValueError: 
                    utl.systemMessage(f"Debe ingresar un entero positivo", "warning")
            case "2":
                if anl_model.n > 0:
                    anl_model.show_vector()
                else:
                    utl.systemMessage("No ha llenado el arreglo", "warning")
            case "3":
                if anl_model.n > 0:
                    anl_model.sort_bubble()
                    utl.systemMessage("Arreglo ordenado por el método de Burbuja")
                else:
                    utl.systemMessage("No ha llenado el arreglo", "warning")
            case "4":
                if anl_model.n > 0:
                    anl_model.sort_selection()
                    utl.systemMessage("Arreglo ordenado por el método de Selección")
                else:
                    utl.systemMessage("No ha llenado el arreglo", "warning")
            case "5":
                pass
            case "6":
                pass
            case "7":
                if anl_model.n > 0:
                    anl_model.sort_random()
                    utl.systemMessage("Arreglo dispuesto aleatoriamente")
                else:
                    utl.systemMessage("No ha llenado el arreglo", "warning")
            case _:
                utl.systemMessage("Opción no válida", "error")