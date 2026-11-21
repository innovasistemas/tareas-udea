import src.utils.colors_symbols as col_sym
import src.config.database as db

averages = [0] * len(db.students)
count_courses = [0] * len(db.students)

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
    print("-" * (115))
    print(f"|{col_sym.BRIGHT_CYAN}{'Listado de Notas':^{115 - 2}}{col_sym.WHITE}|")
    print("-" * (115))
    print(col_sym.BLUE, end="")
    print("-" * (115), col_sym.WHITE)
    print("|", col_sym.MAGENTA, f"{'Estud/Curso':^11} ", col_sym.WHITE, end="")
    for i in range(db.n):
        print(f"| {col_sym.YELLOW}{db.courses[i]:^11}{col_sym.WHITE} \t", end="")
    print(" | ", col_sym.MAGENTA, f"{'Promedio':^10} ", col_sym.WHITE, end="")
    print(" |")
    print(col_sym.BLUE, end="")
    print("-" * (115), col_sym.WHITE)

    # Cuerpo
    for i in range(db.m):
        print(f"| {col_sym.GREEN}{db.students[i]:^11}{col_sym.WHITE}\t", end="")
        for j in range(db.n):
            print(f"| {db.grades[i][j]:^11}\t", end="")
        # print(f" | {col_sym.GREEN}{count_courses[i]:^15}{col_sym.WHITE}", end="")
        if averages[i] >= 3:
            print(f" | {col_sym.GREEN}{round(averages[i], 2):^14}{col_sym.WHITE}", end="")
        else:
            print(f" | {col_sym.RED}{round(averages[i], 2):^14}{col_sym.WHITE}", end="")
        print(" |")
    print(col_sym.BLUE, end="")
    print("-" * (115), col_sym.WHITE)

    # Pie
    footer = f"{col_sym.BRIGHT_CYAN}Total registros: {db.m}{col_sym.WHITE}"
    print(f"| {footer:<121} |")
    print("-" * (115))
    print()

def delete_item(index) -> None:
    del db.students[index]
    del db.grades[index]
    db.m = len(db.students)

def average_count_grades_student(list_data, index) -> None:
    s = 0
    c = 0
    for item in list_data:
        if float(item) >= 0:
            s += float(item)
            c += 1
    averages[index] = s / c if c > 0 else -1
    count_courses[index] = c

def student_average_count() -> None:
    for index, grade in enumerate(db.grades): 
        average_count_grades_student(grade, index)

def sort_bubble_desc() -> None:
    for i in range(db.m - 1):
        for j in range(i + 1, db.m):
            if averages[i] < averages[j]:
               interchange(i, j) 

def sort_selection() -> None:
    for i in range(db.m):
        minimum = count_courses[i]
        k = i 
        for j in range(i + 1, db.m):
            if count_courses[j] < minimum:
                minimum = count_courses[j]
                k = j
        interchange(i, k)

def interchange(i, j) -> None:
    aux = averages[i]
    averages[i] = averages[j]
    averages[j] = aux
    
    aux = count_courses[i]
    count_courses[i] = count_courses[j]
    count_courses[j] = aux
    
    aux = db.students[i]
    db.students[i] = db.students[j]
    db.students[j] = aux
    
    aux_grade = db.grades[i]
    db.grades[i] = db.grades[j]
    db.grades[j] = aux_grade
            
def max_grade_student(index) -> dict:
    maximum = {}
    maximum['codigo'] = db.courses[0]
    maximum['nota'] = db.grades[index][0]
    for i in range(1, db.n): 
        if db.grades[index][i] > maximum['nota']:
            maximum['codigo'] = db.courses[i]
            maximum['nota'] = db.grades[index][i]
    return maximum