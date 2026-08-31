print("Este programa sirve para calcular el area y el perimetro de un circulo")

# 1. pido el valor de r
r = float(input("Ingrese el valor de r: "))

# 2. calcular el area
pi = 3.1416
a = pi * r ** 2

# 3. calcular el perimetro
p = 2 * pi * r

# 4. mostrar el resultado
print("El area y el perimetro de un circulo con radio ", r, " son:")
print("A = ", a)
print("p = ", p)
