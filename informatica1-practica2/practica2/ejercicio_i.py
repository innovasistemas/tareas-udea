# ----------------------------------------
# Programa: Ejercicio i)
# ----------------------------------------

# ----------------------------------------
# Definición de variables
# ----------------------------------------
# caracter: Carácter que se le pide al usuario
# vocales: Guarda la cadena 'aeiou' para verificar si el carácter ingresado se encuentra en ella
# tipo_caracer: Guarda el tipo de carácter ingresado: Vocal, Consonante, Dígito, Otro
# tipo_letra: Guarda el estado de la letra: Mayúscula o Minúscula 
# es_letra: Variable lógica para determinar si es el carácter ingresado es letra

# Datos de entrada e inicialización de variables 
vocales = "aeiou"
tipo_letra = ""
es_letra = False
caracter = input("Ingrese un carácter [Vocal|Consonante|Dígito]: ").strip()

if len(caracter) == 1:
    caracter_aux = caracter.lower()
    if 48 <= ord(caracter) <= 57:
        tipo_caracter = "Dígito"
    elif 65 <= ord(caracter) <= 90:
        es_letra = True
        tipo_letra = "Mayúscula"
    elif 97 <= ord(caracter) <= 122:
        es_letra = True
        tipo_letra = "Minúscula"
    else:
        tipo_caracter = "-"
    
    if es_letra:
        if caracter_aux in vocales:
            tipo_caracter = "Vocal"
        else:
            tipo_caracter = "Consonante"

    print("Entrada: ", caracter)
    print("Salida: ", tipo_caracter, tipo_letra)
else:
    print("La cadena ingresada debe tener sólo un carácter")     
