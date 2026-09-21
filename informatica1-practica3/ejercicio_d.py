# ----------------------------------------
# Programa: Ejercicio d) Binario a decimal
# ----------------------------------------

# ----------------------------------------
# Definición de variables
# ----------------------------------------
# nb: Número binario ingresado como cadena de caracteres
# nd: Número decimal equivalente
# i: Variable iteradora para recorrer la cadena de caracteres
# sw: Swiche. Permite conocer si el número ingresado contiene solo dígitos binarios
# b: Base binaria (2)
# n: Guarda el número de digitos binarios 

print("\n\033[32m", "-" * 41, "\033[0m")
print("\033[32m", "-" * 11, "Binario a Decimal" ,"-" * 11, "\033[0m")
print("\033[32m", "-" * 41, "\033[0m")
nb = input("Número binario: ")
n = len(nb)
i = 0
sw = True
# Verificar si nb es binario
while sw and i < n:
    if nb[i] != "0" and nb[i] != "1":
        sw = False
    else:
        i+=1
if sw:
    b = 2
    nd = 0
    for i in range(0, n, 1):
        nd += int(nb[i]) * b ** (n - i - 1)
    print("\033[33m", end = "")
    print(f"Binario a Decimal: \n{nb}(b2) = {nd}(b10)")
    print("\033[0m", end = "")
else:
    print("\n")
    print("\033[31m")
    print("-" * 41)
    print("¡Error! El número ingresado no es binario")
    print("-" * 41)
    print("\033[0m")

