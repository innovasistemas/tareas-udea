import src.utils.util as utl
import src.utils.colors_symbols as col_sym
import src.models.arrays as array
import src.config.database as db 

def main_menu() -> None:
    '''
    Función para desplegar el menú principal
    '''
    
    option = ""
    while option != "0":
        print(col_sym.GREEN + "-" * 32)
        print(f"| {'Menú Principal':^28} |")
        print("-" * 32 + col_sym.WHITE)
        print("-" * 32)
        print(f"|  {col_sym.RED}0.{col_sym.WHITE} Salir del sistema        |")
        print(f"|  {col_sym.RED}1.{col_sym.WHITE} Ver Estudiantes          |")
        print(f"|  {col_sym.RED}2.{col_sym.WHITE} Ver Cursos               |")
        print(f"|  {col_sym.RED}3.{col_sym.WHITE} Ver Notas                |")
        print(f"|  {col_sym.RED}4.{col_sym.WHITE} Eliminar Estudiante      |")
        print(f"|  {col_sym.RED}5.{col_sym.WHITE} Mejor Nota Estudiante    |")
        print(f"|  {col_sym.RED}6.{col_sym.WHITE} Ordenar por Promedios    |")
        print(f"|  {col_sym.RED}7.{col_sym.WHITE} Ordenar por Cant. Cursos |")
        print("-" * 32)
        option = input(f"{col_sym.YELLOW}Ingresar opción:{col_sym.WHITE} ")
        print()

        match option:
            case "0":
                utl.systemMessage("Programa finalizado")
            case "1":
                array.show_list(db.students, "Estudiantes")
            case "2":
                array.show_list(db.courses, "Cursos")
            case "3":
                array.student_average_count()
                array.show_grades()
            case "4":
                if db.m > 0:
                    datum = input("Estudiante a eliminar: ").strip()
                    if datum in db.students:
                        array.delete_item(db.students.index(datum))
                        utl.systemMessage(f"El estudiante [id={datum}] y sus notas " +
                                        "se eliminaron correctamente", "success")
                    else:
                        utl.systemMessage(f"El estudiante [id={datum}] " + 
                                          f"no se encuentra registrado", "warning")
                else:
                   utl.systemMessage(f"No hay estudiantes registrados", "warning") 
            case "5":
                if db.m > 0:
                    datum = input("Consultar mejor nota del estudiante: ").strip()
                    if datum in db.students:
                        maximum_grade = array.max_grade_student(db.students.index(datum))
                        utl.systemMessage(f"Estudiante [id={datum}] \n" +  
                                          f"Mejor nota: [nota={maximum_grade['nota']}] " +
                                          f"- Curso: [cod={maximum_grade['codigo']}] ", \
                                          "success")
                    else:
                        utl.systemMessage(f"El estudiante [id={datum}] " + 
                                          f"no se encuentra registrado", "warning")
                else:
                   utl.systemMessage(f"No hay estudiantes registrados", "warning") 
            case "6":
                array.student_average_count()
                array.sort_bubble_desc()
                utl.systemMessage("Datos ordenados (método burbuja)")
            case "7":
                array.student_average_count()
                array.sort_selection()
                utl.systemMessage("Datos ordenados (método selección)")
            case _:
                utl.systemMessage("Opción no válida", "error")