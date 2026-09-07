# ----------------------------------------
# Programa: Ejercicio o)
# ----------------------------------------

# ----------------------------------------
# Definición de variables
# ----------------------------------------
# posicion: posicion (número entero mayor a 0) 
# fila: fila correspondiente al estante (fila en la matriz)
# columna: columna correspondiente al compartimento (columna en la matriz)

posicion = int(input("Posición: "))
if posicion > 0:
    fila = posicion // 10
    columna = posicion % 10
    print(f"Estante (fila): {fila}")
    if columna == 1:
        print("Ubicación: Borde izquierdo")
    elif columna == 0:
        print("Ubicación: Borde derecho")
    else:
        print("Ubicación: Zona central")
else:
    print("Coordenada inválida")