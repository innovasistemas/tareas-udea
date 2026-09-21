# ----------------------------------------
# Programa: Ejercicio c) Primeros N términos de la serie de Fibonacci
# ----------------------------------------

# ----------------------------------------
# Definición de variables
# ----------------------------------------
# N: términos a mostrar de la serie Fibonacci
# t1, t2, t3: términos de la serie Fibonacci

print("\n\033[32m", "-" * 41, "\033[0m")
print("\033[32m", "-" * 12, "Serie Fibonacci" ,"-" * 12, "\033[0m")
print("\033[32m", "-" * 41, "\033[0m")
N = int(input("Total de términos a mostrar de la serie Fibonacci: "))
if N >= 2:
    t1 = 0
    t2 = 1
    print("\033[33m", end = "")
    print("Serie de Fibonacci", end = "\n")
    print(t1, t2, sep = ", ", end = "")
    print("\033[0m", end = "")
    for i in range(3, N + 1, 1):
        t3 = t1 + t2
        print("\033[33m", end = "")
        print(",", t3, end = "")
        print("\033[0m", end = "")
        t1 = t2
        t2 = t3
else:
    print("\n")
    print("\033[31m")
    print("-" * 53)
    print("¡Error! Debe especificar un valor mayor o igual a dos")
    print("-" * 53)
    print("\033[0m")