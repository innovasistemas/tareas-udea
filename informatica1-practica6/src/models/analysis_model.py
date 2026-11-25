import random
import time
import src.utils.util as utl
import src.utils.colors_symbols as col_sym

vector = []
n = 0

def fill_vector() -> None:
    vector.clear()
    for i in range(n):
        vector.append(random.randint(1, n))

def show_vector() -> None:
    print("| ", end="")
    for elem in vector:
        print(f"{col_sym.GREEN}{elem:^5}{col_sym.WHITE} |", end="")
    print()

def sort(method: str = '') -> None:
    if n > 0:
        start_time = time.time()
        match method:
            case "Burbuja":
                bubble_sort()
            case "Selección":
                selection_sort()
            case "Inserción":
                insertion_sort()
            case "Fusión":
                merge_sort(0, n - 1)
            case "Aleatorio":
                sort_random()
        message = f"Método de ordenación usado para el arreglo: {method} " \
                  f"\nTiempo total del sistema para {n} datos: " \
                  f"{round(time.time() - start_time, 2)}s"
        utl.systemMessage(message)
        complexity(method)
    else:
        utl.systemMessage("No ha llenado el arreglo", "warning")

def bubble_sort() -> None:
    for i in range(n - 1):
        for j in range(i + 1, n):
            if vector[i] > vector[j]:
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux 

def selection_sort() -> None:
    for i in range(n):
        minimum = vector[i]
        k = i 
        for j in range(i + 1, n):
            if vector[j] < minimum:
                minimum = vector[j]
                k = j
        aux = vector[i]
        vector[i] = vector[k]
        vector[k] = aux

def insertion_sort() -> None:
    for i in range(1, n):
        aux = vector[i]
        k = i - 1
        while k >= 0 and aux < vector[k]:
            vector[k + 1] = vector[k]
            k -= 1
        vector[k + 1] = aux

def merge_sort(left: int, right: int) -> None:
    if left < right:
        medium = left + (right - left) // 2
        merge_sort(left, medium)
        merge_sort(medium + 1, right)
        set_merge(left, medium, right)

def set_merge(left: int, medium: int, right:int) -> None:
    n1 = medium - left + 1
    n2 = right - medium
    list_left = [] 
    list_right = [] 

    for i in range(n1):
        list_left.append(vector[left + i])
    
    for i in range(n2):
        list_right.append(vector[medium + 1 + i])

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if list_left[i] <= list_right[j]:
            vector[k] = list_left[i]
            i += 1
        else:
            vector[k] = list_right[j]
            j += 1
        k += 1

    while i < n1:
        vector[k] = list_left[i]
        i += 1
        k += 1
    
    while j < n2:
        vector[k] = list_right[j]
        j += 1
        k += 1

def sort_random() -> None:
    random.shuffle(vector)

def complexity(method: str = '') -> None:
    match method:
        case "Burbuja":
            print("-" * 67)
            print(f"| {col_sym.YELLOW}{'Algoritmo Burbuja':^35} | {'Contador Frecuencias (CF)':^25}{col_sym.WHITE} |")
            print("-" * 67)
            print(f"| {'for i in range(n - 1):':<35} | {'--> n - 1':<25} |")
            print(f"| {'    for j in range(i + 1, n):':<35} | {'--> n - i':<25} |")
            print(f"| {'        if vector[i] > vector[j]:':<35} | {'--> n - i - 1':<25} |")
            print(f"| {'            aux = vector[i]':<35} | {'--> n - i - 1':<25} |")
            print(f"| {'            vector[i] = vector[j]':<35} | {'--> n - i - 1':<25} |")
            print(f"| {'            vector[j] = aux':<35} | {'--> n - i - 1':<25} |")
            print("-" * 67)
            print(f"| {col_sym.GREEN}{'Mejor caso (Big Omega): Ω(n²)':<35} | {'CF = n² + n - 2':<25}{col_sym.WHITE} |")
            print("-" * 67)
            print(f"| {col_sym.GREEN}{'Peor caso (Big O): O(n²)':<35} | {'CF = (5n² - n - 4)/2':<25}{col_sym.WHITE} |")
            print("-" * 67)
            print(f"| {col_sym.GREEN}{'Caso medio (Big Theta): θ(n²)':<35} | {'CF = (7n² + n - 8)/4':<25}{col_sym.WHITE} |")
            print("-" * 67)

            print()
            
            print("-" * 47)
            print(f"| {col_sym.YELLOW}{'i [0, n - 2]':^15} | {'j':^25}{col_sym.WHITE} |")
            print("-" * 47)
            print(f"| {'i = 0':^15} | {col_sym.WHITE}{'n':^25} |")
            print(f"| {'i = 1':^15} | {col_sym.WHITE}{'n - 1':^25} |")
            print(f"| {'i = 2':^15} | {col_sym.WHITE}{'n - 2':^25} |")
            print(f"| {'i = 3':^15} | {col_sym.WHITE}{'n - 3':^25} |")
            print(f"| {'...':^15} | {col_sym.WHITE}{'...':^25} |")
            print(f"| {'i = n - 2':^15} | {col_sym.WHITE}{'n - (n - 2) = 2':^25} |")
            print("-" * 47)
            print(f"| {col_sym.GREEN}{'Fórmula':<15} | {'∑(n - i) = ∑n - ∑i':<25}{col_sym.WHITE} |")
            print("-" * 47)
            print()

        case "Selección":
            print("-" * 67)
            print(f"| {col_sym.YELLOW}{'Algoritmo Selección':^35} | {'Contador Frecuencias (CF)':^20}{col_sym.WHITE} |")
            print("-" * 67)
            print(f"| {'for i in range(n):':<35} | {'--> n + 1':<25} |")
            print(f"| {'    minimum = vector[i]':<35} | {'--> n':<25} |")
            print(f"| {'    k = i':<35} | {'--> n':<25} |")
            print(f"| {'    for j in range(i + 1, n):':<35} | {'--> n - i':<25} |")
            print(f"| {'        if vector[j] < minimum:':<35} | {'--> n - i - 1':<25} |")
            print(f"| {'            minimum = vector[j]':<35} | {'--> n - i - 1':<25} |")
            print(f"| {'            k = j':<35} | {'--> n - i - 1':<25} |")
            print(f"| {'    aux = vector[i]':<35} | {'--> n':<25} |")
            print(f"| {'    vector[i] = vector[k]':<35} | {'--> n':<25} |")
            print(f"| {'    vector[k] = aux':<35} | {'--> n':<25} |")
            print("-" * 67)
            print(f"| {col_sym.GREEN}{'Mejor caso (Big Omega): Ω(n²)':<35} | {'CF = n² + 5n + 3':<25}{col_sym.WHITE} |")
            print("-" * 67)
            print(f"| {col_sym.GREEN}{'Peor caso (Big O): O(n²)':<35} | {'CF = 2n² + 5n + 4':<25}{col_sym.WHITE} |")
            print("-" * 67)
            print(f"| {col_sym.GREEN}{'Caso medio (Big Theta): θ(n²)':<35} | {'CF = (3n² + 10n + 7)/2':<25}{col_sym.WHITE} |")
            print("-" * 67)

            print()

            print("-" * 47)
            print(f"| {col_sym.YELLOW}{'i [0, n - 1]':^15} | {'j':^25}{col_sym.WHITE} |")
            print("-" * 47)
            print(f"| {'i = 0':^15} | {col_sym.WHITE}{'n':^25} |")
            print(f"| {'i = 1':^15} | {col_sym.WHITE}{'n - 1':^25} |")
            print(f"| {'i = 2':^15} | {col_sym.WHITE}{'n - 2':^25} |")
            print(f"| {'i = 3':^15} | {col_sym.WHITE}{'n - 3':^25} |")
            print(f"| {'...':^15} | {col_sym.WHITE}{'...':^25} |")
            print(f"| {'i = n - 1':^15} | {col_sym.WHITE}{'n - (n - 1) = 1':^25} |")
            print("-" * 47)
            print(f"| {col_sym.GREEN}{'Fórmula':<15} | {'∑(n - i) = ∑n - ∑i':<25}{col_sym.WHITE} |")
            print("-" * 47)
            print()

        case "Inserción":
            print("-" * 69)
            print(f"| {col_sym.YELLOW}{'Algoritmo Inserción':^37} | {'Contador Frecuencias (CF)':^25}{col_sym.WHITE} |")
            print("-" * 69)
            print(f"| {'for i in range(1, n):':<37} | {'--> n':<25} |")
            print(f"| {'    aux = vector[i]':<37} | {'--> n - 1':<25} |")
            print(f"| {'    k = i - 1':<37} | {'--> n - 1':<25} |")
            print(f"| {'    while k >= 0 and aux < vector[k]:':<37} | {'--> n - 1 | n - i':<25} |")
            print(f"| {'        vector[k + 1] = vector[k]':<37} | {'--> n - i - 1':<25} |")
            print(f"| {'        k -= 1':<37} | {'--> n - i - 1':<25} |")
            print(f"| {'    vector[k + 1] = aux':<37} | {'--> n - 1':<25} |")
            print("-" * 69)
            print(f"| {col_sym.GREEN}{'Mejor caso (Big Omega): Ω(n)':<37} | {'CF = 5n - 4':<25}{col_sym.WHITE} |")
            print("-" * 69)
            print(f"| {col_sym.GREEN}{'Peor caso (Big O): O(n²)':<37} | {'CF = (3n² + n - 2)/2':<25}{col_sym.WHITE} |")
            print("-" * 69)
            print(f"| {col_sym.GREEN}{'Caso medio (Big Theta): θ(n²)':<37} | {'CF = (3n² + 11n - 10)/4':<25}{col_sym.WHITE} |")
            print("-" * 69)

            print()

            print("-" * 47)
            print(f"| {col_sym.YELLOW}{'i [1, n - 1]':^15} | {'j':^25}{col_sym.WHITE} |")
            print("-" * 47)
            print(f"| {'i = 0':^15} | {col_sym.WHITE}{'n':^25} |")
            print(f"| {'i = 1':^15} | {col_sym.WHITE}{'n - 1':^25} |")
            print(f"| {'i = 2':^15} | {col_sym.WHITE}{'n - 2':^25} |")
            print(f"| {'i = 3':^15} | {col_sym.WHITE}{'n - 3':^25} |")
            print(f"| {'...':^15} | {col_sym.WHITE}{'...':^25} |")
            print(f"| {'i = n - 1':^15} | {col_sym.WHITE}{'n - (n - 1) = 1':^25} |")
            print("-" * 47)
            print(f"| {col_sym.GREEN}{'Fórmula':<15} | {'∑(n - i) = ∑n - ∑i':<25}{col_sym.WHITE} |")
            print("-" * 47)
            print()

        case "Fusión":
            print("-" * 69)
            print(f"| {col_sym.YELLOW}{'Algoritmo Fusión':^37} | {'Contador Frecuencias (CF)':^25}{col_sym.WHITE} |")
            print("-" * 69)
            print("-" * 69)
            print(f"| {col_sym.GREEN}{'Mejor caso (Big Omega): Ω(nlg(n))':<37} | {'CF':<25}{col_sym.WHITE} |")
            print("-" * 69)
            print(f"| {col_sym.GREEN}{'Peor caso (Big O): O(nlg(n))':<37} | {'CF':<25}{col_sym.WHITE} |")
            print("-" * 69)
            print(f"| {col_sym.GREEN}{'Caso medio (Big Theta): θ(nlg(n))':<37} | {'CF':<25}{col_sym.WHITE} |")
            print("-" * 69)
            print()

    input(f"Presione Enter {col_sym.ENTER} para continuar...")