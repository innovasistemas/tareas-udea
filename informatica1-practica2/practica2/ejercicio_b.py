# Datos de entrada
print("Punto 1 de coordenadas (x1, y1)")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
print("Punto 2 de coordenadas (x2, y2)")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

# Calcular la distancia entre (x1, y1) y (x2, y2)
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

# Salida: mostrar la distancia por pantalla
print(f"Distancia entre ({x1}, {y1}) y ({x2}, {y2}) = {d}")