import math

# Datos de entrada: Solicitar el radio al usuario
r = float(input("Radio circunferencia: "))

# Calcular el perímetro y el área de la circunferencia
P = 2 * math.pi * r
A = 2 * math.pi * r ** 2

# Dados de salida: Mostrar los resultados encontrados
print(f"Radio ingresado: {r}")
print(f"Perímetro: {P} Unid")
print(f"Área: {A}")