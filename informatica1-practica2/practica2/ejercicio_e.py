# ----------------------------------------
# Programa: Ejercicio e)
# ----------------------------------------

# ----------------------------------------
# Definición de variables
# ----------------------------------------
# total_grados: Total Grados que ha rotado el motor
# angulo_final: Ángulo Final en que queda en respecto al eje de partida

total_grados = float(input("Grados de rotación: "))
angulo_final = total_grados % 360
print("Ángulo final: " + str(angulo_final) + "°")
