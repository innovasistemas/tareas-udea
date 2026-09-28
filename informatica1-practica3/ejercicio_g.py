# ----------------------------------------
# Programa: Ejercicio g) Triángulo numérico
# ----------------------------------------

# ----------------------------------------
# Definición de variables
# ----------------------------------------
# num: Número entero para 
# i, j: Variables iteradoras

print("\n\033[32m", "-" * 42, "\033[0m")
print("\033[32m", "-" * 11, "Triángulo Numérico" ,"-" * 11, "\033[0m")
print("\033[32m", "-" * 42, "\033[0m")
num = int(input("Número entero: "))

if num > 0:
    for i in range(1, num + 1):
        print(" " * (num - i), end="")
        for j in range(1, i + 1):
            print(f"{j} ", end="")
        print("")
else:
    print("\n")
    print("\033[31m")
    print("-" * 53)
    print("¡Error! Número no válido")
    print("-" * 53)
    print("\033[0m")