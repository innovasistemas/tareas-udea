# ----------------------------------------
# Programa: Ejercicio h) Cambiar espacios por guiones
# ----------------------------------------

# ----------------------------------------
# Definición de variables
# ----------------------------------------
# texto: Texto que el usuario ingresa
# i: Variable iteradora

print("\n\033[32m", "-" * 44, "\033[0m")
print("\033[32m", "-" * 13, "Cambiar Espacios" ,"-" * 13, "\033[0m")
print("\033[32m", "-" * 44, "\033[0m")
texto = input("Texto: ")
i = 0
n = len(texto)
if n > 0:
    while i < n:
        if texto[i] == " ":
            texto = texto[:i] + "-" + texto[i+1:]
        else:
            i = i + 1
    print("\033[33m", end = "")
    print(f"Texto sin espacios y con guiones: {texto}")
    print("\033[0m")
else:
    print("\n")
    print("\033[31m")
    print("-" * 38)
    print("¡Error! No ingresó el texto")
    print("-" * 38)
    print("\033[0m")