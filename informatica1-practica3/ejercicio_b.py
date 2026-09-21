# ----------------------------------------
# Programa: Ejercicio b) Divisores de un entero
# ----------------------------------------

# ----------------------------------------
# Definición de variables
# ----------------------------------------
# n: número entero
# i: variable iteradora

print("Programa: Divisores de n")

n = int(input("Ingrese un número entero: "))
n = abs(n)
if n > 0:
    print(f"Divisores positivos y negativos de {n}") 
    i = 1
    print("±", i, end = ", ")
    i+=1
    while i <= n // 2:
        if n % i == 0:
            print("±", i, end = ", ")
        i+=1
    print("±", n)
else:
    print("Infinitos divisores (¡Error! División por 0)")