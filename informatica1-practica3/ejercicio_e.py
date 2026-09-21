# ----------------------------------------
# Programa: Ejercicio e) Primos en intervalo
# ----------------------------------------

# ----------------------------------------
# Definición de variables
# ----------------------------------------
# li: Límite inferior del intervalo
# ls: Límite superior del intervalo
# i: Variable iteradora para recorrer el intervalo
# sw: Variable booleana. Permite conocer si un número no es primo
# existe_primo: Variable booleana. Permite conocer si hay primos en el intervalo

print("\n\033[32m", "-" * 38, "\033[0m")
print("\033[32m", "-" * 11, "Números Primos" ,"-" * 11, "\033[0m")
print("\033[32m", "-" * 38, "\033[0m")
li = int(input("Límite inferior: "))
ls = int(input("Límite superior: "))
if li > 1 and ls > 1 and ls >= li:
    print(f"Intervalo definido: [{li}, {ls}]")
    existe_primo = False
    print("\033[33m", end = "")
    print("Número Primos en el intervalo")
    print("\033[0m", end = "")
    for i in range(li, ls + 1, 1):
        sw = True
        j = 2
        while sw and j <= i ** (1/2):
            if i % j == 0:
                sw = False
            else:
                j+=1
        if sw:
            existe_primo = True
            print("\033[33m", end = "")
            print(i, end = ", ")
            print("\033[0m", end = "")
    if not existe_primo:
        print("\033[33m", end = "")
        print("No hay números primos en este intervalo")
        print("\033[0m", end = "")
else:
    print("\n")
    print("\033[31m")
    print("-" * 41)
    print("¡Error!")
    print("Los límites del intervalo deben ser mayores a 1")
    print("El límite inferior debe ser menor que el límite superior")
    print("-" * 41)
    print("\033[0m")
