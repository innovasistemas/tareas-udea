# Equivalencia de 1 milla en metros 
milla_metros = 1609.34

# Datos de entrada
Vmh = float(input("Velocidad (Mi/h): "))

# Convertir Mi/h a m/s y a Km/h
Vms = Vmh * milla_metros / 3600
Vkh = milla_metros / 1000

# Salida
print(f"Velocidad (m/s): Vms = {Vms}")
print(f"Velocidad (Km/h): Vkh = {Vkh}")