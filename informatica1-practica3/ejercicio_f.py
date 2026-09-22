# ----------------------------------------
# Programa: Ejercicio f) Triángulo rectángulo
# ----------------------------------------

# ----------------------------------------
# Definición de variables
# ----------------------------------------
# h: Altura del triángulo rectángulo
# i: Variable iteradora

print("\n\033[32m", "-" * 44, "\033[0m")
print("\033[32m", "-" * 11, "Triángulo Rectángulo" ,"-" * 11, "\033[0m")
print("\033[32m", "-" * 44, "\033[0m")

h = int(input("Altura del triángulo rectángulo: "))
if h > 0:
    print("\033[33m", end = "")
    for i in range(1, h + 1, 1):
        print(" " * (h - i), end="")
        print("*" * i)
    print("\033[0m", end = "")
else:
    print("\n")
    print("\033[31m")
    print("-" * 38)
    print("¡Error! La altura debe ser mayor a cero")
    print("-" * 38)
    print("\033[0m")