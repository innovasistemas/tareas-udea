# Datos para pruebas
# students = ['10000', '30000', '40000', '50000']
# courses = ["Aritmética", "Cálculo", "Ecuaciones", "Álgebra", "Estadística", "Informática"]
# grades = [
#         [3.9, 3.8, 3.3, 4.5, 4.1, 1.1],
#         [4.0, 4.3, 4.7, 3.5, 4.0, -1],
#         [4.0, 4.3, 4.7, 3.5, 4.0, -1],
#         [3.0, 1.3, 2.8, 2.6, 4.2, 2.1]
#     ]
# grades = [
#         [3.9, 3.8, 3.3, 4.5, 4.1, 1.1],
#         [4.0, 4.3, 4.7, 3.5, 4.0, -1],
#         [4.0, 4.3, 4.7, 3.5, 4.0, -1],
#         [-2, -1, 4.6, 4.5, 4.8, 2.1],
#         [3.0, 1.3, 2.8, 2.6, 4.2, 2.1],
#         [-2, -1, 4.6, 4.5, 4.8, 2.1],
#         [3.0, 1.3, 2.8, 2.6, 4.2, 2.1]
#     ]

students = []
courses = []
grades = []
enrolled_students = []
years = []


def load_data_csv():
    '''
    Función para cargar los archivos csv en memoria
    '''
    
    global students, courses, grades, enrolled_students, years

    file = open("assets/database/notas_estudiantes.csv", "r", encoding="utf-8")
    l = 0
    for line in file:
        if l == 0:
            courses = line.split(",")
            # Quitar el \n del final de la línea en el archivo csv
            courses[4] = courses[4][:len(courses[4]) - 1]
        elif l == 1:
            students = line.split(",")
            students[6] = students[6][:len(students[6]) - 1]
        else:
            notes = line.split(",")
            notes[4] = notes[4][:len(notes[4]) - 1]
            grades.append(notes)
        l += 1
    file.close()

    file = open("assets/database/hist_matriculados.csv", "r", encoding="utf-8")
    l = 0
    for line in file:
        if l != 0:
            aux_data = line.split(",")
            # Quitar el \n del final de la línea en el archivo csv
            aux_data[1] = aux_data[1][:len(aux_data[1]) - 1]
            years.append(int(aux_data[0]))
            enrolled_students.append(int(aux_data[1]))
        l += 1
    file.close()

load_data_csv()
m = len(students)
n = len(courses)
h = len(enrolled_students)

