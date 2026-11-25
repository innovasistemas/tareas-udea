import src.utils.util as utl
import src.utils.colors_symbols as col_sym
import src.models.history_model as his_model 
import src.config.database as db

def history_menu() -> None:
    '''
    Función para desplegar el menú de históricos
    '''
    a = 0
    b = 0
    mae = 0
    y_estim = []
    option = ""
    while option != "0":
        print(col_sym.GREEN + "-" * 32)
        print(f"| {'Menú Histórico Matrículas':^28} |")
        print("-" * 32 + col_sym.WHITE)
        print("-" * 32)
        print(f"|  {col_sym.RED}0.{col_sym.WHITE} Regresar                 |")
        print(f"|  {col_sym.RED}1.{col_sym.WHITE} Ver Histórico Matrículas |")
        print(f"|  {col_sym.RED}2.{col_sym.WHITE} Regresión Lineal         |")
        print(f"|  {col_sym.RED}3.{col_sym.WHITE} Predecir Matrículas      |")
        print("-" * 32)
        option = input(f"{col_sym.YELLOW}Ingresar opción:{col_sym.WHITE} ")
        print()

        match option:
            case "0":
                pass
            case "1":
                his_model.show_data(db.enrolled_students, "Histórico Matrículas")
            case "2":
                print("Parámetros de ajuste a la regresión lineal")
                a = his_model.calculation_a()
                b = his_model.calculation_b(a)
                y_estim = his_model.linear_regression(db.years, a, b)
                mae = his_model.MAE(y_estim)
                utl.systemMessage(f"a = {round(a, 2)}\nb = {round(b, 2)}" \
                                  f"\nMean Absolute Error: MAE = {round(mae, 2)}")
                his_model.show_data(y_estim, "Regresión Lineal")
            case "3":
                print("Estimar estudiantes matriculados")
                try:
                    year = int(input("Ingrese un año futuro: "))
                    if year > max(db.years):
                        estimation = his_model.estimating_students(year, a, b)
                        utl.systemMessage(f"Estudiantes estimados para el año {year}: {estimation:.0f}" \
                                          f"\nMean Absolute Error: MAE = {mae:.2f}" )
                    else:
                        utl.systemMessage(f"Año no válido. Debe ingresar un año mayor a {max(db.years)}", "warning")
                except ValueError:
                    utl.systemMessage(f"Año no válido. Debe ingresar un año mayor a {max(db.years)}", "warning")
            case _:
                utl.systemMessage("Opción no válida", "error")