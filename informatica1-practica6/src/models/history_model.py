import matplotlib.pyplot as plt
import src.utils.colors_symbols as col_sym
import src.config.database as db

def show_data(y: list, title: str) -> None:
    # Encabezado
    print("-" * 25)
    print(f"| {col_sym.BRIGHT_CYAN}{title:^20} {col_sym.WHITE} |")
    print("-" * 25)
    print(col_sym.BLUE, end="")
    print("-" * 25, col_sym.WHITE)
    print(f"| {col_sym.YELLOW}{'Año':^7}{col_sym.WHITE} ", end="")
    print(f"| {col_sym.YELLOW}{'Estudiantes':^11}{col_sym.WHITE}", end="")
    print(" |")
    print(col_sym.BLUE, end="")
    print("-" * 25, col_sym.WHITE)

    # Cuerpo
    for i in range(db.h):
        print(f"| {db.years[i]:^7} | {round(y[i], 2):^11} |")
    print("-" * 25, col_sym.WHITE)

    # Pie
    footer = f"{col_sym.BRIGHT_CYAN}Total registros: {db.h}{col_sym.WHITE} "
    print(f"| {footer:<20}  |")
    print("-" * 25)
    print()

def linear_regression(x: list, a: float, b: float) -> list:
    y = []
    for datum in x:
        y.append(a * datum + b)
    return y

def MAE(y: list) -> float:
    s_mae = 0
    for i in range(db.h):
        s_mae += abs(db.enrolled_students[i] - y[i])
    return s_mae / db.h

def calculate_slope() -> float:
    '''
    Calcular pendiente
    '''
    return (max(db.enrolled_students) - min(db.enrolled_students))  / (max(db.years) - min(db.years))

def calculate_intercept(a: float) -> float:
    '''
    Calcular intercepto
    '''
    return (min(db.enrolled_students) - a * min(db.years))

def estimating_students(x: int, a: float, b: float) -> float: 
    return a * x + b

def generate_plot(
        years: list, students: list, a: float, b: float, future_year: int, 
        estimation: float, mae: float, 
        filename: str = "assets/graphs/grafica_regresion.png"
) -> None:
    # 1. Crear el lienzo de la gráfica
    plt.figure(figsize=(10, 6))
    
    # 2. Dibujar los datos históricos reales (puntos azules)
    plt.scatter(years, students, color="blue", label="Datos históricos reales")
    
    # 3. Dibujar la línea de regresión desde el año inicial hasta el año futuro
    x_linea = years + [future_year]
    y_linea = [a * x + b for x in x_linea]
    plt.plot(x_linea, y_linea, color="red", label=f"Regresión lineal (y = {a:.2f}x + {b:+.2f}) | MAE: {mae:.2f}")
    
    # 4. Resaltar el punto específico estimado para el futuro (punto verde grande)
    plt.scatter([future_year], [estimation], color="green", s=100, zorder=5, label=f"Estimación {future_year}: {round(estimation)} est.")
    
    # 5. Personalizar títulos, ejes y leyenda
    plt.title("Proyección de Estudiantes Matriculados")
    plt.xlabel("Año")
    plt.ylabel("Cantidad de Estudiantes")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    
    # 6. Guardar la gráfica en un archivo (IMPORTANTE: hacerlo antes de plt.show())
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()  # Libera la memoria de la figura
