import random
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

def sort_bubble() -> None:
    for i in range(n - 1):
        for j in range(i + 1, n):
            if vector[i] > vector[j]:
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux 

def sort_selection() -> None:
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

def sort_random() -> None:
    random.shuffle(vector)