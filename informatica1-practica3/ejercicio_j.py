# ----------------------------------------
# Programa: Ejercicio j) Codificación de mensajes
# ----------------------------------------

# ----------------------------------------
# Definición de variables
# ----------------------------------------
# mensaje: Texto ingresado por teclado para cifrar
# texto: Guarda el mensaje originaly se le añade un espacio al final
# texto_encriptado: Guarda el texto final cifrado
# n: Guarda la longitud del mensaje
# i: Variable iteradora de la cadena. Marca el límite superior de las subcadenas
# j: Guarda el límite inferior de las subcadenas
# k: Variable iteradora de las subcadenas
# l: Variable iteradora de las subcadenas
# tc1: Guarda el carácter en posición par
# tc2: Guarda el carácter en posición impar


print("\n\033[32m", "-" * 50, "\033[0m")
print("\033[32m", "-" * 12, "Codificación de mensajes" ,"-" * 12, "\033[0m")
print("\033[32m", "-" * 50, "\033[0m")
mensaje = input("Mensaje: ")
texto = mensaje + " "
n = len(texto)
if n > 0:
    texto_encriptado = ""
    j = 0
    for i in range(n):
        if texto[i] == ' ':
            tc1 = texto[j]
            tc2 = ""
            k = j + 1
            l = 1
            while k < i:
                if l % 2 == 0:
                    tc1 += texto[k]
                else:
                    tc2 += texto[k]
                k = k + 1
                l = l + 1
            j = i + 1
            texto_encriptado += tc1 + tc2 + " "   
        if texto[i] in 'aáAÁ':
            texto = texto[:i] + "1" + texto[i+1:]
        elif texto[i] in 'eéEÉ':
            texto = texto[:i] + "2" + texto[i+1:]
        elif texto[i] in 'iíIÍ':
            texto = texto[:i] + "3" + texto[i+1:]
        elif texto[i] in 'oóOÓ':
            texto = texto[:i] + "4" + texto[i+1:]
        elif texto[i] in 'uúUÚ':
            texto = texto[:i] + "5" + texto[i+1:]
    print("\033[33m", end = "")
    print(f"Mensaje encriptado: {texto_encriptado}")
    print("\033[0m")
else:
    print("\n")
    print("\033[31m")
    print("-" * 38)
    print("¡Error! No ingresó el mensaje")
    print("-" * 38)
    print("\033[0m")
  