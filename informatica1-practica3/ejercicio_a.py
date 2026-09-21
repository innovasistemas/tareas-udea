# ----------------------------------------
# Programa: Ejercicio a) Calculadora básica
# ----------------------------------------

# ----------------------------------------
# Definición de variables
# ----------------------------------------
# A, B: números ingresados por el usuario para ser operados
# opcion: variable para capturar la opción del menú ingresada por el usuario

opcion = ""
A = 0
B = 0

while opcion != "7":
    print("-" * 10 + "Menú de opciones" + "-" * 10)
    print("1. Ingresar A y B")
    print("2. Valores actuales de A y B")
    print("3. Multiplicación")
    print("4. Residuo de A / B")
    print("5. A ^ B")
    print("6. Mayor de los dos números")
    print("7. Salir")
    opcion = input("Ingrese su opción: ")

    # match opcion:
    #     case "1":
    #         A = float(input("Ingrese A: "))
    #         B = float(input("Ingrese B: "))
    #     case "2":
    #         print(f"A = {A} \t B = {B}")
    #     case "3":
    #         operacion = A * B
    #         print(f"{A} * {B} = {operacion}")
    #     case "4":
    #         if B != 0:
    #             operacion = A % B
    #             print(f"{A} % {B} = {operacion}")
    #         else: 
    #             print("¡Error! División por cero")
    #     case _:
    #         print("Opción no válida") 


    if opcion == "1":
        A = float(input("Ingrese A: "))
        B = float(input("Ingrese B: "))
    elif opcion == "2":
        print(f"A = {A} \t B = {B}")
    elif opcion == "3":
        operacion = A * B
        print(f"{A} * {B} = {operacion}")
    elif opcion == "4":
        if B != 0:
            operacion = A % B
            print(f"{A} % {B} = {operacion}")
        else: 
            print("¡Error! División por cero")
    elif opcion == "5":
            if A == 0 and B == 0:
                print(f"{A} ^ {B} no está definido")
            else:
                operacion = A ** B
                print(f"{A} ^ {B} = {operacion}")
    elif opcion == "6":
        operacion = max(A, B)
        print(f"mayor({A},  {B}) = {operacion}")
    elif opcion == "7":
        print("Programa finalizado")
    else: 
        print("Opción no válida")    


