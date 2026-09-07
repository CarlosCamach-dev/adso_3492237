edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad <= 12:
    print("Calsificacion: Niño.")
elif edad >= 13 and edad <= 17:
    print("Clasificacion: Adolescente.")
elif edad >= 18 and edad < 60:
    print("Clasificacion: Adulto.")
else:
    print("Clasificacion: Adulto mayor.")