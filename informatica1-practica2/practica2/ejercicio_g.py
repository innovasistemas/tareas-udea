print("Este programa sirve para calcular la tarifa que un usuario debe pagar segun su edad.")

# 1. pido la edad del usuario
edad = int(input("Ingrese su edad: "))

# 2. pregunto si el usuario tiene menos de 18 años
if edad < 18:
    if edad < 5:
        print("Debido a que tu edad es ", edad, "tu entrada es gratis")
    elif 5 <= edad <= 12:
        print("Debido a que tu edad es ", edad, "tu tarifa es de niño")    
    else:
        print("Debido a que tu edad es ", edad, "tu tarifa es de joven")
else: # el usuario tiene 18 años o mas
    if edad < 60:
        print("Debido a que tu edad es ", edad, "tu tarifa es de adulto")
    else: # el usuario tiene 60 años o mas
        print("Debido a que tu edad es ", edad, "tu tarifa es de adulto mayor")



