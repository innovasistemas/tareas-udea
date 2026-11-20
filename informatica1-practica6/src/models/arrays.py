import src.utils.colors_symbols as col_sym
import src.config.database as db

averages = [0] * len(db.students)

def show_list(list_data, description) -> None:
    header = f"{col_sym.BRIGHT_CYAN}Listado de {description}{col_sym.WHITE}"
    print("-" * 34)
    print(f"| {header:^40} |")
    print("-" * 34)
    for index, datum in enumerate(list_data):
        course = f"{description[:len(description) - 1]} {index + 1}: {datum}"
        print(f"| {course:<30} |")
        print("-" * 34)
    footer = f"{col_sym.BRIGHT_CYAN}Total registros: {len(list_data)}{col_sym.WHITE}"
    print(f"| {footer:<40} |")
    print("-" * 34)
    print()

def show_grades() -> None:
    # Encabezado
    print("-" * (db.n * 22))
    print(f"|{col_sym.BRIGHT_CYAN}{'Listado de Notas':^{db.n * 22 - 2}}{col_sym.WHITE}|")
    print("-" * (db.n * 22))
    print(col_sym.BLUE, end="")
    print("-" * (db.n * 22), col_sym.WHITE)
    print("|", col_sym.MAGENTA, f"{'Estud/Curso':^11} ", col_sym.WHITE, end="")
    for i in range(db.n):
        print(f"| {col_sym.YELLOW}{db.courses[i]:^11}{col_sym.WHITE} \t", end="")
    print(" | ", col_sym.MAGENTA, f"{'Promedio':^11} ", col_sym.WHITE, end="")
    print(" |")
    print(col_sym.BLUE, end="")
    print("-" * (db.n * 22), col_sym.WHITE)

    # Cuerpo
    for i in range(db.m):
        print(f"| {col_sym.GREEN}{db.students[i]:^11}{col_sym.WHITE}\t", end="")
        for j in range(db.n):
            print(f"| {db.grades[i][j]:^11}\t", end="")
        if averages[i] >= 3:
            print(f" | {col_sym.GREEN}{round(averages[i], 2):^15}{col_sym.WHITE}", end="")
        else:
            print(f" | {col_sym.RED}{round(averages[i], 2):^15}{col_sym.WHITE}", end="")
        print(" |")
    print(col_sym.BLUE, end="")
    print("-" * (db.n * 22), col_sym.WHITE)

    # Pie
    footer = f"{col_sym.BRIGHT_CYAN}Total registros: {db.m}{col_sym.WHITE}"
    print(f"| {footer:<{db.n * 23}} |")
    print("-" * (db.n * 22))
    print()

def delete_item(index) -> None:
    del db.students[index]
    del db.grades[index]
    db.m = len(db.students)

def average_grades_student(list_data) -> float:
    s = 0
    c = 0
    for item in list_data:
        if item >= 0:
            s += item
            c += 1
    return s / c if c > 0 else -1

def student_average() -> None:
    for index, grade in enumerate(db.grades): 
        averages[index] = average_grades_student(grade)

def sort_bubble_desc() -> None:
    for i in range(db.m - 1):
        for j in range(i + 1, db.m):
            if averages[i] < averages[j]:
                aux = averages[i]
                averages[i] = averages[j]
                averages[j] = aux
                
                aux = db.students[i]
                db.students[i] = db.students[j]
                db.students[j] = aux
                
                aux_grade = db.grades[i]
                db.grades[i] = db.grades[j]
                db.grades[j] = aux_grade
                

    