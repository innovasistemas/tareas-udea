# ----------------------------------------
# Programa: Ejercicio c)
# ----------------------------------------

# ----------------------------------------
# Definición de variables
# ----------------------------------------
# milla_metros: equivalencia de una milla terrestre en metros
# milla_km: equivalencia de una milla terrestre en kilómetros
# Vmh: Velocidad en metros por hora
# Vms: Velocidad en metros por segundo
# Vkh: Velocidad en kilómetros por hora 



# Equivalencia de 1 milla en metros 
milla_metros = 1609.34
milla_km = milla_metros / 1000

# Datos de entrada
Vmh = float(input("Velocidad (Mi/h): "))

# Convertir Mi/h a m/s y a Km/h
Vkh = milla_km * Vmh
Vms = Vkh * 1000 / 3600

# Salida
print(f"Velocidad (Km/h): Vkh = {Vkh}")
print(f"Velocidad (m/s): Vms = {Vms}")