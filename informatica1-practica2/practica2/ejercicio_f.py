# ----------------------------------------
# Programa: Ejercicio f)
# ----------------------------------------

# ----------------------------------------
# Definición de variables
# ----------------------------------------
# sucursal: Sucursal del empleado. Admite los valores A y B
# nht: Número de Horas Trabajadas por el empleado a la semana
# nhb: Número de Horas sin contar extras
# nhe: Número de Horas Extras
# nhjb: Número de Horas Jornada Base 
# vh: Valor Hora sin recargo
# vhe: Valor Hora Extra
# the: Total Hora Extra
# sb: Salario Básico
# sn: Salario Neto
# sw: Swiche, variable para controlar si la sucursal es válida

# Datos de entrada  
sucursal = (input("Sucursal [A | B]: ").upper())
nht = int(input("Número de horas trabajadas: "))
sw = True

if sucursal == "A":
    nhjb = 40
    vh = 10
    vhe = 20
    nhe = nht - nhjb 
elif sucursal == "B":
    nhjb = 45
    vh = 12
    vhe = 25
    nhe = nht - nhjb 
else: 
    sw = False

# Datos de salida
if sw:
    if nhe > 0:
        nhb = nhjb
        the = vhe * nhe
    else: 
        nhb = nht 
        nhe = 0
        the = 0

    sb = nhb * vh
    sn = sb + the

    print("Sucursal: ", sucursal)
    print("Número de Horas Trabajadas: ", nht)
    print("Número de Horas Base: ", nhb)
    print("Número de Horas Extras: ", nhe)
    print("Salario Básico Semanal: ", sb)
    print("Salario Horas Extras: ", the)
    print("Salario Neto: ", sn)
else:
    print("Sucursal no válida")

